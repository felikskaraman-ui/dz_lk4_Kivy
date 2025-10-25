# 🎨 Приложение на Kivy: Приветствие и Резюме

## 📚 Архитектура Kivy

**Kivy** — это кроссплатформенный фреймворк для создания графических интерфейсов на Python.  
Он построен на системе экранов (ScreenManager), позволяющей легко переключаться между окнами.

Программа реализует два экрана:
- `GreetingScreen` — экран приветствия
- `ResumeScreen` — экран с резюме пользователя
![telegram-cloud-photo-size-2-5469624754374835033-x](https://github.com/user-attachments/assets/61b4ceef-70d0-4991-9f93-b25d087f9f90)
![telegram-cloud-photo-size-2-5469624754374835034-x](https://github.com/user-attachments/assets/fc6ad0d5-9a91-432f-a5e6-86bee3631977)

---

## ⚙️ Импорты и зависимости

```python
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
```

### Используемые модули:
- **App** — базовый класс приложения.
- **ScreenManager, Screen** — управление переключением экранов.
- **FadeTransition** — плавная анимация перехода.
- **Image, Label, Button** — основные визуальные компоненты.
- **FloatLayout** — гибкое позиционирование элементов.
- **Window** — настройка размеров окна.

---

## 🪟 Настройка окна

Размер окна задаётся заранее:
```python
Window.size = (700, 700)
```

---

## 👋 Класс `GreetingScreen` — экран приветствия

Отображает приветственное сообщение и кнопку перехода к резюме.

### Содержимое:
- Фон — изображение `привет.jpg`
- Текст **«Привет Мир!»** крупным шрифтом
- Кнопка **«Перейти к резюме»** для перехода к следующему экрану

### Логика перехода:
```python
def go_to_resume(self, instance):
    self.manager.current = "resume"
```

---

## 👤 Класс `ResumeScreen` — экран резюме

Создает экран с фоном, фотографией и текстовой информацией.

### Элементы интерфейса:
| Элемент | Содержание | Размер шрифта |
|----------|-------------|---------------|
| Фон | стена.jpg | — |
| Фото | фел.jpg | — |
| Имя | Карамян Феликс | 32 |
| Биография | Студент 2 курса МАИ, М3О-236БВ-24 | 20 |
| Умения | Красиво фотографирую | 20 |
| Опыт | Панорама | 20 |

Также добавлена кнопка **«Назад»** для возврата на экран приветствия.

### Метод возврата:
```python
def go_to_greeting(self, instance):
    self.manager.current = "greeting"
```

---

## 🧩 Класс `ResumeApp` — главный класс приложения

Создаёт экранный менеджер и добавляет оба экрана с плавной анимацией:

```python
sm = ScreenManager(transition=FadeTransition())
sm.add_widget(GreetingScreen(name="greeting"))
sm.add_widget(ResumeScreen(name="resume"))
```

---

## 🚀 Запуск программы

```python
if __name__ == "__main__":
    ResumeApp().run()
```

Метод `run()` запускает главный цикл событий Kivy, обеспечивая интерактивность приложения.

---

## 🧠 Основные принципы Kivy в проекте

- Механизм экранов (`ScreenManager`) для переключения между окнами.
- Абсолютное позиционирование элементов с помощью `FloatLayout`.
- Использование изображений и текста через `Image` и `Label`.
- Событийная модель: кнопки связаны с функциями через `bind(on_press=...)`.

---

## 🧾 Итог

Приложение на Kivy демонстрирует:
- создание нескольких экранов,
- анимацию переходов,
- работу с изображениями и текстом,
- реализацию интерфейса резюме пользователя в интерактивной форме.
