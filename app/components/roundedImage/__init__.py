import os
from kivy.lang import Builder
from kivy.uix.image import AsyncImage

class RoundedImage(AsyncImage):
    pass

file_path = os.path.dirname(__file__)

Builder.load_file(os.path.join(file_path,'roundedImage.kv'))