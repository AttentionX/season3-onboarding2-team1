import base64
import os

from dotenv import load_dotenv

load_dotenv()

from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

system_message = "You are a helpful assistant"


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def encode_frame(frame):
    return base64.b64encode(frame).decode("utf-8")


def encode_images(image_paths, frames=False):
    if frames is True:
        return [
            f"data:image/jpeg;base64,{encode_frame(synthesized_frame)}"
            for synthesized_frame in image_paths
        ]
    return [
        f"data:image/jpeg;base64,{encode_image(image_path)}"
        for image_path in image_paths
    ]


def test_gpt():
    return chatgpt("What is the meaning of life?")


def chatgpt(query, model="gpt-4-1106-preview"):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": query,
            }
        ],
        model=model,
    )

    response = response.choices[0].message.content
    return response


def test_vision_api():
    client = OpenAI()

    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What’s in this image?"},
                    {
                        "type": "image_url",
                        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                    },
                ],
            }
        ],
        max_tokens=300,
    )

    return response.choices[0].message.content


def vision_api(images, prompt):
    content = [{"type": "text", "text": prompt}]
    for image in images:
        content.append({"type": "image_url", "image_url": image})
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": content,
            }
        ],
        max_tokens=1000,
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    # response = test_vision_api()
    response = test_gpt()
    print(response)
