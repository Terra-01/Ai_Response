import os
from flask import Flask, render_template, request
import config
import thought
from dotenv import load_dotenv

def page_not_found(e):
    return render_template('apology.html'), 404


app = Flask(__name__)
app.config.from_object(config.config['development'])

app.register_error_handler(404, page_not_found)

def configure():
    load_dotenv()

@app.route('/', methods=["GET", "POST"])
def index():

    if request.method == 'POST':
        configure()
        prompt = request.form['topic']
        gen = thought.generate_thought(prompt)
        answer = gen.replace('\n', '')


    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)
