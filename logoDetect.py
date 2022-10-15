import requests
# If you are using a Jupyter Notebook, uncomment the following line.
# %matplotlib inline
import matplotlib.pyplot as plt
import json
from PIL import Image
from io import BytesIO

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
image_url = input("Gimme jpg url: ")

headers = {'Ocp-Apim-Subscription-Key': subscription_key}
params = {'visualFeatures': 'Adult'}
data = {'url': image_url}
response = requests.post(analyze_url, headers=headers,
                         params=params, json=data)

# headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type':'application/octet-stream'}
# with open('C:\\Users\\spike\\Documents\\Hackathons\\BigRedHacks\\gray-shirt-logo.jpg', 'rb') as f:
#     data = f.read()
# response = requests.post(analyze_url, headers=headers,
#                          params=params, data=data)


response.raise_for_status()

# The 'analysis' object contains various fields that describe the image. The most
# relevant caption for the image is obtained from the 'description' property.
analysis = response.json()
print(json.dumps(response.json()))
# image_caption = analysis["description"]["captions"][0]["text"].capitalize()

# Display the image and overlay it with the caption.
image = Image.open(BytesIO(requests.get(image_url).content))
plt.imshow(image)
plt.axis("off")
# _ = plt.title(size="x-large", y=-0.1)
plt.show()