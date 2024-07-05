from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.timepicker import TimePicker


class TimePickerApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10)

        self.time_label = Label(text='Выберите время', font_size=30)
        layout.add_widget(self.time_label)

        button = Button(text='Открыть Time Picker', font_size=20)
        button.bind(on_release=self.open_time_picker)
        layout.add_widget(button)

        return layout

    def open_time_picker(self, instance):
        time_picker = TimePicker()

        popup = Popup(title='Выберите время', content=time_picker, size_hint=(None, None), size=(400, 400))

        time_picker.bind(time=self.on_time_select)

        popup.open()

    def on_time_select(self, instance, time):
        self.time_label.text = 'Выбранное время: {}'.format(time)

        instance.parent.parent.dismiss()


if __name__ == '__main__':
    TimePickerApp().run()