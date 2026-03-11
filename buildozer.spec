[app]
title = Spy Game DZ
package.name = spygame
package.domain = org.bensahla

# السطر الذي حل مشكلة التوقف في الصورة الأخيرة
version = 0.1

source.dir = .
source.include_exts = py,png,jpg,jpeg,ttf,json

# تحديد الإصدارات بدقة يمنع تعارض الأدوات (STDERR)
requirements = python3,kivy==2.2.1,pillow,hostpython3

orientation = portrait
fullscreen = 1

android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.private_storage = True
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 0
