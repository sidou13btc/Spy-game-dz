[app]

# (str) Title of your application
title = Spy Game DZ

# (str) Package name
package.name = spygame

# (str) Package domain (needed for android packaging)
package.domain = org.bensahla

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let's include all common extensions)
source.include_exts = py,png,jpg,jpeg,ttf,json

# (list) Application requirements
# تأكدنا من إضافة pillow للتعامل مع الصور و kivy للواجهة
requirements = python3,kivy,pillow

# (str) Custom source folders for requirements
# (list) Permissions
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (str) The orientation of the app (portrait, landscape or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) List of service to declare
# (list) Permissions

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK directory (if empty, it will be downloaded)
# (str) Android SDK directory (if empty, it will be downloaded)

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess download.
android.skip_update = False

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only.
android.accept_sdk_license = True

# (str) Android entry point, default is ok for Kivy-based app
android.entrypoint = main.py

# (str) Architecture to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (bool) allow backup
android.allow_backup = True

# (int) format version for the spec file
config.version = 1

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = off, 1 = on)
# مهم جداً لـ GitHub Actions
warn_on_root = 0

