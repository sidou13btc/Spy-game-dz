%%writefile buildozer.spec
[app]
title = Spy Game
package.name = spy_game
package.domain = dz.bensahla
source.dir = .
source.include_exts = py,png,jpg,jpeg,ttf,json
version = 1.0.0

# المكتبات الضرورية
requirements = python3,kivy,pillow,arabic-reshaper,python-bidi

orientation = portrait
fullscreen = 1
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
android.archs = armeabi-v7a, arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
