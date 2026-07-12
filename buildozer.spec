[app]
title = Video Dịch Lồng Tiếng
package.name = videodich
package.domain = org.video.dich
source.dir = .
version = 0.1

# Dùng phiên bản Kivy ổn định, tương thích cao nhất
requirements = python3, kivy==2.2.1, googletrans==4.0.0-rc1, gTTS, moviepy, ffmpeg

android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
android.api = 33
android.archs = arm64-v8a
# Thêm cấu hình tối ưu đồ họa
android.minapi = 21
android.ndk_api = 21

orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 0
android.accept_sdk_license = True
android.sdk_license_agreement = yes
# Giảm cảnh báo biên dịch
android.cflags = -Wno-error

