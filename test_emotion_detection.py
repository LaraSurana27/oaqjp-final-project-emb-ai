"""Unit tests for the EmotionDetection package."""

import unittest
from unittest.mock import patch, MagicMock
import json
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test cases for the emotion_detector function."""

    def _mock_api_response(self, emotions, status_code=200):
        """Helper to create a mock API response."""
        mock_response = MagicMock()
        mock_response.status_code = status_code
        if status_code == 200:
            response_body = {
                "emotionPredictions": [
                    {
                        "emotion": emotions,
                        "target": "",
                        "emotionMentions": []
                    }
                ]
            }
            mock_response.text = json.dumps(response_body)
        else:
            mock_response.text = ""
        return mock_response

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_joy(self, mock_post):
        """Test that 'I am glad this happened' returns joy as dominant."""
        mock_post.return_value = self._mock_api_response({
            "anger": 0.006273,
            "disgust": 0.002115,
            "fear": 0.008966,
            "joy": 0.978154,
            "sadness": 0.049396
        })
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_anger(self, mock_post):
        """Test that 'I am really mad about this' returns anger."""
        mock_post.return_value = self._mock_api_response({
            "anger": 0.834149,
            "disgust": 0.023901,
            "fear": 0.016051,
            "joy": 0.003574,
            "sadness": 0.061903
        })
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_disgust(self, mock_post):
        """Test that 'I feel disgusted just hearing about this' returns disgust."""
        mock_post.return_value = self._mock_api_response({
            "anger": 0.014056,
            "disgust": 0.972192,
            "fear": 0.011498,
            "joy": 0.000485,
            "sadness": 0.051803
        })
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_sadness(self, mock_post):
        """Test that 'I am so sad about this' returns sadness."""
        mock_post.return_value = self._mock_api_response({
            "anger": 0.023462,
            "disgust": 0.004105,
            "fear": 0.058507,
            "joy": 0.001405,
            "sadness": 0.869462
        })
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_fear(self, mock_post):
        """Test that 'I am really afraid that this will happen' returns fear."""
        mock_post.return_value = self._mock_api_response({
            "anger": 0.007832,
            "disgust": 0.003469,
            "fear": 0.930755,
            "joy": 0.002051,
            "sadness": 0.093212
        })
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_blank_input_returns_none(self, mock_post):
        """Test that blank input (HTTP 400) returns None for all values."""
        mock_post.return_value = self._mock_api_response({}, status_code=400)
        result = emotion_detector("")
        self.assertIsNone(result['dominant_emotion'])
        self.assertIsNone(result['anger'])

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_return_format(self, mock_post):
        """Test that the return dictionary has all six required keys."""
        mock_post.return_value = self._mock_api_response({
            "anger": 0.1,
            "disgust": 0.2,
            "fear": 0.3,
            "joy": 0.05,
            "sadness": 0.35
        })
        result = emotion_detector("Test text")
        expected_keys = {
            'anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion'
        }
        self.assertEqual(set(result.keys()), expected_keys)
        self.assertEqual(result['dominant_emotion'], 'sadness')


if __name__ == '__main__':
    unittest.main()
