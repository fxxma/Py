import requests

TOKEN = "dipshit7870"
USER_ID = "felixmaudem"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USER_ID}/graphs"
post_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

user_params = {
    "token": TOKEN,
    "username": USER_ID,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
graph_params = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
pixel_params = {
    "date": "20240603",
    "quantity": "10",
}
headers = {
    "X-USER-TOKEN": TOKEN
}
res = requests.post(url=post_pixel_endpoint, json=pixel_params, headers=headers)
print(res.text)
