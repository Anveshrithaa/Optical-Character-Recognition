import json
import os
import sys
import requests
import time
# If you are using a Jupyter notebook, uncomment the following line.
# %matplotlib inline
# import matplotlib.pyplot as plt
# from matplotlib.patches import Polygon
# from PIL import Image
from io import BytesIO

missing_env = False
# Add your Computer Vision subscription key and endpoint to your environment variables.
# if 'COMPUTER_VISION_ENDPOINT' in os.environ:
endpoint = "https://handwriting-ocr-tarp.cognitiveservices.azure.com/"
# else:
#     print("From Azure Cognitive Service, retrieve your endpoint and subscription key.")
#     print("\nSet the COMPUTER_VISION_ENDPOINT environment variable, such as \"https://westus2.api.cognitive.microsoft.com\".\n")
#     missing_env = True

# if 'COMPUTER_VISION_SUBSCRIPTION_KEY' in os.environ:
subscription_key = "ce44d595f42c4d32a20f13daeab14129"
# else:
#     print("From Azure Cognitive Service, retrieve your endpoint and subscription key.")
#     print("\nSet the COMPUTER_VISION_SUBSCRIPTION_KEY environment variable, such as \"1234567890abcdef1234567890abcdef\".\n")
#     missing_env = True

if missing_env:
    print("**Restart your shell or IDE for changes to take effect.**")
    sys.exit()

text_recognition_url = endpoint + "/vision/v3.0/read/analyze"

# Set image_url to the URL of an image that you want to recognize.
image_url = "https://1drv.ms/u/s!AhyXQNzqtIZrjWBUg1cYsv-c2VeU?e=Cc8MrX"

headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}
# data = {'url': image_url}
image_path=r'D:\VIT\Fall Semester 2020-21\TARP\Project'+r'\Prescription.jpeg'
image_data = open(image_path, "rb").read()
response = requests.post(
    text_recognition_url, headers=headers, data=image_data)
response.raise_for_status()

# Extracting text requires two API calls: One call to submit the
# image for processing, the other to retrieve the text found in the image.

# Holds the URI used to retrieve the recognized text.
operation_url = response.headers["Operation-Location"]

# The recognized text isn't immediately available, so poll to wait for completion.
analysis = {}
jsonval = {}
poll = True
while (poll):
    response_final = requests.get(
        response.headers["Operation-Location"], headers=headers)
    jsonval = response_final.json()
    
    print(json.dumps(jsonval, indent=4))
    time.sleep(1)
    if ("analyzeResult" in jsonval):
        poll = False
    if ("status" in jsonval and jsonval['status'] == 'failed'):
        poll = False
# polygons = []
if ("analyzeResult" in jsonval):
    allvals=[]
    for val in jsonval["analyzeResult"]["readResults"][0]["lines"]:
        text = val['text'].split()
        for word in text:
            if(word.isalnum()):
                allvals.append(word.lower())
    # print(allvals)
    import difflib
    mr = difflib.SequenceMatcher()
    ratios = []
    meds = ["rantac","crocin"]
    print("Medicines Needed By User:",meds)
    final_meds = []
    for medicine in meds:
        final_meds.extend(medicine.split())
    # print(final_meds)
        # med = ["rantac","crocin","digene"]
    for meds in allvals:
        for check_med in final_meds:
            seq = difflib.SequenceMatcher(None,meds,check_med)
            d = seq.ratio()*100
            ratios.append([meds,check_med,d])
    # print(ratios)
    allow=[]
    for ratio in ratios:
        if(ratio[2]>60 and ratio[0].isalpha()):
            allow.append(ratio[1])
    print("Medicines Approved:",allow)