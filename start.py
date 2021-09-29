from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.pagelayout import PageLayout


class Wrapper(PageLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)



class TitleScreen:
    pass


class ModuleScreen(AnchorLayout):
    def __init__(self, **kwargs):
        super(ModuleScreen, self).__init__(**kwargs)
        self.current_page = 'title'

    def on_pre(self):
        print(self.current_page)



class Main(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return Wrapper()
    
    

if __name__ == '__main__':
    Main().run()
