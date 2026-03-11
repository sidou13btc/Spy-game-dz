import os
import random
import time
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import arabic_reshaper
from bidi.algorithm import get_display

# ---------------- المحرك البصري واللغوي ----------------
def ar(text):
    if not text: return ""
    reshaped = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped)
    return bidi_text

CLR_BG = "#020617"
CLR_CARD = "#0F172A"
CLR_ACCENT = "#FF4D4D"
CLR_TEXT = "#F8FAFC"
CLR_SUB = "#94A3B8"

# تحديد المسارات لتكون متوافقة مع أندرويد
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UI_DIR = os.path.join(BASE_DIR, "ui_images")
PLAYER_DIR = os.path.join(BASE_DIR, "player_images")
EXTS = (".png", ".jpg", ".jpeg", ".webp")

IMG_WIDTH = 680
IMG_HEIGHT = 1000

root = tk.Tk()
root.title("Spy Game")
root.configure(bg=CLR_BG)

# جعل التطبيق يملأ الشاشة في أندرويد
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

main_frame = tk.Frame(root, bg=CLR_BG)
main_frame.pack(fill="both", expand=True)

# باقي المنطق البرمجي (المتغيرات والدوال)
players_var = tk.IntVar(value=5)
spies_var = tk.IntVar(value=1)
minutes_var = tk.IntVar(value=2)
saved_names = []
session_players = []
current_idx = 0
timer_active = False
available_secrets = []
image_cache = {}

def refresh_available_secrets():
    global available_secrets
    try:
        if os.path.exists(PLAYER_DIR):
            all_imgs = [f for f in os.listdir(PLAYER_DIR) if f.lower().endswith(EXTS)]
            spy_img = next((f for f in all_imgs if f.startswith("26051997")), all_imgs[0] if all_imgs else None)
            if spy_img:
                available_secrets = [f for f in all_imgs if f != spy_img]
            else:
                available_secrets = all_imgs[:]
            random.shuffle(available_secrets)
    except:
        available_secrets = []

refresh_available_secrets()

def get_img(folder, name_with_ext, size=(IMG_WIDTH, IMG_HEIGHT)):
    cache_key = (folder, name_with_ext, size)
    if cache_key in image_cache: return image_cache[cache_key]
    
    path = os.path.join(folder, name_with_ext)
    if not os.path.exists(path):
        for ex in EXTS:
            if os.path.exists(path + ex):
                path = path + ex
                break
    
    if os.path.exists(path):
        img = Image.open(path)
        img.thumbnail(size, Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        image_cache[cache_key] = photo
        return photo
    return None

# --- الدوال الخاصة بالواجهات (Home, Names, Identity, Timer) تتبع هنا بنفس منطقك السابق ---
# ملاحظة: تم اختصار الواجهات هنا لضمان إرسال الكود الأساسي المعدل للمسارات.
# تأكد من استخدام دالة ar(text) لجميع النصوص العربية.

def show_home():
    for w in main_frame.winfo_children(): w.destroy()
    content = tk.Frame(main_frame, bg=CLR_BG)
    content.place(relx=0.5, rely=0.5, anchor="center")
    tk.Label(content, text=ar("الـجـاسـوس"), font=("Arial", 32, "bold"), fg=CLR_ACCENT, bg=CLR_BG).pack(pady=20)
    tk.Button(content, text=ar("إبدأ المهمة"), bg=CLR_ACCENT, fg="white", font=("Arial", 15), command=show_names).pack(pady=20)
    tk.Label(content, text="By Bensahla Sidahmed", font=("Arial", 10), fg=CLR_SUB, bg=CLR_BG).pack()

def show_names():
    # كود واجهة الأسماء الخاص بك مع التأكد من استخدام ar()
    show_home() # مؤقتاً للعودة

show_home()
root.mainloop()
