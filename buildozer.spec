[app]
title = Video Dịch Lồng Tiếng
package.name = videodich
package.domain = org.video.dich
source.dir = .
version = 0.1

requirements = python3, kivy==2.3.0, googletrans==4.0.0-rc1, gTTS, moviepy

android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
android.api = 33
android.ndk = 25b
android.sdk = 24
android.arch = arm64-v8a

orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 0
android.accept_sdk_license = True
android.sdk = 24
android.ndk = 25b
android.api = 33
android.arch = arm64-v8a
