# genai vs real street view of a random location

from gmicloud import Client
from gmicloud._internal._models import SubmitRequestRequest
import random
from openai import OpenAI
import webbrowser
import time

# random_gps
lat = random.uniform(-90, 90)
lon = random.uniform(-180, 180)

client = OpenAI(api_key=key)

p1 = "create a prompt to generate a video about this location: " + str(lat) + " " + str(lon)

resp = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "You are a geopolitical expert"},
        {"role": "user", "content": p1}
        ],
    model="gpt-4o")
p2 = resp.choices[0].message.content


client = Client(
    email=email,
    password=pswd
)

# models = client.video_manager.get_models()
# print(f"Available models: {[model.model for model in models]}")


request = SubmitRequestRequest(
    model="Kling-Text2Video-V2.1-Master",
    payload={
        "prompt": p2,
        "video_length": 3  # Duration in seconds
    }
)

response = client.video_manager.create_request(request)
print(f"Request submitted with ID: {response.request_id}")

request_id = response.request_id

request_detail = client.video_manager.get_request_detail(request_id)
request_detail.status
video_url = request_detail.dict()["outcome"]["video_url"]


#wait for 5 minutes
delay_in_seconds = 5 * 60

street_view_url = f"https://www.google.com/maps/@?api=1&map_action=pano&viewpoint={lat},{lon}"
webbrowser.open(street_view_url)
webbrowser.oepn(video_url)
