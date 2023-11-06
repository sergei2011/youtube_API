from googleapiclient.discovery import build
import os

class Video:

    def __init__(self, channel_id: str, youtube = build('youtube', 'v3', developerKey=os.getenv('API_KEY_YOUTUBE'))) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""

        self.channel_id = channel_id
        self.youtube = youtube
        self.channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(self.channel)
        self.view_count = self.channel["items"][0]["statistics"]['viewCount']
        self.description = self.channel["items"][0]["snippet"]['description']
        self.subscriberCount = int(self.channel["items"][0]["statistics"]['subscriberCount'])
        self.url = f"https://www.youtube/channels/{self.channel_id}"



    def __str__(self):
        return f"{self.description})"


class PLVideo(Video):
    def __init__(self, channel_id: str, id_playlist: str):
        self.id_playlist = id_playlist
        super().__init__(channel_id)
