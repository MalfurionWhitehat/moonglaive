from typing import List
import requests


class Channel:
    id: str
    name: str
    users: int


class User:
    id: str
    username: str
    discriminator: int


class Message:
    id: str
    author: User


class Discord():
    def __init__(self, authorization: str):
        self.authorization = authorization

    def get_channels(self, guild_id: str) -> Channel:
        headers = {
            'authorization': self.authorization
        }
        response = requests.get(
            f'https://discord.com/api/guilds/{guild_id}/channels',
            headers=headers
        )
        body = response.json()
        return body

    def get_messages(self, channel_id: str) -> List[Message]:
        headers = {
            'authorization': self.authorization
        }
        response = requests.get(
            f'https://discord.com/api/channels/{channel_id}/messages?limit=100',
            headers=headers
        )
        body = response.json()
        return body

    def get_users_count_from_messages(self, channel_id: str) -> str:
        messages = self.get_messages(channel_id)
        if type(messages) is list:
            users_list = list(map(
                lambda message: message['author']['username'] +
                message['author']['discriminator'], messages))
            counts = {user: users_list.count(user) for user in users_list}
            return str(len(counts))
        else:
            return ''
