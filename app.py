from flask import Flask, render_template, request
from stories import Story, story
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chickens'
debug = DebugToolbarExtension(app)

@app.route('/')
def home():
    questions = story.prompts
    return render_template('home.html', prompts=questions)

@app.route('/story')
def complete_story():
    template = story.generate(request.args)
    return render_template('story.html', template=template)