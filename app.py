import base64
from flask import Flask, render_template, request, redirect, url_for
from instagram_crawler.crawler import get_posts_by_user
import requests

from openai import OpenAI
client = OpenAI(
    api_key="YOUR_OPEN_AI_DEVELOPER_KEY"
)

app = Flask(__name__)

# encode an image URL to base 64
def get_as_base64(url):
    return base64.b64encode(requests.get(url).content).decode("utf-8")


@app.route("/", methods=("GET", "POST"))
def index():
    # render template
    if request.method != "POST":
        username = request.args.get("username")
        prompt = request.args.get("prompt")
        result = request.args.get("result")
        return render_template("index.html", username=username, prompt=prompt, result=result)
    
    # gather user input
    username = request.form["username"]
    prompt = request.form["prompt"]
    
    # scrape Instagram for the desired user
    instagram_posts = get_posts_by_user(username)
    captions = [x["caption"] for x in instagram_posts]
    img_urls = [x["img"] for x in instagram_posts]
    
    # build ChatGPT payload
    payload = {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": 
                    "I am providing some images and captions from Instagram for the user {username}. \
                    Please answer the following prompt using all the images and captions provided. \
                    Prompt: {prompt}".format(username=username, prompt=prompt)
            },
            {
                "type": "text",
                "text": "Captions (separated by the | character): {captions}".format(captions=" | ".join(captions))
            }
        ]
    }
    for img_url in img_urls:
        try:
            base64_image = get_as_base64(img_url)
            payload["content"].append(
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"
                    }
                },
            )
        except Exception:
            # print("Couldn't encode the following image url: " + img_url)
            continue
    
    # ask agent
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        max_tokens=300,
        messages=[payload]
    )
    return redirect(url_for(
            "index", 
            username=username, 
            prompt=prompt, 
            result=response.choices[0].message.content
        )
    )
