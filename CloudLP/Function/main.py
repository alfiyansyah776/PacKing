import logging
from operator import itemgetter
import os
import json

from flask import jsonify
from google.cloud import aiplatform
from google.protobuf import json_format
from google.protobuf.struct_pb2 import Value
import requests
import tensorflow as tf

import PIL
import numpy as np
from io import BytesIO


COLUMNS = ['bread', 'egg', 'fried-food', 'meat','noodles-pasta','rice', 'seafood','soup',
           'vegetable-fruit','asinan-jakarta','bika-ambon','donuts',
           'dumplings','gudeg','macaroni-and-cheese','pempek','rendang','sate','surabi','dairy-product']

aip_client = aiplatform.gapic.PredictionServiceClient(client_options={
    'api_endpoint': 'us-central1-aiplatform.googleapis.com'
})
aip_endpoint_name = f'projects/{os.environ["GCP_PROJECT"]}/locations/us-central1/endpoints/{os.environ["ENDPOINT_ID"]}'


def get_prediction(instance):
    logging.info('Sending prediction request to AI Platform ...')
    try:
        pb_instance = json_format.ParseDict(instance, Value())
        response = aip_client.predict(endpoint=aip_endpoint_name,
                                      instances=[pb_instance])
        return list(response.predictions[0])
    except Exception as err:
        logging.error(f'Prediction request failed: {type(err)}: {err}')
        return None


def preprocess_image(image_url):
    logging.info(f'Fetching image from URL: {image_url}')
    try:
        image_response = requests.get(image_url, stream=True)
        image_response.raise_for_status()
        assert image_response.headers.get('Content-Type') == 'image/jpeg'
        
    except (ConnectionError, requests.exceptions.RequestException,
            AssertionError):
        logging.error(f'Error fetching image from URL: {image_url}')
        return None

    logging.info('Decoding and preprocessing image ...')
    
    img = PIL.Image.open(BytesIO(image_response.content))
    img = img.resize((180,180))
    img = np.asarray(img, dtype= np.float32)
    img = img / 255
    img = img.reshape(180,180,3)
    
    return img.tolist()  # Make it JSON-serializable


def classify_image(request):
    # Set CORS headers for the preflight request
    if request.method == 'OPTIONS':
        # Allows POST requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }
        return ('', 204, headers)

    # Disallow non-POSTs
    if request.method != 'POST':
        return ('Not found', 404)

    # Set CORS headers for the main request
    headers = {'Access-Control-Allow-Origin': '*'}

    request_json = request.get_json(silent=True)
    if not request_json or not 'image_url' in request_json:
        return ('Invalid request', 400, headers)

    instance = preprocess_image(request_json['image_url'])
    if not instance:
        return ('Invalid request', 400, headers)

    raw_prediction = get_prediction(instance)
    if not raw_prediction:
        return ('Error getting prediction', 500, headers)

    probabilities = zip(COLUMNS, raw_prediction)
    sorted_probabilities = sorted(probabilities,key=itemgetter(1),reverse=True)[0]

    hasil = {}
    hasil["food"] = str(sorted_probabilities[0])

    kirim = json.dumps(hasil)
    
    return (kirim, 200, headers)