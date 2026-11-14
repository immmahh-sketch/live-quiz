#import <UIKit/UIKit.h>

// The phone's scene. The app delegate has already built the window with the React Native view in it; this puts that window on the scene.
@interface PhoneSceneDelegate : UIResponder <UIWindowSceneDelegate>
@property (nonatomic, strong) UIWindow *window;
@end

@implementation PhoneSceneDelegate

- (void)scene:(UIScene *)scene willConnectToSession:(UISceneSession *)session options:(UISceneConnectionOptions *)connectionOptions {
  if (![scene isKindOfClass:[UIWindowScene class]]) return;
  id<UIApplicationDelegate> app = [UIApplication sharedApplication].delegate;
  UIWindow *window = app.window;
  if (window == nil) return;
  window.windowScene = (UIWindowScene *)scene;
  self.window = window;
  [window makeKeyAndVisible];
}

@end
