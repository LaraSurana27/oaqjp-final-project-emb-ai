"""
Emotion Detection module using Watson NLP EmotionPredict API.

This module provides a function to analyze text and detect emotions
(anger, disgust, fear, joy, sadness) using the IBM Watson NLP service.
"""

import json
import requests


def emotion_detector(text_to_analyse):
    """
    Analyze the given text and detect emotions using the Watson NLP API.

    Args:
        text_to_analyse (str): The text to analyze for emotions.

    Returns:
        dict: A dictionary containing scores for anger, disgust, fear,
              joy, sadness, and the dominant_emotion. Returns None values
              for all keys if the API returns a 400 status code.
    """
    url = (
        'https://sn-watson-emotion.labs.skills.network/'
        'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    headers = {
        "grpc-metadata-mm-model-id":
            "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    response = requests.post(
        url, json=input_json, headers=headers, timeout=10
    )

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    response_dict = json.loads(response.text)

    emotions = (
        response_dict.get('emotionPredictions',
                          response_dict.get('emotion_predictions',
                                            [{}]))[0].get('emotion', {})
    )

    anger_score = emotions.get('anger', 0)
    disgust_score = emotions.get('disgust', 0)
    fear_score = emotions.get('fear', 0)
    joy_score = emotions.get('joy', 0)
    sadness_score = emotions.get('sadness', 0)

    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    emotion_scores['dominant_emotion'] = dominant_emotion

    return emotion_scores
