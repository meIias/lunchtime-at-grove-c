"""
app.py

- contains flask app startup logic + routes
"""

from flask import (
    Flask,
    jsonify,
    request,
    render_template
)

app = Flask(
    __name__,
    template_folder="./templates"
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
    - responds with the result being their matched user
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
        pass  # todo
    else:
        result = "missing required info (user, lunch or coffee)"

    return jsonify({
        "result": result
    })


if __name__ == "__main__":
    app.run()

