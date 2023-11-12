from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

COLOUR = (1, 0, 1)
ALT_COLOUR = (1, 1, 0)


class LabelsApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name_to_label = {"Zane": "IS THE BEST", "Ryan": "is ok", "Lucas": "knows what he is doing"}

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.name_to_label:
            temp_button = Button(text=name)
            temp_button.bind(on_release=self.press_entry)
            temp_button.background_color = COLOUR
            self.root.ids.entries_box.add_widget(temp_button)

    def press_entry(self, instance):
        name = instance.text
        instance.background_colour = ALT_COLOUR
        self.status_text = f"{name} {self.name_to_label[name]}"


LabelsApp().run()
