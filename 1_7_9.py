class Video:

    def create(self, name):
        self.name = name

    def play(self):
        return f"воспроизведение видео {self.name}"

class YouTube:
    videos = []

    @classmethod
    def add_video(cls, video):
        cls.videos.append(video)

    @classmethod
    def play(cls, video_indx):
        return cls.videos[video_indx]

v1 = Video()
v2 = Video()
v1.create("Python")
v2.create("Python ООП")
YouTube.add_video(v1)
YouTube.add_video(v2)
for i in YouTube.videos:
    print(i.play())

