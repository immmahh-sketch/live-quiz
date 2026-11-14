// The CarPlay native library only compiles with the CarPlay scene delegates in place, so leave it out of the build unless CARPLAY=1
// (the production-carplay profile). A plain build then has no CarPlay code at all, and car.ts never loads it.
module.exports = {
  dependencies: process.env.CARPLAY === '1' ? {} : { '@g4rb4g3/react-native-carplay': { platforms: { ios: null, android: null } } },
};
