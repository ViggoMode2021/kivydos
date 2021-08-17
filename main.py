from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
# from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.core.audio import SoundLoader
from kivy.uix.boxlayout import BoxLayout


# define different screens

class TitleWindow(Screen):
    pass

class FirstWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('screenmanager_dos.kv')


class MyLayout(BoxLayout):
    pass
'''
class SoundPlayer(BoxLayout):
    def play_sound(instance,self):
        sound = SoundLoader.load('correcto.mp3')
        if sound:
            sound.volume = 0.1
            sound.play()
'''
class AwesomeApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return kv
        return SoundPlayer()


if __name__ == '__main__':
    AwesomeApp().run()
