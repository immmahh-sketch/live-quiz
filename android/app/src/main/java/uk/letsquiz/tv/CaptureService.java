package uk.letsquiz.tv;

import android.app.Activity;
import android.app.Notification;
import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.app.Service;
import android.content.Context;
import android.content.Intent;
import android.content.pm.ServiceInfo;
import android.graphics.Bitmap;
import android.graphics.PixelFormat;
import android.hardware.display.DisplayManager;
import android.hardware.display.VirtualDisplay;
import android.media.Image;
import android.media.ImageReader;
import android.media.projection.MediaProjection;
import android.media.projection.MediaProjectionManager;
import android.os.Build;
import android.os.Handler;
import android.os.HandlerThread;
import android.os.IBinder;
import android.os.SystemClock;
import android.util.Base64;

import java.io.ByteArrayOutputStream;
import java.nio.ByteBuffer;

/**
 * Captures the TV screen for the quiz call (Android's MediaProjection), about 8 frames a second
 * at 1280x720, and hands each one to MainActivity as a JPEG data URL. The web page paints them on
 * a canvas and sends that into the call. Android 10 and later only allow screen capture from a
 * foreground service, hence a service rather than doing it in the activity.
 */
public class CaptureService extends Service {
    /** Where frames go (MainActivity). Frames are dropped while the page is still busy with the last one. */
    public interface Sink {
        boolean ready();
        void frame(String dataUrl);
        void state(String state, String message);
    }

    public static final String EXTRA_CODE = "code", EXTRA_DATA = "data";
    private static final int W = 1280, H = 720, FRAME_MS = 125, NOTE_ID = 7;
    static volatile Sink sink;
    static volatile boolean running;

    private MediaProjection projection;
    private VirtualDisplay display;
    private ImageReader reader;
    private HandlerThread thread;
    private long last;
    private Bitmap bitmap;
    private final ByteArrayOutputStream jpeg = new ByteArrayOutputStream(96 * 1024);

    @Override
    public IBinder onBind(Intent intent) { return null; }

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        startInForeground();
        if (intent == null || running) return START_NOT_STICKY;
        int code = intent.getIntExtra(EXTRA_CODE, Activity.RESULT_CANCELED);
        Intent data = intent.getParcelableExtra(EXTRA_DATA);
        try {
            MediaProjectionManager mpm = (MediaProjectionManager) getSystemService(Context.MEDIA_PROJECTION_SERVICE);
            projection = mpm.getMediaProjection(code, data);
            if (projection == null) throw new IllegalStateException("no projection");
            thread = new HandlerThread("quiz-call-capture");
            thread.start();
            Handler handler = new Handler(thread.getLooper());
            // Android 14 wants a callback registered before the virtual display exists.
            projection.registerCallback(new MediaProjection.Callback() {
                @Override public void onStop() { stopSelf(); }
            }, handler);
            reader = ImageReader.newInstance(W, H, PixelFormat.RGBA_8888, 2);
            reader.setOnImageAvailableListener(this::onImage, handler);
            int dpi = getResources().getDisplayMetrics().densityDpi;
            display = projection.createVirtualDisplay("LetsQuizCall", W, H, dpi, DisplayManager.VIRTUAL_DISPLAY_FLAG_AUTO_MIRROR, reader.getSurface(), null, handler);
            running = true;
            Sink s = sink;
            if (s != null) s.state("started", "");
        } catch (Exception e) {
            Sink s = sink;
            if (s != null) s.state("error", "Screen capture failed: " + e.getMessage());
            stopSelf();
        }
        return START_NOT_STICKY;
    }

    private void onImage(ImageReader r) {
        Image img = null;
        try {
            img = r.acquireLatestImage();
            if (img == null) return;
            long now = SystemClock.uptimeMillis();
            Sink s = sink;
            if (s == null || now - last < FRAME_MS || !s.ready()) return;
            last = now;
            Image.Plane p = img.getPlanes()[0];
            ByteBuffer buf = p.getBuffer();
            int pixelStride = p.getPixelStride(), rowStride = p.getRowStride();
            int padded = rowStride / pixelStride; // rows can be wider than the image
            if (bitmap == null || bitmap.getWidth() != padded) bitmap = Bitmap.createBitmap(padded, H, Bitmap.Config.ARGB_8888);
            bitmap.copyPixelsFromBuffer(buf);
            Bitmap frame = padded == W ? bitmap : Bitmap.createBitmap(bitmap, 0, 0, W, H);
            jpeg.reset();
            frame.compress(Bitmap.CompressFormat.JPEG, 70, jpeg);
            if (frame != bitmap) frame.recycle();
            s.frame("data:image/jpeg;base64," + Base64.encodeToString(jpeg.toByteArray(), Base64.NO_WRAP));
        } catch (Exception ignored) {
        } finally {
            if (img != null) img.close();
        }
    }

    private void startInForeground() {
        Notification.Builder b;
        if (Build.VERSION.SDK_INT >= 26) {
            NotificationManager nm = (NotificationManager) getSystemService(Context.NOTIFICATION_SERVICE);
            nm.createNotificationChannel(new NotificationChannel("call", "Quiz call", NotificationManager.IMPORTANCE_LOW));
            b = new Notification.Builder(this, "call");
        } else {
            b = new Notification.Builder(this);
        }
        Notification n = b.setContentTitle("Let's Quiz is on the quiz call")
            .setContentText("The TV screen is being shared")
            .setSmallIcon(R.mipmap.ic_launcher)
            .setOngoing(true)
            .build();
        if (Build.VERSION.SDK_INT >= 29) startForeground(NOTE_ID, n, ServiceInfo.FOREGROUND_SERVICE_TYPE_MEDIA_PROJECTION);
        else startForeground(NOTE_ID, n);
    }

    @Override
    public void onDestroy() {
        boolean was = running;
        running = false;
        try { if (display != null) display.release(); } catch (Exception ignored) {}
        try { if (reader != null) reader.close(); } catch (Exception ignored) {}
        try { if (projection != null) projection.stop(); } catch (Exception ignored) {}
        if (thread != null) thread.quitSafely();
        display = null; reader = null; projection = null; thread = null;
        Sink s = sink;
        if (was && s != null) s.state("stopped", "");
        super.onDestroy();
    }
}
