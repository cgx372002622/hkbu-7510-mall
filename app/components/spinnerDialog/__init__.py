from kivymd.uix.dialog import MDDialog
import os
from kivy.lang import Builder

class SpinnerDialog(MDDialog):
    def show(self):
        self.open()

    def hide(self):
        self.dismiss()

file_path = os.path.dirname(__file__)

Builder.load_file(os.path.join(file_path,'spinnerDialog.kv'))

