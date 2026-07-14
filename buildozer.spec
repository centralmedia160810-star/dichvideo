[app]
title = Video Dịch Lời Tiếng
package.name = videodich
package.domain = org.videodich
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,otf,mp4,mkv,avi,srt
source.ignore_dirs = .git,.github,__pycache__,buildozer,tam_thoi
version = 1.0

requirements = python3,kivy==2.2.1,pillow==10.2.0,numpy==1.26.4,opencv-python-headless==4.9.0.80,moviepy==1.0.3,pydub==0.25.1,gTTS==2.5.1,requests==2.31.0
android.python_version = 3.10
android.api = 33
android.ndk = 25b
android.sdk = 24
android.optimize = 0
android.buildtools = 33.0.2
android.accepts_license = True  # ✅ DÒNG QUAN TRỌNG NHẤT

android.permissions = INTERNET,READ_MEDIA_VIDEO,READ_MEDIA_AUDIO,WRITE_EXTERNAL_STORAGE,FOREGROUND_SERVICE
android.arch = arm64-v8a,armeabi-v7a

orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 0
android.allow_backup = True
