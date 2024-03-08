from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class ForestryCollegeApp(MDApp):
    def build(self):
        return MDLabel(text="Привет, это Лесо_колледж!", halign="center")


ForestryCollegeApp().run()