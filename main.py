import os
import time
import warnings
warnings.filterwarnings('ignore')
import uvicorn
from fastapi import FastAPI
from fastapi import Request
from src.models import NLPDataInput, project
from src.download_load_model import sentiment_model, disaster_model
import requests
from PIL import Image
from io import BytesIO

# force_download = False

# sentiment_model = download_model(model_name = , modelType='text', force_download=force_download)
# twitter_model = download_model(model_name="tinybert-disaster-tweet", modelType='text', force_download=force_download)
# image_model = download_model(model_name="human_pose_classification", modelType='image', force_download=force_download)



app = FastAPI()


@app.get("/")
def home():
    return {'message': project}


@app.post("/sentiment_analysis")
def sentiment_analysis(data: NLPDataInput):
    output = sentiment_model(data.text)
    return output


@app.post("/disaster_classifier")
def classify_disaster(data: NLPDataInput):
    output = disaster_model(data.text)
    return output

# from IPython.display import display


# @app.post("/pose_classifier")
# def classify_pose(data: ImageDataInput):
#     try:
#         url = str(data.url[0])
#         response = requests.get(url)
#         if response.status_code == 200:
#             image = Image.open(BytesIO(response.content))
#             output = image_model(image)
#         return output
#     except Exception as e:
#         output = {'error': str(e)}


if __name__=="__main__":
    # uvicorn.run(app="main:app", port=8502, reload=True, host="0.0.0.0")
    uvicorn.run(app="main:app", port=8502, reload=True, host="0.0.0.0")

