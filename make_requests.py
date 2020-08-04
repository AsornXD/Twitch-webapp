import os
from twitch import TwitchClient

def get_follows(limit, user):
    limit = int(limit)
    client = TwitchClient(os.environ['CLIENT_ID'])
    users = client.users.translate_usernames_to_ids([user])
    follow_list = []
    for user in users:
        for i in client.users.get_follows(user.id, limit):
            follow_list.append({'name': i.channel.name, 'date': i.created_at})
    return follow_list
def check_if_subscribed(user, channel):
    client = TwitchClient(os.environ['CLIENT_ID'])
    idarray = client.users.translate_usernames_to_ids([user])
    print (idarray)
    check = client.check_subscribed_to_channel(idarray[0], 44322889)
    print(check)
    if (check):
        return user, "is subscirbed to", channel

    else:
        return user, "is not subscirbed to", client.channels.get_by_id(44322889).name

def get_topgames(templimit):
    client = TwitchClient(os.environ['CLIENT_ID'])
    return client.games.get_top(int(templimit))

def get_channels(search_query, search_limit):
    client = TwitchClient(os.environ['CLIENT_ID'])
    return client.search.channels(search_query, limit = int(search_limit))
