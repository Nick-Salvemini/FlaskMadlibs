from flask import Flask, render_template
import static.stories as stories
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chickens'
debug = DebugToolbarExtension(app)

@app.route('/')
def home():
    # questions = story.prompts
    # return render_template('home.html', prompts=questions)
    return story

@app.route('/story')
def story():
    return render_template('story.html')