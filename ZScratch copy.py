import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.camera import Camera
from kivy.lang import Builder

#--load cv camera
class Cam(Camera):
    pass


class Microscope(Screen):

    def salve(self):
        print('salved')


#-- main widget 
class Main(Screen):


     #-- take a pic       
    def capture(self):
       self.ids.cam.capture()
#--scene manager
class ScreenManager(ScreenManager):
    pass

#--load my.kv gui
GUI = Builder.load_file('gui.kv')

#--main app
class MyApp(App):

    def build(self):

        return GUI

if __name__ == "__main__":

    MyApp().run()