
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.camera import Camera

Builder.load_file("./frontend.kv")


class CameraScreen(Screen):
    def start(self):
        self.cam = Camera(resolution=(320, 240))
        self.cam.play = True

    def stop(self):
        pass

    def capture(self):
        pass


class ImageScreen(Screen):
    pass


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
