// Box Clever for iPhone and CarPlay. Builds run in Expo's cloud (EAS), so no Mac is needed.
// CARPLAY=1 adds the CarPlay scene and entitlement. Leave it off until Apple has approved the CarPlay entitlement for the developer
// account: with it on, the build fails at signing because the provisioning profile cannot carry an entitlement Apple has not granted.
const carplay = process.env.CARPLAY === '1';
module.exports = () => ({
  expo: {
    name: 'Box Clever',
    slug: 'box-clever',
    version: '0.1.0',
    orientation: 'portrait',
    icon: './assets/icon.png',
    userInterfaceStyle: 'light',
    newArchEnabled: true,
    splash: { image: './assets/icon.png', resizeMode: 'contain', backgroundColor: '#1b1544' },
    ios: {
      supportsTablet: false,
      bundleIdentifier: process.env.BUNDLE_ID || 'uk.letsquiz.boxclever',
      infoPlist: {
        UIBackgroundModes: ['audio'],
        ITSAppUsesNonExemptEncryption: false,
        ...(carplay ? { UIRequiredDeviceCapabilities: ['carplay'] } : {}),
      },
      ...(carplay ? { entitlements: { 'com.apple.developer.carplay-voice-based-conversation': true } } : {}),
    },
    plugins: [
      ['expo-speech-recognition', { microphonePermission: 'Box Clever listens for your answers when you play hands-free.', speechRecognitionPermission: 'Box Clever turns your spoken answers into text while you play hands-free.' }],
      ['expo-build-properties', { ios: { deploymentTarget: '16.4' } }],
      ...(carplay ? ['./plugins/withCarPlay'] : []),
    ],
    extra: { eas: { projectId: 'a838db3c-33ec-4657-ab9c-0b4b1671ccce' }, gameUrl: process.env.GAME_URL || 'https://letsquiz.uk/warmup?c=LAURA&boxes=1', carplay },
  },
});
