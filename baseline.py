import base64
import os

from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
client = OpenAI(api_key=os.environ.get('API_KEY'))

import openai_api as openai

# encode_images
# vision_api
# test_vision_api

image_dir = 'fridge/'
image_paths = os.listdir(image_dir)
image_paths = [image_dir + elem for elem in image_paths]
print(image_paths)

encoded_images = openai.encode_images(image_paths)

prompt = '''You are a professional chef. For the following image of a fridge, do two tasks: first, identify the ingredients,
and second, come up with five ideas of dishes that utilize these ingredients. Please respond with a list of identified ingredients, \\
a list of dishes, and a reason you chose each dish.'''

responses = []
for image in encoded_images:
    response = openai.vision_api(image, prompt)
    responses.append(response)

for elem in responses:
    print(elem)