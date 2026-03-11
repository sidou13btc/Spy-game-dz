import os
import random
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle
from kivy.utils import platform
from kivy.clock import Clock
import arabic_reshaper
from bidi.algorithm import get_display

# --- إعدادات المحرك اللغوي ---
def ar(text):
    if not text: return ""
    reshaped = arabic_reshaper.reshape(text)
    return get_display(reshaped)

# --- الألوان (نفس ذوقك الفني) ---
CLR_BG = [0.008, 0.024, 0.09, 1]  # #020617
CLR_ACCENT = [1, 0.3, 0.3, 1]    # #FF4D4D
CLR_TEXT = [0.97, 0.98, 0.99, 1] # #F8FAFC

# --- طلب الصلاحيات للأندرويد ---
def ask_permissions():
    if platform == 'android':
        from android.permissions import request_permissions, Permission
        request_permissions([
            Permission.READ_EXTERNAL_STORAGE, 
            Permission.WRITE_EXTERNAL_STORAGE,
            Permission.MANAGE_EXTERNAL_STORAGE
        ])

# --- واجهة البداية ---
class HomeScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        with self.canvas.before:
            Color(*CLR_BG)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        
        layout.add_widget(Label(text=ar("الـجـاسـوس"), font_size='50sp', color=CLR_ACCENT, bold=True))
        layout.add_widget(Label(text="DZ VERSION", font_size='20sp', color=[0.5, 0.5, 0.5, 1]))

        btn = Button(text=ar("إبدأ المهمة"), size_hint=(0.8, 0.15), pos_hint={'center_x': 0.5},
                     background_color=CLR_ACCENT, font_size='25sp', bold=True)
        btn.bind(on_press=self.go_to_setup)
        
        layout.add_widget(btn)
        layout.add_widget(Label(text="By Bensahla Sidahmed", font_size='14sp', color=[0.4, 0.4, 0.4, 1]))
        
        self.add_widget(layout)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def go_to_setup(self, instance):
        self.manager.current = 'setup'

# --- واجهة إعداد اللعبة ---
class SetupScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        # سيتم بناء العناصر هنا لتحديد عدد اللاعبين والجواسيس
        layout = BoxLayout(orientation='vertical', padding=30)
        layout.add_widget(Label(text=ar("إعدادات اللعبة"), font_size='30sp'))
        
        # زر مؤقت للانتقال (يمكنك توسيع هذا الجزء لإضافة العدادات)
        start_btn = Button(text=ar("توزيع الأدوار"), size_hint=(1, 0.2), background_color=CLR_ACCENT)
        start_btn.bind(on_press=self.start_game)
        layout.add_widget(start_btn)
        self.add_widget(layout)

    def start_game(self, instance):
        # منطق التوزيع سيوضع هنا
        print("Starting Game...")

# --- مدير الواجهات ---
class SpyApp(App):
    def build(self):
        ask_permissions()
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(SetupScreen(name='setup'))
        return sm

if __name__ == '__main__':
    SpyApp().run()
