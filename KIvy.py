# main_kivy.py
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window

# Настройка размеров окна
Window.size = (700, 700)

class GreetingScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()

        # Фоновое изображение
        bg_image = "привет.jpg"
        layout.add_widget(Image(source=bg_image, allow_stretch=True, keep_ratio=False))

        # Приветственный текст
        layout.add_widget(Label(
            text="Привет Мир!",
            font_size=100,
            bold=True,
            color=(1, 1, 1, 1),
            size_hint=(None, None),
            size=(600, 100),
            pos=(20, 300)
        ))

        # Кнопка для перехода к резюме
        button = Button(
            text="Перейти к резюме",
            size_hint=(0.4, 0.1),
            pos_hint={"x": 0.3, "y": 0.1},
            background_color=(0, 0, 0, 0),
            color=(0, 0, 0, 1),
            font_size=25,
            bold=True
        )
        button.bind(on_press=self.go_to_resume)
        layout.add_widget(button)

        self.add_widget(layout)

    def go_to_resume(self, instance):
        self.manager.current = "resume"

class ResumeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()

        # Фон
        bg_image = "стена.jpg"
        layout.add_widget(Image(source=bg_image, allow_stretch=True, keep_ratio=False))

        # Фото поверх фона
        fg_image = "фел.jpg"
        layout.add_widget(Image(source=fg_image, size_hint=(None, None), size=(300, 200), pos=(200, 460)))

        # Текстовые метки
        layout.add_widget(Label(text="Карамян Феликс", font_size=32, pos=(10, 330), color=(0, 0, 0, 1)))
        layout.add_widget(Label(text="Биография:", font_size=25, pos=(-260,80), color=(0, 0, 0, 1)))
        layout.add_widget(Label(text="Студент 2 курса МАИ, М3О-236БВ-24", font_size=20, pos=(-155,50), color=(0, 0, 0, 1)))
        layout.add_widget(Label(text="Умения:", font_size=25, pos=(-280, 20), color=(0, 0, 0, 1)))
        layout.add_widget(Label(text="Красиво фотографирую ", font_size=20, pos=(-220, -5), color=(0, 0, 0, 1)))
        layout.add_widget(Label(text="Опыт:", font_size=25, pos=(-290,-30), color=(0, 0, 0, 1)))
        layout.add_widget(Label(text="Панорама", font_size=20, pos=(-280,-55), color=(0, 0, 0, 1)))

        # Кнопка назад к приветствию
        button = Button(
            text="Назад",
            size_hint=(0.2, 0.1),
            pos_hint={"x":0.4, "y":0.05},
            background_color = (0, 0, 0, 0),
            color = (0, 0, 0, 1),
            font_size=30,
            bold = True
        )
        button.bind(on_press=self.go_to_greeting)
        layout.add_widget(button)

        self.add_widget(layout)

    def go_to_greeting(self, instance):
        self.manager.current = "greeting"

class ResumeApp(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(GreetingScreen(name="greeting"))
        sm.add_widget(ResumeScreen(name="resume"))
        return sm

if __name__ == "__main__":
    ResumeApp().run()
