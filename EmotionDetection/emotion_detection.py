import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)

    formatted_response = json.loads(response.text)
    formatted_response = formatted_response["emotionPredictions"][0]

    anger = formatted_response['emotion']['anger']
    disgust = formatted_response['emotion']['disgust']
    fear = formatted_response['emotion']['fear']
    joy = formatted_response['emotion']['joy']
    sadness = formatted_response['emotion']['sadness']
    dominant_emotion = max(formatted_response['emotion'], key=formatted_response['emotion'].get)

    return {'anger': anger, 'disgust': disgust, 'fear': fear, 
            'joy': joy, 'sadness': sadness, 'dominant_emotion': dominant_emotion}

  