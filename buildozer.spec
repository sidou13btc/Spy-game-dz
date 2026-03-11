[app]
# (str) Title of your application
title = Spy Game DZ

# (str) Package name
package.name = spygame

# (str) Package domain (needed for android packaging)
package.domain = org.bensahla

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,ttf,json

# (list) Application requirements
# تأكد من إضافة pillow لمعالجة الصور
requirements = python3,kivy,pillow,arabic-reshaper,python-bidi

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Android API to use
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) skip update of the setup.py
android.skip_update = False

# (bool) use the old build system
android.copy_libs = 1

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = off, 1 = on)
warn_on_root = 1
