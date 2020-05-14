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

INSULT = ['shit', 'stupid', 'dumb']


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    	<html>
    		Hi! This is the home page.
    		<br>
    		<a href="/hello-greet">Click here if you want a compliment</a>
    		<a href="/hello-insult">Click here if you want a insult</a>
    	</html>
    """


@app.route('/hello-insult')
def say_diss():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/diss">
          <div>
          	What's your name? <input type="text" name="person">
          </div>
          <div>
	          Select your diss options:
	            <select name="insult">
	    			<option value="shit">shit</option>
	   				<option value="stupid">stupid</option>
	    			<option value="dumb">dumb</option>
	  			</select>
	  		</div>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/hello-greet')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          <div>
          	What's your name? <input type="text" name="person">
          </div>
          <div>
	          Select your greeting options:
	            <select name="greeting">
	    			<option value="awesome">awesome</option>
	   				<option value="terrific">terrific</option>
	    			<option value="fantastic">fantastic</option>
	    			<option value="neato">neato</option>
	    			<option value="fantabulous">fantabulous</option>
	    			<option value="wowza">wowza</option>
	    			<option value="oh-so-not-meh">oh-so-not-meh</option>
	    			<option value="brilliant">brilliant</option>
	    			<option value="ducky">ducky</option>
	    			<option value="coolio">coolio</option>
	    			<option value="incredible">incredible</option>
	    			<option value="wonderful">wonderful</option>
	    			<option value="smashing">smashing</option> 
	    			<option value="lovely">lovely</option>    				    			
	  			</select>
	  		</div>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("greeting")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """


@app.route('/diss')
def diss_person():
    """Get user by name."""

    player = request.args.get("person")
    insult = request.args.get("insult")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A diss</title>
      </head>
      <body>
        Hi, {player}! I think you're {insult}!
      </body>
    </html>
    """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
