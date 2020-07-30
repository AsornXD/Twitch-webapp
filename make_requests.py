import os
from twitch import TwitchClient

def get_follows(limit, user):
    limit = int(limit)
    client = TwitchClient(secrets.Client_ID)
    users = client.users.translate_usernames_to_ids([user])
    follow_list = []
    for user in users:
        for i in client.users.get_follows(user.id, limit):
            follow_list.append({'name': i.channel.name, 'date': i.created_at})
    return follow_list
