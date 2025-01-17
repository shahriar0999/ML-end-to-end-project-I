import os
import torch
import sys
from fastapi.testclient import TestClient
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import src.aws_s3 as aws_s3
from transformers import pipeline
import torchvision
from transformers import AutoImageProcessor #-> like Tokenizer

# model_ckpt = "google/vit-base-patch16-224-in21k"
# model = "C:/Users/shahr/Music/Project ML/MLOps with FASTAPI/end-to-end-project/ml-models/human_pose_classification"
# image_processor = AutoImageProcessor.from_pretrained(model, use_fast=True)

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

############################### Download ML Models ###############################
force_download = False

# def download_model(model_name: str, modelType: str, force_download: bool):
#     if modelType == 'text':
#         local_path = 'ml-models/'+model_name
#         if not os.path.isdir(local_path) or force_download:
#             aws_s3.download_dir(local_path, model_name)
#         model = pipeline('text-classification', model=local_path, device=device)

model_name = "tinybert-sentiment-analysis"
local_path = 'ml-models/'+model_name
if not os.path.isdir(local_path) or force_download:
    aws_s3.download_dir(local_path, model_name)
sentiment_model = pipeline('text-classification', model=local_path, device=device)
print("**download sentiment model")

model_name = "tinybert-disaster-tweet"
local_path = 'ml-models/'+model_name
if not os.path.isdir(local_path) or force_download:
    aws_s3.download_dir(local_path, model_name)
disaster_model = pipeline('text-classification', model=local_path, device=device)
print('download disaster model**')

    # elif modelType == 'image':
    #     local_path = 'ml-models/'+model_name
    #     if not os.path.isdir(local_path) or force_download:
    #         aws_s3.download_dir(local_path, model_name)
    #     model = pipeline('image-classification', model=local_path, device=device, image_processor=image_processor)
    # # return the model
    # return model