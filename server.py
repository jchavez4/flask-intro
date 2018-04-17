"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

INSULTS = ['stupid', 'muggle','smelly', 'gross', 'newb', 'lame-o', 'reptar']


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      Hi! This is the home page.
      <a href="/hello">Get a compliment!</a>
    </html>
    """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    compliment = ""
    for item in AWESOMENESS:
      compliment += '<option value = "{}">{}</option>\n'.format(item, item)

    insult = ""
    for item in INSULTS:
      insult += '<option value = "{}">{}</option>\n'.format(item, item)

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <br>
          Select a compliment:
          <select name = "greeting">
            {}
          <input type="submit" value="Submit">
        </form>          
      </body>
    </html>
    """.format(compliment)


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("greeting")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """.format(player=player, compliment=compliment)

@app.route('/insult')
def insult_person():
    player = request.args.get("person")




if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
