from flask import Flask, render_template, request
import make_requests

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit/followlist")
def submitfollow():
    user_limit = request.values.get("limit")
    user_user = request.values.get("user")
    print(user_user)
    results_follow_list = make_requests.get_follows(user_limit, user_user)
    return render_template("display_follows.html", user = user_user, limit = user_limit, followlist = results_follow_list)

@app.route("/submit/checksubscriber")
def submitsub():
    my_user = request.values.get("subuser")
    my_channel = request.values.get("channel")
    get_sub_result = make_requests.check_if_subscribed(my_user, my_channel)
    return render_template("displaysub.html", result = get_sub_result)

@app.route("/submit/topgames")
def submittop():
    limit2 = request.values.get("my_limit")
    get_top = make_requests.get_topgames(limit2)
    return render_template("displaytop.html", gamelist = get_top, this_limit = limit2)

@app.route("/submit/searchchannel")
def submitchannel():
    channel_query = request.values.get("my_channel_query")
    channel_limit = request.values.get("my_channel_limit")
    get_channels = make_requests.get_channels(channel_query, channel_limit)
    return render_template("display_channel.html", channellist = get_channels, this_channel_limit = channel_limit, this_channel_query = channel_query)

@app.route("/submit/leaguestats")
def submitlolstats():
    this_league_username = request.values.get("my_league_username")
    this_league_region = request.values.get("my_league_region")
    return render_template("display_league_stats.html", league_stats = make_requests.get_league_stats(this_league_username, this_league_region), league_username = this_league_username, league_region = this_league_region)

app.config['TEMPLATED_AUTO_RELOAD'] = True
if __name__ == "__main__":
    app.run(host = "127.0.0.1", port = 5000, debug= True, use_reloader = False)
