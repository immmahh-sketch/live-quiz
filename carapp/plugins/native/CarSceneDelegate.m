#import <CarPlay/CarPlay.h>
#if __has_include(<react-native-carplay/RNCarPlay.h>)
#import <react-native-carplay/RNCarPlay.h>
#else
#import "RNCarPlay.h"
#endif

// The car's scene: gives react-native-carplay the car's interface controller and window, and tells it when the car screen is showing.
@interface CarSceneDelegate : UIResponder <CPTemplateApplicationSceneDelegate>
@end

@implementation CarSceneDelegate

- (void)templateApplicationScene:(CPTemplateApplicationScene *)templateApplicationScene
   didConnectInterfaceController:(CPInterfaceController *)interfaceController
                        toWindow:(CPWindow *)window {
  [RNCarPlay connectWithInterfaceController:interfaceController window:window];
}

- (void)templateApplicationScene:(CPTemplateApplicationScene *)templateApplicationScene
didDisconnectInterfaceController:(CPInterfaceController *)interfaceController
                      fromWindow:(CPWindow *)window {
  [RNCarPlay disconnect];
}

- (void)sceneDidBecomeActive:(UIScene *)scene { [RNCarPlay stateChanged:YES]; }
- (void)sceneWillResignActive:(UIScene *)scene { [RNCarPlay stateChanged:NO]; }

@end
