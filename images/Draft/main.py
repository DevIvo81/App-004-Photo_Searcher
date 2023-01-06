import os, wikipedia, requests
os.system("cls")

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_file("./frontend.kv")

page = wikipedia.page("beach", auto_suggest=False)

class FirstScreen(Screen):
    def search_image(self):
        # Get user query from TextInput
        query = self.manager.current_screen.ids.user_query.text
        # Get wikipedia page and first image link
        page = wikipedia.page(query, auto_suggest=False)
        image_link = page.images[0]
        # Download the image
        req = requests.get(image_link)
        imagepath = "./images/image.jpg"
        with open(imagepath, "wb") as file:
            file.write(req.content)
        # Set the image in the Image widget
        if not query:
            self.manager.current_screen.ids.img.source = 'images/CanyonGrail.jpg'
        else:
            self.manager.current_screen.ids.img.source = 'images/image.jpg'

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    
    def build(self):
        return RootWidget()
        

if __name__ == "__main__":
    app = MainApp()
    app.run()
    print(page)
