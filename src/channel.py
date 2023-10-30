import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""


    def __init__(self, channel_id: str, youtube = build('youtube', 'v3', developerKey=os.getenv('API_KEY_YOUTUBE'))) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""

        self.__channel_id = channel_id
        self.youtube = youtube
        self.channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.title = self.channel["items"][0]["snippet"]['title']
        self.view_count = self.channel["items"][0]["statistics"]['viewCount']
        self.description = self.channel["items"][0]["snippet"]['description']
        self.video_count = self.channel["items"][0]["statistics"]['videoCount']
        self.subscriberCount = int(self.channel["items"][0]["statistics"]['subscriberCount'])
        self.url = f"https://www.youtube/channels/{self.__channel_id}"


    def __str__(self):
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        return self.subscriberCount + other.subscriberCount

    def __sub__(self, other):
        return self.subscriberCount - other.subscriberCount

    def __lt__(self, other):
        return self.subscriberCount < other.subscriberCount

    def __le__(self, other):
        return self.subscriberCount <= other.subscriberCount

    def __gt__(self, other):
        return self.subscriberCount > other.subscriberCount

    def __ge__(self, other):
        return self.subscriberCount >= other.subscriberCount


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""


        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        youtube = build('youtube', 'v3', developerKey=os.getenv('API_KEY_YOUTUBE'))
        return youtube


    def to_json(self, w_file):
        json_data = {
            '__channel_id': self.__channel_id,
            'title': self.title,
            'descrition': self.description,
            'url': self.url,
            'subscriber_count': self.subscriberCount,
            'videoCount': self.video_count,
            'viewCount': self.view_count
        }
        with open(w_file, 'w') as f:
            f.write(json.dumps(json_data, ensure_ascii=False, indent=4))



