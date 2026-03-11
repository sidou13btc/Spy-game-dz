[app]
title = Spy Game DZ
package.name = spygame
package.domain = org.bensahla
source.dir = .
source.include_exts = py,png,jpg,kv,ttf,json
version = 1.0.0

# المتطلبات الأساسية للتشغيل
requirements = python3,kivy,pillow,arabic-reshaper,python-bidi

orientation = portrait
fullscreen = 1
android.archs = arm64-v8a, armeabi-v7a
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# إعدادات النظام
android.api = 31
android.minapi = 21
android.ndk = 25b
android.skip_update = False
android.copy_libs = 1

[buildozer]
log_level = 2
warn_on_root = 1
