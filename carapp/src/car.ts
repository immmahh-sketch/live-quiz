// The car screen. The app has Apple's voice-based conversation entitlement, which is voice-first: the car shows Apple's voice control indicator (what the app is doing:
// ready, speaking, listening), and the quiz is played by voice through the phone, which reads the questions aloud and listens. The first CarPlay build drew a
// list of boxes here; it crashed the moment it connected (the scene handler was the wrong kind for this category), and a list is not what this category is for.
// Only used when the app is built with CarPlay on (CARPLAY=1) and Apple has granted the entitlement.
export type VoiceMode = 'idle' | 'speaking' | 'listening';

export function startCarPlay(_send?: unknown) {
  // required here, not at the top, so a build without CarPlay never loads the native module
  // eslint-disable-next-line @typescript-eslint/no-var-requires
  const { CarPlay, VoiceControlTemplate } = require('@g4rb4g3/react-native-carplay');
  let template: any = null;
  let mode: VoiceMode = 'idle';
  const states = [
    { identifier: 'idle', titleVariants: ["Let's Quiz! Say your choice", "Let's Quiz!"], repeats: false },
    { identifier: 'speaking', titleVariants: ['Speaking…', 'Speaking'], repeats: true },
    { identifier: 'listening', titleVariants: ['Listening…', 'Listening'], repeats: true },
  ];
  const apply = () => { try { template?.activateVoiceControlState(mode); } catch (e) { /* the car may have gone */ } };
  const onConnect = () => {
    template = new VoiceControlTemplate({ voiceControlStates: states });
    CarPlay.setRootTemplate(template, false);
    setTimeout(apply, 300);
  };
  const onDisconnect = () => { template = null; };
  CarPlay.registerOnConnect(onConnect);
  CarPlay.registerOnDisconnect(onDisconnect);
  if (CarPlay.connected) onConnect();

  return {
    setState(_s: unknown) { /* the game's boxes are not shown in the car */ },
    setVoice(m: VoiceMode) { if (m === mode) return; mode = m; apply(); },
    stop() { CarPlay.unregisterOnConnect(onConnect); CarPlay.unregisterOnDisconnect(onDisconnect); },
  };
}
