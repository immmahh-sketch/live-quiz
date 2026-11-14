# Box Clever app (iPhone + CarPlay), built with Expo

The game is the web page (letsquiz.uk). This app shows it full screen and adds what a web page cannot do:
spoken answers (the app listens for the page), staying alive in the background, and the CarPlay screen.

- `App.tsx` the web view, the listening bridge, the CarPlay hook-up
- `src/inject.js` two scripts put into the page: a SpeechRecognition that asks the app to listen, and a bridge that reads the game's state and sends taps back
- `src/model.ts` what the car list shows for each moment of the game (pure, tested)
- `src/car.ts` draws that list on CarPlay (`@g4rb4g3/react-native-carplay`)
- `plugins/withCarPlay.js` + `plugins/native/*.m` add the CarPlay scene to the generated iOS project (only when `CARPLAY=1`)
- `app.config.js`, `eas.json` the app's settings and the cloud build profiles

## Get it on your iPhone (TestFlight), no Mac needed

Do this once, from a terminal in this folder (`carapp`). It asks for your Expo and Apple logins itself; nothing is stored in the repo.

```bash
npm install
npm install -g eas-cli
eas login
eas init
eas build --platform ios --profile production
eas submit --platform ios --latest
```

- The bundle id is `uk.letsquiz.boxclever` (change it with the `BUNDLE_ID` environment variable, or in `app.config.js`, before the first build).
- `eas build` signs the app with your Apple developer account (it will ask you to log in) and builds on Expo's Macs.
- `eas submit` sends it to App Store Connect; it appears in TestFlight after Apple's short processing.
- This first build has no CarPlay in it. Use it to check the phone side works: the game loads, hands-free listens, shared-phone names work.

## An .ipa file to install yourself (sideload)

```bash
eas device:create          # once: registers your iPhone with your Apple developer account
eas build --platform ios --profile preview
```

When the build finishes, EAS gives a link to the signed .ipa (it also installs straight from that link on a registered iPhone). The file is signed for the phones you registered, so a tool such as Sideloadly or AltStore can install it (they re-sign it with your Apple ID if needed). It cannot be built without your Apple login, so it has to be run from your own terminal.

## The car app plays boxes only

The app opens `warmup?c=LAURA&boxes=1`. `boxes=1` drops every item that is not Box Clever's boxes (Hot Potato and the other mid-game rounds) for that game; the game's own pages are unchanged.

## Turn on CarPlay (after Apple approves the entitlement)

1. Request the entitlement at developer.apple.com (CarPlay request form), category "voice-based conversational". Apple reviews it; games are not a listed category, so it may be refused.
2. When granted, make sure the App ID `uk.letsquiz.boxclever` has the CarPlay capability in the developer portal, then refresh the profile: `eas credentials`.
3. Build with CarPlay switched on and send it to TestFlight:

```bash
eas build --platform ios --profile production-carplay
eas submit --platform ios --latest
```

`CARPLAY=1` adds the CarPlay scene, the `com.apple.developer.carplay-voice-based-conversation` entitlement and `UIRequiredDeviceCapabilities: carplay`. Without Apple's grant the signing step fails, which is why it is off by default.

## What is tested and what is not

Tested here (Windows, no Mac): the injected scripts and the car list logic against the real game in a headless browser (a full two-player game driven by car "taps", and one driven by spoken replies through the listening shim); the config plugin's output (scene manifest, entitlement); the TypeScript.

Never run: the native build, the CarPlay scene delegates (`plugins/native`), the Expo speech module on a device, any real car. The first `eas build --profile production-carplay` will show whether the scene delegates compile and link against `react-native-carplay` (`#import "RNCarPlay.h"`), and the first drive will show how the car's screen and microphone behave. Expect to iterate on these.

## Things to know

- The game runs inside the app's web view. If the phone's app is closed, the game stops; open the app on the phone first, then connect to the car.
- A CarPlay list is a short, plain list: the five categories, then the boxes in a row, then the stakes or the four answers. It is not the drawer cabinet. Questions are read aloud as well, and a long question may be cut off on the car screen.
- Apple's voice-based conversational category allows only a few screens and must be voice-first. If Apple's review objects to touch lists, the voice-only flow still works with CarPlay audio.
