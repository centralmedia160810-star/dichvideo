from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
from kivy.utils import platform
import os

if platform == "android":
    from android.permissions import request_permissions, Permission
    request_permissions([
        Permission.READ_EXTERNAL_STORAGE,
        Permission.WRITE_EXTERNAL_STORAGE
    ])

try:
    from googletrans import Translator
    from gtts import gTTS
    import moviepy.editor as mp
except ImportError:
    pass


class VideoDichApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=25, spacing=20)
        
        tieude = Label(text='📽️ VIDEO DỊCH LỒNG TIẾNG', font_size=24, bold=True, color=(0.2, 0.5, 0.8, 1))
        self.layout.add_widget(tieude)

        self.chon_btn = Button(text='📂 Chọn video cần xử lý', font_size=18, background_color=(0.2, 0.6, 0.9, 1), size_hint=(1, 0.15))
        self.chon_btn.bind(on_press=self.chon_video)
        self.layout.add_widget(self.chon_btn)

        self.mo_btn = Button(text='✨ Bật làm mờ nền', font_size=18, background_color=(0.6, 0.4, 0.9, 1), size_hint=(1, 0.15))
        self.mo_btn.bind(on_press=self.bat_lammo)
        self.layout.add_widget(self.mo_btn)
        self.lam_mo = False

        self.xuly_btn = Button(text='🚀 Bắt đầu tạo video', font_size=18, background_color=(0.1, 0.7, 0.3, 1), disabled=True, size_hint=(1, 0.15))
        self.xuly_btn.bind(on_press=self.xu_ly)
        self.layout.add_widget(self.xuly_btn)

        self.trangthai = Label(text='✅ Sẵn sàng sử dụng!', font_size=15, color=(0.3, 0.3, 0.3, 1))
        self.layout.add_widget(self.trangthai)

        return self.layout

    def chon_video(self, instance):
        self.trangthai.text = "⏳ Vui lòng chọn tệp video..."
        self.fc = FileChooserListView(filters=["*.mp4", "*.mkv", "*.avi"])
        self.fc.bind(on_submit=self.lay_video)
        self.layout.add_widget(self.fc)

    def lay_video(self, instance, selection, touch):
        self.video_path = selection[0]
        self.layout.remove_widget(self.fc)
        ten_file = os.path.basename(self.video_path)
        self.trangthai.text = f"✅ Đã chọn: {ten_file[:25]}..."
        self.xuly_btn.disabled = False

    def bat_lammo(self, instance):
        self.lam_mo = not self.lam_mo
        if self.lam_mo:
            self.mo_btn.text = "☑️ Đã bật làm mờ nền"
            self.mo_btn.background_color = (0.2, 0.8, 0.5, 1)
        else:
            self.mo_btn.text = "✨ Bật làm mờ nền"
            self.mo_btn.background_color = (0.6, 0.4, 0.9, 1)

    def xu_ly(self, instance):
        self.trangthai.text = "🔄 Đang xử lý, vui lòng chờ..."
        try:
            phude_goc = "Xin chào bạn! Đây là nội dung video được dịch tự động. Chúc bạn xem video vui vẻ!"
            
            dich = Translator()
            phude_dich = dich.translate(phude_goc, dest='vi').text

            giongdoc = gTTS(text=phude_dich, lang='vi', slow=False)
            giongdoc.save("giongdoc_temp.mp3")

            video = mp.VideoFileClip(self.video_path)
            video = video.resize((1920, 1080))
            
            if self.lam_mo:
                video = video.fx(mp.vfx.gaussian_blur, 6)

            amthanh = mp.AudioFileClip("giongdoc_temp.mp3")
            video_cuoi = video.set_audio(amthanh)

            luu_duongdan = "/storage/emulated/0/Download/VIDEO_DA_DICH_1080p.mp4"
            video_cuoi.write_videofile(luu_duongdan, fps=30, codec='libx264', audio_codec='aac')

            os.remove("giongdoc_temp.mp3")
            self.trangthai.text = f"✅ HOÀN TẤT! Đã lưu:\n📁 {luu_duongdan}"

        except Exception as e:
            self.trangthai.text = f"❌ Lỗi: {str(e)}"


if __name__ == "__main__":
    VideoDichApp().run()
      
