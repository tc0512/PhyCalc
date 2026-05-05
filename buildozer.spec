[app]
title = PhyCalc
package.name = phycalc
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttc
version = 0.1
requirements = python3,kivy
icon.filename = %(source.dir)s/logo.png

[android]
api = 34
minapi = 21
ndk = 23b
android.accept_sdk_license = True
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
