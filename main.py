import requests
import datetime as dt
USERNAME = "eddypham"
TOKEN= "oameraghvserjg"

pixela_endpoint = "https://pixe.la/v1/users"
user_params={
    "token": os.environ['TOKEN'],
    "username": "eddypham",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
GRAPHID ="graph1"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params={
    "id":"graph1",
    "name":"Programming Hours",
    "unit":"Hours",
    "type":"int",
    "color":"ichou"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint,json=graph_params, headers=headers)
# print(response.text)

pixel_creation_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"
today = dt.datetime.now()
request_body={
    "date":today.strftime("%Y%m%d"),
    "quantity":input(str("How many hours did you code today? "))
}

response = requests.post(url=pixel_creation_endpoint,json=request_body,headers=headers)
print(response.text)
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today.strftime('%Y%m%d')}"
put_request_params={
    "quantity":"5"
}
# response = requests.put(url=update_endpoint,json=put_request_params,headers=headers)
# # print(response.text)

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_pixel_endpoint,headers=headers)
# print(response.text)
