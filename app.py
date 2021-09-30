from sys import modules
import time
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from video import stream_video, save_settings, read_settings
from threading import Thread
from kivy.uix.popup import Popup

# Fonts Initialization
import kivysome 

kivysome.enable(
    "https://kit.fontawesome.com/378653e3a3.js", group=kivysome.FontGroup.SOLID)

# End Fonts Initialization

history = []
def back_screen(self):
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
    
    def research_window(self):
        history.append(self.name)
        self.manager.current = 'research-screen'
        self.manager.transition.direction = 'left'
    
    def video_window(self):
        history.append(self.name)
        self.manager.current = 'video_mode-screen'
        self.manager.transition.direction = 'left'

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
    host = ObjectProperty(None)
    port = ObjectProperty(None)
    rendering_mode = ObjectProperty(None)
    timer = ObjectProperty(None)
    record = ObjectProperty(None)
    save_button = ObjectProperty(None)
    def __init__(self, **kw):
        super().__init__(**kw)
        self.back = lambda : back_screen(self)
    
    def init_settings(self):
        settings = read_settings()
        self.host.text = settings['host']
        self.port.text = settings['port']
        self.timer.value = settings['timer']
        render = False
        if settings['rendering_mode'] == 1:
            render = True
        self.rendering_mode.active = render
        record = False
        if settings['record'] == 1:
            record = True
        self.record.active = record
        

    def animate_button(self):
        anim_btn = Animation(size_hint=(0.37, 0.72), duration=0.09,
                             transition='out_sine')
        anim_btn += Animation(size_hint=(0.35, 0.7), duration=0.09,
                              transition='out_sine')
        anim_btn.start(self.save_button)
        render = 0 
        record = 0
        if self.rendering_mode.active:
            render = 1
        if self.record.active:
            record = 1
        status = save_settings({'host': self.host.text, 'port': self.port.text,
                      'rendering_mode': render, 'timer': int(self.timer.value), 'record': record})
        title='Error'
        content='Something Went Wrong!'
        if status:
            title = 'Success'
            content = 'Settings are saved.'
        pop = Popup(title=(title), content=Label(
            text=content), size_hint=(None, None), size=(400, 100))
        pop.open()


        
class ResearchWindow(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.back = lambda : back_screen(self)

class VideoMode(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.back = lambda : back_screen(self)

    def open_window(self, video_name, button):
        btn_anim = Animation(size=(260, 160), duration=0.3)
        btn_anim += Animation(size=(250, 150), duration=0.3)
        btn_anim.start(button)
        th1 = Thread(target=stream_video , args=(video_name, ))
        th1.start()
        th1.join()
        return


class AppNavigator(ScreenManager):
    pass

class Launch(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = (1000,650)
        Window.size = self.size
        Window.bind(on_resize=self.reSize)
    
    def reSize(self, *args):
        Window.size = self.size
        return True
    
    def build(self):
        return AppNavigator()
    


if __name__ == '__main__':
    Launch().run()
