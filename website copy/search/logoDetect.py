import requests
# If you are using a Jupyter Notebook, uncomment the following line.
# %matplotlib inline
import matplotlib.pyplot as plt
import json
from PIL import Image
from io import BytesIO
import os
from pathlib import Path


def predict(image_url):
    # Add your Computer Vision subscription key and endpoint to your environment variables.
    # if 'COMPUTER_VISION_SUBSCRIPTION_KEY' in os.environ:
    #     subscription_key = os.environ['COMPUTER_VISION_SUBSCRIPTION_KEY']
    # else:
    #     print("\nSet the COMPUTER_VISION_SUBSCRIPTION_KEY environment variable.\n**Restart your shell or IDE for changes to take effect.**")
    #     sys.exit()

    # if 'COMPUTER_VISION_ENDPOINT' in os.environ:
    #     endpoint = os.environ['COMPUTER_VISION_ENDPOINT']

    subscription_key = '138925f0920e4218a33dece2f8763e61'
    endpoint = 'https://bigredhackslogodetection.cognitiveservices.azure.com/'

    analyze_url = endpoint + "vision/v3.1/analyze"

    # Set image_url to the URL of an image that you want to analyze.
    # image_url = input("Gimme jpg url: ")

    headers = {'Ocp-Apim-Subscription-Key': subscription_key}
    params = {'visualFeatures': 'Brands'}
    # data = {'url': image_url}
    # response = requests.post(analyze_url, headers=headers,
    #                         params=params, json=data)

    headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type':'application/octet-stream'}

    BASE_DIR = str(Path(__file__).resolve().parent.parent)

    image_url = image_url.replace('/', '\\')


    # print('\n',BASE_DIR,'\n')

    # print('\n',image_url,'\n')

    with open(BASE_DIR+image_url, 'rb') as f:
        data = f.read()
    response = requests.post(analyze_url, headers=headers,
                             params=params, data=data)


    response.raise_for_status()

    # The 'analysis' object contains various fields that describe the image. The most
    # relevant caption for the image is obtained from the 'description' property.
    analysis = response.json()
    print('ANALYSIS:\n',analysis,'\n')
    try:
        return analysis["brands"][0]['name']
    except:
        print('no brands')
        return None