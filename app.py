from sys import modules
import time
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty

# Fonts Initialization
import kivysome 

kivysome.enable(
    "https://kit.fontawesome.com/378653e3a3.js", group=kivysome.FontGroup.SOLID)

# End Fonts Initialization

history = []
def back_screen(self):
    print(history)
    screen = history.pop()
    self.manager.current = screen
    self.manager.transition.direction='right'

class StartWindow(Screen):
    project_lbl = ObjectProperty(None)
    start_button = ObjectProperty(None)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.animate()
    def animate(self):
        anim_lbl = Animation(pos=(0, -80), duration=0.7, transition='out_sine')
        anim_lbl.start(self.project_lbl)
    def animate_button(self):
        anim_btn = Animation(size=(280.0, 80.0), duration=0.09,
                             transition='out_sine')
        anim_btn += Animation(size=(260.0, 70.0), duration=0.09,
                             transition='out_sine')
        anim_btn.start(self.start_button)
        self.manager.current = 'modules-screen'
        self.manager.transition.direction='left'
        history.append(self.name)

class ModulesWindow(Screen):
    setting_button = ObjectProperty(None)
    def __init__(self, **kw):
        super().__init__(**kw)
        self.back = lambda : back_screen(self)
    def setting_animate(self):
        anim_btn = Animation(size=(70.0, 70.0), duration=0.06,
                             transition='in_out_quart')
        anim_btn += Animation(size=(60.0, 60.0), duration=0.06,
                              transition='in_out_quart')
        anim_btn.start(self.setting_button)
        self.manager.current='settings-screen'
        self.manager.transition.direction = 'left'
        history.append(self.name)

class SettingWindow(Screen):
    save_button = ObjectProperty(None)
    def __init__(self, **kw):
        super().__init__(**kw)
        self.back = lambda : back_screen(self)
        

    def animate_button(self):
        anim_btn = Animation(size_hint=(0.37, 0.42), duration=0.09,
                             transition='out_sine')
        anim_btn += Animation(size_hint=(0.35, 0.4), duration=0.09,
                              transition='out_sine')
        anim_btn.start(self.save_button)
        



class AppNavigator(ScreenManager):
    pass

class Launch(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = (1100, 800)
        Window.size = self.size
        Window.bind(on_resize=self.reSize)
    
    def reSize(self, *args):
        Window.size = self.size
        return True
    
    def build(self):
        return AppNavigator()
    


if __name__ == '__main__':
    Launch().run()
