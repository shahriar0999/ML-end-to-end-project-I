import pytest
import sys
import os
from fastapi.testclient import TestClient
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.models import NLPDataInput
from main import app


client = TestClient(app)

def test_classify_disaster():
    data = NLPDataInput(text=["This is a test disaster tweet"], user_id="shahriar@gmail.com")
    response = client.post("/disaster_classifier", json=data.dict())
    assert response.status_code == 200
    assert "label" in response.json()[0]

def test_classify_sentiment():
    data = NLPDataInput(text=["I love you but you hate me"], user_id="shahriar@gmail.com")
    response = client.post("/sentiment_analysis", json=data.dict())
    assert response.status_code == 200
    assert "label" in response.json()[0]


# def test_classify_pose():
#     data = ImageDataInput(url=["https://media.istockphoto.com/id/1213229711/photo/young-indian-man-in-glasses-drink-coffee-sitting-on-the-stairs-in-the-street.jpg?s=1024x1024&w=is&k=20&c=YA6C5dNS60b4lR_0UioUQFBWtcpiiiHOsU1ZRV7YmEM="], user_id="shahriar@gmail.com")
#     # Convert the data to a dictionary and ensure the URL is a string
#     data_dict = data.dict()
#     data_dict['url'] = [str(url) for url in data_dict['url']]
#     response = client.post("/pose_classifier", json=data_dict)
#     assert response.status_code == 200
#     assert "label" in response.json()[0]


test_classify_sentiment()
test_classify_disaster()
# test_classify_pose()
