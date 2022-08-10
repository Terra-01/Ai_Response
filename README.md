# This is Ai Response
#### Video Demo:  <https://youtu.be/9rtJPLsuzI4>
#### Description:
This project uses the Open Ai API along with GPT-3 in the programming language of Python, Flask, HTML, Css and Jinja.
The structure of the project is fairely simple, as the basic structure of a web-application should be.

Let's look at the files in the root folder:-
The "app.py" file contains the code to use the functions so that the web server can be started along with the logic and api behind the project.
The "config.py" file is used to initialize the "app.py" file so everything would run smoothly.
The "requirements.txt" is the file which stores all the necessary components to get this applicatin up and running.
The "thought.py" file is where the magic happens, this file contacts the Open Ai's davinci engine along with the input that the application gets from the user, if no input is given then the Ai is smart enough to give back a reponse by itself.

Now, in the templates folder we have two html files "apology.html" and the "index.html", as the name suggests "apology.html" just returns error 404 which could happen in two scenarios (either the Open Ai returns back no value because of wrong api key OR the Open Ai server crashes), meanwhile the "index.html" consists of all the elements that are to be displayed to the user.

Lastly, in the static folder we have "bg.jpg" the background image that is displayed at the "index.html", the "favicon.ico" an icon which is displayed at the navigation bar near the title in the browser tab, and "styles.css" a Css file which is used for all the formatting and design in the html file.

Feel free to hit me up if you need anything.
This was Ai Respnse.

## Technology stacks and Api's Used:
> Open AI's api, GPT-3, Python, JavaScript, HTML, CSS, Jinja and Flask.

## FAQ's:-

##### What is GPT-3?
> GPT-3, or the third generation Generative Pre-trained Transformer, is a neural network machine learning model trained using internet data to generate any type of text. Developed by OpenAI, it requires a small amount of input text to generate large volumes of relevant and sophisticated machine-generated text.GPT-3's deep learning neural network is a model with over 175 billion machine learning parameters. To put things into scale, the largest trained language model before GPT-3 was Microsoft's Turing NLG model, which had 10 billion parameters. As of early 2021, GPT-3 is the largest neural network ever produced. As a result, GPT-3 is better than any prior model for producing text that is convincing enough to seem like a human could have written it.

##### What is Open AI?
> OpenAI is a tech company founded in December 2015 by partners including Elon Musk, known for his leadership of the Tesla electric car company and the SpaceX space exploration company. From headquarters in San Francisco, CA, OpenAI seeks to promote artificial intelligence through an open, cooperative model.

##### What is Flask?
> Flask is a web application framework written in Python. It was developed by Armin Ronacher, who led a team of international Python enthusiasts called Poocco. Flask is based on the Werkzeg WSGI toolkit and the Jinja2 template engine.Both are Pocco projects.

##### What is Jinja?
> Jinja is a fast, expressive, extensible templating engine. Special placeholders in the template allow writing code similar to Python syntax. Then the template is passed data to render the final document.
