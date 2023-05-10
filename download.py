import requests
import os

url = "https://www.kaggle.com/datasets/andrewmvd/cyberbullying-classification/download"

# create the ./data directory if it doesn't exist
if not os.path.exists("./data"):
    os.makedirs("./data")

# send an HTTP request to the provided URL and get the response
response = requests.get(url)

# save the response content to the ./data directory with a filename of "cyberbullying_classification.csv"
with open("./data/dataset.csv", "wb") as file:
    file.write(response.content)
