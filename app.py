"""
app.py

- contains flask app startup logic + routes
"""

import shelve
from contextlib import closing

from os import path

from flask import (
    Flask,
    jsonify,
    request,
    render_template
)

import lunchtime_matching

DATA_STORE_PATH = './lunchtime.db'

app = Flask(
    __name__,
    template_folder="./templates"
)

app_data_store = shelve.open(
    DATA_STORE_PATH,
    writeback=True
)


@app.route('/', methods=['GET'])
def main():
    """
    app entry point - renders welcome/login page
    """
    return render_template("index.html")


@app.route('/lunchtime', methods=['POST'])
def lunchtime():
    """
    route to handle users lunch/coffee choice
    - responds with the result being their matched user(s)
    - expected request body:
    {
        user: string,
        meetup_type: string
    }
    - expected response body:
    {
        result: string
    }
    """
    user = request.json.get('user', '')
    meetup_type = request.json.get('meetup_type', '')

    result = ""

    if user and meetup_type and meetup_type in ['lunch', 'coffee']:
        if meetup_type == 'coffee':
            matched_user = lunchtime_matching.find_coffeemate(app_data_store, user)
            if not matched_user:
                result = "You've matched with everyone, no more coffee for you :("
            else:
                result = "Get coffee with %s!" % matched_user
        else:
            matched_users = lunchtime_matching.find_lunchmates(app_data_store, user)
            if len(matched_users):
                result = "Grab lunch with %s!" % ', '.join(matched_users)
            else:
                result = "Not enough people to grab lunch with :("
    else:
        result = "missing required info (user, lunch or coffee)"

    return jsonify({
        "result": result
    })


if __name__ == "__main__":
    # initialize app data on first start
    lunchtime_matching.check_init_data_store(app_data_store)

    with closing(app_data_store):
        app.run()

