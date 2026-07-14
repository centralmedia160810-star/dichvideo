from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
from kivy.utils import platform
import os
import sys

# Cấp quyền trên Android
if platform == "android":
    from android.permissions import request_permissions, Permission
    from android.storage import primary_external_storage_path
    request_permissions([
        Permission.READ_MEDIA_VIDEO,
        Permission.READ_MEDIA_AUDIO,
        Permission.WRITE_EXTERNAL_STORAGE,
        Permission.INTERNET
    ])

try:
    from gtts import gTTS
    from moviepy.editor import VideoFileClip, AudioFileClip
    import numpy as np
except ImportError as e:
    print(f"Lỗi thư viện: {e}")
    pass

class VideoDichApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=25, spacing=20)
        
        tieude = Label(text="🎬 VIDEO DỊCH LỜI TIẾNG", font_size=24, bold=True)
        self.layout.add_widget(tieude)
        
        self.chon_btn = Button(text="📂 Chọn video cần xử lý", font_size=18)
        self.chon_btn.bind(on_press=self.chon_video)
        self.layout.add_widget(self.chon_btn)
        
        self.lam_btn = Button(text="🎞️ Bật làm mờ nền", font_size=18, background_color=(0.2, 0.6, 0.9, 1))
        self.lam_btn.disabled = True
        self.lam_no = False
        self.lam_btn.bind(on_press=self.bat_lam_no)
        self.layout.add_widget(self.lam_btn)
        
        self.xuly_btn = Button(text="🚀 Bắt đầu dịch video", font_size=18, background_color=(0.2, 0.8, 0.5, 1))
        self.xuly_btn.disabled = True
        self.xuly_btn.bind(on_press=self.xu_ly)
        self.layout.add_widget(self.xuly_btn)
        
        self.trangthai = Label(text="✅ Sẵn sàng sử dụng!", font_size=15)
        self.layout.add_widget(self.trangthai)
        
        return self.layout

    def chon_video(self, instance):
        self.trangthai.text = "⬇️ Vui lòng chọn tệp video..."
        self.fc = FileChooserListView(filters=["*.mp4", "*.mkv", "*.avi"])
        self.fc.bind(on_submit=self.lay_video)
        self.layout.add_widget(self.fc)
        self.chon_btn.disabled = True

    def lay_video(self, selection, touch):
        self.video_path = selection[0]
        self.layout.remove_widget(self.fc)
        ten_file = os.path.basename(self.video_path)
        self.trangthai.text = f"✅ Đã chọn: {ten_file[:25]}..."
        self.lam_btn.disabled = False
        self.xuly_btn.disabled = False
        self.chon_btn.disabled = False

    def bat_lam_no(self, instance):
        if not self.lam_no:
            self.lam_no = True
            self.lam_btn.text = "🎞️ Tắt làm mờ nền"
            self.lam_btn.background_color = (0.2, 0.8, 0.5, 1)
        else:
            self.lam_no = False
            self.lam_btn.text = "🎞️ Bật làm mờ nền"
            self.lam_btn.background_color = (0.2, 0.6, 0.9, 1)

    def xu_ly(self, instance):
        self.trangthai.text = "⏳ Đang xử lý, vui lòng chờ..."
        try:
            # Nội dung dịch ví dụ
            phude_goc = "Xin chào bạn! Đây là nội dung video được dịch tự động."
            dich = gTTS(text=phude_goc, lang='vi', slow=False)
            ten_am = "giong_dich.mp3"
            dich.save(ten_am)

            # Mở video & âm thanh
            video = VideoFileClip(self.video_path)
            am_thanh = AudioFileClip(ten_am)
            video = video.resize((1080, 1920) if video.size[0] < video.size[1] else (1920, 1080))

            # Làm mờ nếu bật
            if self.lam_no:
                from moviepy.video.fx.all import blur
                video = blur(video, 6)

            # Gắn âm thanh mới
            video_cuoi = video.set_audio(am_thanh)

            # Lưu tệp đúng đường dẫn Android
            if platform == "android":
                thu_muc = primary_external_storage_path()
                luu_duong = os.path.join(thu_muc, "Download", "VIDEO_DICH.mp4")
            else:
                luu_duong = "VIDEO_DICH.mp4"

            video_cuoi.write_videofile(luu_duong, fps=30, codec="libx264", audio_codec="aac")
            
            # Xóa tệp tạm
            os.remove(ten_am)
            self.trangthai.text = f"✅ HOÀN THÀNH! Đã lưu tại: {luu_duong}"

        except Exception as e:
            self.trangthai.text = f"❌ Lỗi: {str(e)}"
            print(f"Lỗi chi tiết: {e}")

if __name__ == "__main__":
    VideoDichApp().run()
        
