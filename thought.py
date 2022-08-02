import os
import openai
import config
from dotenv import load_dotenv

def configure():
    load_dotenv()

configure()
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_thought(prompt):
    response = openai.Completion.create(
      model="text-davinci-002",
      prompt="Generate thought for the day, from topic: {}.".format(prompt),
      temperature=0.7,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    return response['choices'][0]['text']

# to execute the above code but in commandline :-
# openai api completions.create -m text-davinci-002 -p "Generate thought for the day, from famous people" -t 0.7 -M 256 --stream
