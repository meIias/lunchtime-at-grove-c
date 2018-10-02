"""
app.py

- contains flask app startup logic + routes
"""

from flask import (
    Flask,
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


if __name__ == "__main__":
    app.run()

