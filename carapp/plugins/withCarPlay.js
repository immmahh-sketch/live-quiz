// Expo config plugin: gives the generated iOS app a CarPlay scene next to the phone scene.
//  - Info.plist: a scene manifest with two scenes (the phone's window, and CarPlay)
//  - PhoneSceneDelegate.m: attaches the window the app delegate already built (it holds the React Native view) to the phone scene
//  - CarSceneDelegate.m: hands the car's interface controller and window to react-native-carplay
// Both .m files are copied into the app target and added to its Compile Sources. Nothing else in the generated project is edited.
// Only used when CARPLAY=1 (see app.config.js), because the CarPlay entitlement has to be granted by Apple first.
const fs = require('fs');
const path = require('path');
const { withInfoPlist, withXcodeProject, withDangerousMod, IOSConfig } = require('expo/config-plugins');

const FILES = ['PhoneSceneDelegate.m', 'CarSceneDelegate.m'];

const withSceneManifest = (config) => withInfoPlist(config, (c) => {
  c.modResults.UIApplicationSceneManifest = {
    UIApplicationSupportsMultipleScenes: true,
    UISceneConfigurations: {
      UIWindowSceneSessionRoleApplication: [{ UISceneConfigurationName: 'Phone', UISceneDelegateClassName: 'PhoneSceneDelegate' }],
      CPTemplateApplicationSceneSessionRoleApplication: [{ UISceneConfigurationName: 'CarPlay', UISceneDelegateClassName: 'CarSceneDelegate' }],
    },
  };
  return c;
});

const withCopiedSources = (config) => withDangerousMod(config, ['ios', (c) => {
  const dest = path.join(c.modRequest.platformProjectRoot, c.modRequest.projectName);
  fs.mkdirSync(dest, { recursive: true });
  for (const f of FILES) fs.copyFileSync(path.join(__dirname, 'native', f), path.join(dest, f));
  return c;
}]);

const withCompiledSources = (config) => withXcodeProject(config, (c) => {
  const name = c.modRequest.projectName;
  for (const f of FILES) {
    IOSConfig.XcodeUtils.addBuildSourceFileToGroup({ filepath: path.join(name, f), groupName: name, project: c.modResults });
  }
  return c;
});

module.exports = (config) => withCompiledSources(withCopiedSources(withSceneManifest(config)));
