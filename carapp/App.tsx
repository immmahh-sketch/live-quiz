// Box Clever for iPhone and CarPlay. The game itself is the web page (letsquiz.uk), shown full screen; this app adds three things the web
// page cannot do: it listens for spoken answers (a web view has no speech recognition), it keeps running with the screen off or in the
// background (audio mode), and it draws the CarPlay screen from the game's state.
import React, { useCallback, useEffect, useRef } from 'react';
import { SafeAreaView, StatusBar, StyleSheet } from 'react-native';
import { WebView, WebViewMessageEvent } from 'react-native-webview';
import Constants from 'expo-constants';
import { useKeepAwake } from 'expo-keep-awake';
import { ExpoSpeechRecognitionModule, useSpeechRecognitionEvent } from 'expo-speech-recognition';
import { speech, bridge } from './src/inject';
import { startCarPlay } from './src/car';

const extra = (Constants.expoConfig?.extra || {}) as { gameUrl: string; carplay: boolean };

export default function App() {
  useKeepAwake();
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
      car.current = startCarPlay((k, v, ex) => js(`window.lqAct(${JSON.stringify(k)}, ${JSON.stringify(v)}, ${JSON.stringify(ex || {})})`));
    } catch (e) { /* no CarPlay module in this build */ }
    return () => car.current?.stop();
  }, [js]);

  const onMessage = useCallback((ev: WebViewMessageEvent) => {
    let m: any; try { m = JSON.parse(ev.nativeEvent.data); } catch { return; }
    if (m.t === 'speech') {
      if (m.op === 'start') listen(m.id, m.lang);
      else if (m.op === 'stop') { try { ExpoSpeechRecognitionModule.stop(); } catch {} }
      else if (m.op === 'abort') { try { ExpoSpeechRecognitionModule.abort(); } catch {} finish(); }
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
        originWhitelist={['https://*']}
      />
    </SafeAreaView>
  );
}

const s = StyleSheet.create({ root: { flex: 1, backgroundColor: '#1b1544' }, web: { flex: 1, backgroundColor: '#1b1544' } });
