[app]

# (str) Title of your application
title = Spy Game DZ

# (str) Package name
package.name = spygame

# (str) Package domain (needed for android packaging)
package.domain = org.bensahla

# (str) Application version (تمت إضافته لإصلاح الخطأ السابق)
version = 0.1

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,jpeg,ttf,json

# (list) Application requirements
requirements = python3,kivy,pillow

# (str) Custom source folders for requirements
# (list) Permissions
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) The orientation of the app (portrait, landscape or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (int) Android SDK version to use
android.sdk = 33

# (bool) If True, then automatically accept SDK license
android.accept_sdk_license = True

# (str) Android entry point
android.entrypoint = main.py

# (str) Architecture to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) allow backup
android.allow_backup = True

[buildozer]

# (int) Log level (2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = off)
# ضروري جداً لبيئة GitHub Actions
warn_on_root = 0
