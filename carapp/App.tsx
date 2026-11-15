// Box Clever for iPhone and CarPlay. The game itself is the web page (letsquiz.uk), shown full screen; this app adds three things the web
// page cannot do: it listens for spoken answers (a web view has no speech recognition), it keeps running with the screen off or in the
// background (audio mode), and it draws the CarPlay screen from the game's state.
import React, { useCallback, useEffect, useRef, useState } from 'react';
import { ActivityIndicator, Pressable, SafeAreaView, StatusBar, StyleSheet, Text, View } from 'react-native';
import { WebView, WebViewMessageEvent } from 'react-native-webview';
import Constants from 'expo-constants';
import { useKeepAwake } from 'expo-keep-awake';
import { ExpoSpeechRecognitionModule, useSpeechRecognitionEvent } from 'expo-speech-recognition';
import { speech, bridge } from './src/inject';
import { startCarPlay } from './src/car';

const extra = (Constants.expoConfig?.extra || {}) as { gameUrl: string; carplay: boolean };

export default function App() {
  useKeepAwake();
  const [err, setErr] = useState('');
  const web = useRef<WebView>(null);
  const listening = useRef<{ id: number; alts: string[] } | null>(null);
  const car = useRef<ReturnType<typeof startCarPlay> | null>(null);

  const js = useCallback((code: string) => web.current?.injectJavaScript(code + '; true;'), []);
  const finish = useCallback(() => {
    const l = listening.current; if (!l) return;
    listening.current = null;
    js(`window.__lqSRDone(${l.id}, ${JSON.stringify(l.alts)})`);
  }, [js]);

  useSpeechRecognitionEvent('result', (e) => {
    if (!listening.current) return;
    listening.current.alts = (e.results || []).map((r) => r.transcript).filter(Boolean).slice(0, 4);
    if (e.isFinal) finish();
  });
  useSpeechRecognitionEvent('end', finish);
  useSpeechRecognitionEvent('error', finish);

  const listen = useCallback(async (id: number, lang: string) => {
    finish();
    try {
      const perm = await ExpoSpeechRecognitionModule.requestPermissionsAsync();
      if (!perm.granted) { js(`window.__lqSRDone(${id}, [])`); return; }
      listening.current = { id, alts: [] };
      ExpoSpeechRecognitionModule.start({ lang: lang || 'en-GB', interimResults: false, maxAlternatives: 4, continuous: false });
    } catch (e) { listening.current = null; js(`window.__lqSRDone(${id}, [])`); }
  }, [finish, js]);

  useEffect(() => {
    if (!extra.carplay) return;
    try {
      car.current = startCarPlay();
    } catch (e) { /* no CarPlay module in this build */ }
    return () => car.current?.stop();
  }, [js]);

  const onMessage = useCallback((ev: WebViewMessageEvent) => {
    let m: any; try { m = JSON.parse(ev.nativeEvent.data); } catch { return; }
    if (m.t === 'speech') {
      if (m.op === 'start') listen(m.id, m.lang);
      else if (m.op === 'stop') { try { ExpoSpeechRecognitionModule.stop(); } catch {} }
      else if (m.op === 'abort') { try { ExpoSpeechRecognitionModule.abort(); } catch {} finish(); }
    } else if (m.t === 'voice') {
      try { car.current?.setVoice(m.s); } catch {} // what the page is doing: speaking, listening or idle (shown on the car screen)
    } else if (m.t === 'state') {
      try { car.current?.setState(JSON.parse(m.s)); } catch {}
    }
  }, [finish, listen]);

  return (
    <SafeAreaView style={s.root}>
      <StatusBar barStyle="light-content" />
      <WebView
        ref={web}
        style={s.web}
        source={{ uri: extra.gameUrl }}
        injectedJavaScriptBeforeContentLoaded={speech}
        injectedJavaScriptBeforeContentLoadedForMainFrameOnly={false}
        injectedJavaScript={bridge}
        onMessage={onMessage}
        javaScriptEnabled
        domStorageEnabled
        allowsInlineMediaPlayback
        mediaPlaybackRequiresUserAction={false}
        setSupportMultipleWindows={false}
        originWhitelist={['*']}
        startInLoadingState
        renderLoading={() => <View style={s.center}><ActivityIndicator color="#fff" size="large" /><Text style={s.sub}>Loading Box Clever…</Text></View>}
        onLoadStart={() => setErr('')}
        onError={(e) => setErr(e.nativeEvent.description || 'The game could not be loaded.')}
        onHttpError={(e) => setErr('The game returned an error (' + e.nativeEvent.statusCode + ').')}
      />
      {err ? (
        <View style={[s.center, s.over]}>
          <Text style={s.msg}>{err}</Text>
          <Text style={s.sub}>Check the phone's internet connection.</Text>
          <Pressable style={s.btn} onPress={() => { setErr(''); web.current?.reload(); }}><Text style={s.btnt}>Try again</Text></Pressable>
        </View>
      ) : null}
    </SafeAreaView>
  );
}

const s = StyleSheet.create({
  root: { flex: 1, backgroundColor: '#1b1544' }, web: { flex: 1, backgroundColor: '#1b1544' },
  center: { flex: 1, alignItems: 'center', justifyContent: 'center', padding: 24 },
  over: { position: 'absolute', left: 0, right: 0, top: 0, bottom: 0, backgroundColor: '#1b1544' },
  msg: { color: '#fff', fontSize: 22, fontWeight: '800', textAlign: 'center' }, sub: { color: '#fff', opacity: 0.7, marginTop: 8, marginBottom: 20, textAlign: 'center' },
  btn: { backgroundColor: '#ffd54a', borderRadius: 14, paddingVertical: 14, paddingHorizontal: 28 }, btnt: { color: '#1b1544', fontSize: 18, fontWeight: '900' },
});
