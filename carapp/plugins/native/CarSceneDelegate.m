#import <CarPlay/CarPlay.h>
#if __has_include(<react-native-carplay/RNCarPlay.h>)
#import <react-native-carplay/RNCarPlay.h>
#else
#import "RNCarPlay.h"
#endif

// The car's scene: gives react-native-carplay the car's interface controller, and tells it when the car screen is showing.
// An app with the voice-based conversation entitlement (not navigation) must implement the plain didConnectInterfaceController: method. The version with a
// CPWindow is for navigation apps only: with just that one, CarPlay raises an exception the moment the app is opened on the car screen (the first CarPlay build
// crashed this way). Such apps have no CPWindow (carWindow is nil), so a spare window stands in for the one the library expects.
@interface CarSceneDelegate : UIResponder <CPTemplateApplicationSceneDelegate>
@end

@implementation CarSceneDelegate

- (void)templateApplicationScene:(CPTemplateApplicationScene *)templateApplicationScene
   didConnectInterfaceController:(CPInterfaceController *)interfaceController {
  UIWindow *w = (UIWindow *)templateApplicationScene.carWindow;
  if (w == nil) w = [[UIWindow alloc] initWithFrame:CGRectMake(0, 0, 1, 1)];
  [RNCarPlay connectWithInterfaceController:interfaceController window:(CPWindow *)w];
}

- (void)templateApplicationScene:(CPTemplateApplicationScene *)templateApplicationScene
didDisconnectInterfaceController:(CPInterfaceController *)interfaceController {
  [RNCarPlay disconnect];
}

- (void)sceneDidBecomeActive:(UIScene *)scene { [RNCarPlay stateChanged:YES]; }
- (void)sceneWillResignActive:(UIScene *)scene { [RNCarPlay stateChanged:NO]; }

@end
