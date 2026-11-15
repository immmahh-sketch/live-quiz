// Box Clever for iPhone and CarPlay. Builds run in Expo's cloud (EAS), so no Mac is needed.
// CARPLAY=1 adds the CarPlay scene and entitlement. Leave it off until Apple has approved the CarPlay entitlement for the developer
// account: with it on, the build fails at signing because the provisioning profile cannot carry an entitlement Apple has not granted.
const carplay = process.env.CARPLAY === '1';
module.exports = () => ({
  expo: {
    name: 'Lets Quiz (Carplay Edition)',
    slug: 'box-clever',
    version: '0.2.1',
    orientation: 'portrait',
    icon: './assets/icon.png',
    userInterfaceStyle: 'light',
    newArchEnabled: true,
    // Over-the-air updates (EAS Update): the app's own JavaScript (App.tsx and src/) can be replaced without a new TestFlight build, as long as the
    // native side is unchanged. A new native build needs a new `version` (the runtime version follows it), or old installs would get JS that does not fit.
    runtimeVersion: { policy: 'appVersion' },
    updates: { url: 'https://u.expo.dev/a838db3c-33ec-4657-ab9c-0b4b1671ccce', enabled: true, checkAutomatically: 'ON_LOAD', fallbackToCacheTimeout: 3000 },
    splash: { image: './assets/icon.png', resizeMode: 'contain', backgroundColor: '#1b1544' },
    ios: {
      supportsTablet: false,
      bundleIdentifier: process.env.BUNDLE_ID || 'uk.letsquiz.boxclever',
      infoPlist: {
        UIBackgroundModes: ['audio'],
        ITSAppUsesNonExemptEncryption: false,
        // Apple's upload check wants a purpose text for each of these because the web view library can open them (a game page never does)
        NSPhotoLibraryUsageDescription: 'Box Clever does not use your photos. This is needed only because the web view can offer a photo picker.',
        NSPhotoLibraryAddUsageDescription: 'Box Clever does not save photos.',
        NSCameraUsageDescription: 'Box Clever does not use the camera. This is needed only because the web view can offer a camera option.',
      },
      ...(carplay ? { entitlements: { 'com.apple.developer.carplay-voice-based-conversation': true } } : {}),
    },
    plugins: [
      ['expo-speech-recognition', { microphonePermission: 'Box Clever listens for your answers when you play hands-free.', speechRecognitionPermission: 'Box Clever turns your spoken answers into text while you play hands-free.' }],
      ['expo-build-properties', { ios: { deploymentTarget: '16.4' } }],
      ...(carplay ? ['./plugins/withCarPlay'] : []),
    ],
    extra: { eas: { projectId: 'a838db3c-33ec-4657-ab9c-0b4b1671ccce' }, gameUrl: process.env.GAME_URL || 'https://letsquiz.uk/warmup?pool=1&car=1', carplay },
  },
});
