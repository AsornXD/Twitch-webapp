from flask import Flask, render_template, request
import make_requests

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit")
def submit():
    user_limit = request.values.get("limit")
    user_user = request.values.get("user")
    results_follow_list = make_requests.get_follows(user_limit, user_user)
    return render_template("display_follows.html", user = user_user, limit = user_limit, followlist = results_follow_list)

app.config['TEMPLATED_AUTO_RELOAD'] = True
if __name__ == "__main__":
    app.run(host = "127.0.0.1", port = 5000, debug= True, use_reloader = False)
