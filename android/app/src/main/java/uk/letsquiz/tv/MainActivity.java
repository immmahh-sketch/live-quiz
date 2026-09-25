package uk.letsquiz.tv;

import android.app.Activity;
import android.content.Intent;
import android.content.pm.ApplicationInfo;
import android.graphics.Bitmap;
import android.graphics.Color;
import android.media.projection.MediaProjectionManager;
import android.os.Build;
import android.net.Uri;
import android.os.Bundle;
import android.view.KeyEvent;
import android.view.View;
import android.view.ViewGroup;
import android.view.Window;
import android.view.WindowManager;
import android.webkit.JavascriptInterface;
import android.webkit.WebChromeClient;
import android.webkit.WebResourceError;
import android.webkit.WebResourceRequest;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.FrameLayout;

import org.json.JSONObject;

/**
 * Let's Quiz! for Fire TV: a full-screen WebView on letsquiz.uk/tv, the TV-only page that is
 * built for a remote's ring and centre button. Everything else (the quiz writer, the game,
 * the phones) lives on the website, so this app almost never needs updating.
 */
public class MainActivity extends Activity {
    private static final String HOME = "https://letsquiz.uk/tv";
    private WebView web;
    private FrameLayout root;
    private View fullscreenView;
    private WebChromeClient.CustomViewCallback fullscreenCallback;
    private static final int REQ_CAPTURE = 41;
    /** A frame is on its way to the page; newer ones are dropped until it has been painted. */
    private volatile boolean framePending;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN, WindowManager.LayoutParams.FLAG_FULLSCREEN);
        getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);

        root = new FrameLayout(this);
        root.setBackgroundColor(Color.parseColor("#1b1544"));
        // Debug builds only: lets Chrome DevTools on a computer inspect the page.
        if ((getApplicationInfo().flags & ApplicationInfo.FLAG_DEBUGGABLE) != 0) WebView.setWebContentsDebuggingEnabled(true);
        web = new WebView(this);
        web.setBackgroundColor(Color.parseColor("#1b1544"));
        web.setLayoutParams(new FrameLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.MATCH_PARENT));
        root.addView(web);
        setContentView(root);

        WebSettings s = web.getSettings();
        s.setJavaScriptEnabled(true);
        s.setDomStorageEnabled(true);
        s.setDatabaseEnabled(true);
        s.setMediaPlaybackRequiresUserGesture(false);
        s.setLoadWithOverviewMode(true);
        s.setUseWideViewPort(true);
        s.setSupportZoom(false);
        s.setBuiltInZoomControls(false);
        s.setCacheMode(WebSettings.LOAD_DEFAULT);
        s.setMixedContentMode(WebSettings.MIXED_CONTENT_NEVER_ALLOW);
        // The site switches into TV mode (big focus rings, D-pad navigation) when it sees this.
        s.setUserAgentString(s.getUserAgentString() + " LetsQuizTV/1.0");

        web.setWebViewClient(new WebViewClient() {
            @Override
            public boolean shouldOverrideUrlLoading(WebView view, WebResourceRequest request) {
                Uri u = request.getUrl();
                String host = u.getHost() == null ? "" : u.getHost();
                // Stay inside the quiz; anything else (a YouTube link, say) is not for the TV.
                if (host.endsWith("letsquiz.uk") || host.endsWith("github.io") || host.equals("localhost")) return false;
                return true;
            }

            @Override
            public void onReceivedError(WebView view, WebResourceRequest request, WebResourceError error) {
                if (request.isForMainFrame()) view.loadData(offlinePage(), "text/html; charset=utf-8", "utf-8");
            }
        });

        web.setWebChromeClient(new WebChromeClient() {
            @Override
            public void onShowCustomView(View view, CustomViewCallback callback) {
                // Full-screen video (a YouTube clip on a question).
                if (fullscreenView != null) { callback.onCustomViewHidden(); return; }
                fullscreenView = view; fullscreenCallback = callback;
                web.setVisibility(View.GONE);
                root.addView(view, new FrameLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.MATCH_PARENT));
            }

            @Override
            public void onHideCustomView() {
                if (fullscreenView == null) return;
                root.removeView(fullscreenView);
                fullscreenView = null;
                if (fullscreenCallback != null) fullscreenCallback.onCustomViewHidden();
                fullscreenCallback = null;
                web.setVisibility(View.VISIBLE);
                web.requestFocus();
            }
        });

        // The TV page's "Exit to Fire TV" button calls LetsQuizApp.exit().
        web.addJavascriptInterface(new AppBridge(), "LetsQuizApp");

        web.setFocusable(true);
        web.setFocusableInTouchMode(true);
        web.requestFocus();
        if (savedInstanceState != null) web.restoreState(savedInstanceState); else web.loadUrl(HOME);
    }

    /**
     * What the web page may ask of the app: to close it completely (not just send it to the
     * background), and to start or stop sharing the screen into the quiz call.
     */
    private final class AppBridge {
        @JavascriptInterface
        public void exit() {
            runOnUiThread(() -> finishAndRemoveTask());
        }

        @JavascriptInterface
        public void startCapture() {
            runOnUiThread(() -> {
                if (CaptureService.running) { toPage("started", ""); return; }
                CaptureService.sink = sink;
                MediaProjectionManager mpm = (MediaProjectionManager) getSystemService(MEDIA_PROJECTION_SERVICE);
                try { startActivityForResult(mpm.createScreenCaptureIntent(), REQ_CAPTURE); }
                catch (Exception e) { toPage("error", "This Fire TV cannot share its screen"); }
            });
        }

        @JavascriptInterface
        public void stopCapture() {
            runOnUiThread(() -> stopService(new Intent(MainActivity.this, CaptureService.class)));
        }
    }

    // Frames and news from the capture service, passed on to the web page (window.__lqFrame / __lqCaptureState).
    private final CaptureService.Sink sink = new CaptureService.Sink() {
        @Override public boolean ready() { return !framePending; }
        @Override public void frame(String dataUrl) {
            framePending = true;
            String js = "window.__lqFrame&&window.__lqFrame('" + dataUrl + "')";
            web.post(() -> web.evaluateJavascript(js, v -> framePending = false));
        }
        @Override public void state(String state, String message) { web.post(() -> toPage(state, message)); }
    };

    private void toPage(String state, String message) {
        String js = "window.__lqCaptureState&&window.__lqCaptureState(" + JSONObject.quote(state) + "," + JSONObject.quote(message) + ")";
        web.evaluateJavascript(js, null);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode != REQ_CAPTURE) return;
        if (resultCode != RESULT_OK || data == null) { toPage("denied", "Screen sharing was not allowed"); return; }
        Intent svc = new Intent(this, CaptureService.class)
            .putExtra(CaptureService.EXTRA_CODE, resultCode)
            .putExtra(CaptureService.EXTRA_DATA, data);
        if (Build.VERSION.SDK_INT >= 26) startForegroundService(svc); else startService(svc);
    }

    private String offlinePage() {
        return "<!doctype html><html><body style='margin:0;background:#1b1544;color:#fff;font-family:sans-serif;display:flex;align-items:center;justify-content:center;height:100vh;text-align:center'>"
            + "<div><div style='font-size:64px'>📡</div><h1>Can't reach letsquiz.uk</h1><p style='font-size:20px;opacity:.8'>Check the Fire TV's internet connection, then press the centre button to try again.</p>"
            + "<button onclick=\"location.href='" + HOME + "'\" autofocus style='font-size:24px;padding:14px 28px;border-radius:14px;border:0;background:#ffd60a;font-weight:bold'>Try again</button></div></body></html>";
    }

    @Override
    public boolean onKeyDown(int keyCode, KeyEvent event) {
        if (keyCode == KeyEvent.KEYCODE_BACK) {
            if (fullscreenView != null) { web.getWebChromeClient(); onBackPressed(); return true; }
            if (web.canGoBack()) { web.goBack(); return true; }
            moveTaskToBack(true);
            return true;
        }
        // Media keys on the remote: treat play/pause as the centre button.
        if (keyCode == KeyEvent.KEYCODE_MEDIA_PLAY_PAUSE || keyCode == KeyEvent.KEYCODE_MEDIA_PLAY) {
            web.dispatchKeyEvent(new KeyEvent(KeyEvent.ACTION_DOWN, KeyEvent.KEYCODE_DPAD_CENTER));
            web.dispatchKeyEvent(new KeyEvent(KeyEvent.ACTION_UP, KeyEvent.KEYCODE_DPAD_CENTER));
            return true;
        }
        return super.onKeyDown(keyCode, event);
    }

    @Override
    public void onBackPressed() {
        if (fullscreenView != null) {
            root.removeView(fullscreenView);
            fullscreenView = null;
            if (fullscreenCallback != null) fullscreenCallback.onCustomViewHidden();
            fullscreenCallback = null;
            web.setVisibility(View.VISIBLE);
            web.requestFocus();
            return;
        }
        if (web.canGoBack()) web.goBack(); else moveTaskToBack(true);
    }

    @Override
    protected void onSaveInstanceState(Bundle outState) {
        super.onSaveInstanceState(outState);
        web.saveState(outState);
    }

    @Override
    protected void onNewIntent(Intent intent) {
        super.onNewIntent(intent);
        web.requestFocus();
    }

    @Override
    protected void onDestroy() {
        stopService(new Intent(this, CaptureService.class));
        CaptureService.sink = null;
        web.destroy();
        super.onDestroy();
    }
}
