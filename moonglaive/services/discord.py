from typing import List
import requests


class Channel:
    id: str
    name: str
    users: str
    messages: str


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
        messages = []
        base_url = f'https://discord.com/api/channels/{channel_id}/messages?limit=100'
        url = base_url
        while(True):
            response = requests.get(
                url,
                headers=headers
            )
            body = response.json()
            if(type(body) is list and len(body) > 0):
                messages += body
                before = body[-1]['id']
                url = f'{base_url}&before={before}'
            else:
                break;
        return messages

    def get_users_count_from_messages(self, messages: List[Message]) -> str:
        if type(messages) is list:
            users_list = list(map(
                lambda message: message['author']['username'] +
                message['author']['discriminator'], messages))
            counts = {user: users_list.count(user) for user in users_list}
            return str(len(counts))
        else:
            return ''
