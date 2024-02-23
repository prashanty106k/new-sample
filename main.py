from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from pytube import YouTube
import os

class YouTubeDownloader(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10)
        
        self.url_input = TextInput(hint_text="Enter YouTube URL", multiline=False)
        layout.add_widget(self.url_input)

        self.download_mp3_button = Button(text="Download MP3", on_press=self.download_mp3)
        layout.add_widget(self.download_mp3_button)

        self.download_mp4_button = Button(text="Download MP4", on_press=self.download_mp4)
        layout.add_widget(self.download_mp4_button)

        self.result_label = Label(text="")
        layout.add_widget(self.result_label)

        return layout

    def download_mp3(self, instance):
        url = self.url_input.text
        try:
            yt = YouTube(url)
            video = yt.streams.filter(only_audio=True).first()
            out_file = video.download()
            base, ext = os.path.splitext(out_file)
            new_file = base + ".mp3"
            os.rename(out_file, new_file)
            self.result_label.text = "Successfully Downloaded as MP3"
        except Exception as e:
            self.result_label.text = f"Error: {str(e)}"

    def download_mp4(self, instance):
        url = self.url_input.text
        try:
            yt = YouTube(url)
            video = yt.streams.get_highest_resolution()
            out_file = video.download()
            self.result_label.text = "Successfully Downloaded as MP4"
        except Exception as e:
            self.result_label.text = f"Error: {str(e)}"

if __name__ == '__main__':
    YouTubeDownloader().run()
