import os
import sys
import unittest
import json
import imghdr
from PIL import Image

sys.path.append(os.getcwd())
from Backend.Prediction_API.predict import get_prediction
from Backend.ELA_API.ela import convert_to_ela
from Backend.Cloud_Functions.resize import decode_base64, encode_base64, process, resize_image

class TestPrediction(unittest.TestCase):
    def test_prediction(self):
        """
        Test that a prediction has been made.
        This test is highly dependent on the model that has been produced.
        If the model changes, the result of this test may change.
        """
        img_path = os.getcwd() + '/Unit Tests/Assets/test_prediction.jpg'
        ela = convert_to_ela(img_path)
        prediction = get_prediction(ela)

        self.assertTrue((prediction != None) and (prediction != 0))

    def test_unable_predict(self):
        """
        Test that a prediction could not be made.
        This test is highly dependent on the model that has been produced.
        If the model changes, the result of this test may change.
        """
        img_path = os.getcwd() + '/Unit Tests/Assets/test_unpredictable.jpg'
        ela = convert_to_ela(img_path)
        prediction = get_prediction(ela)

        self.assertTrue((prediction != None) and (prediction == 0))


class TestEla(unittest.TestCase):
    def test_ela(self):
        """
        Test that an ela image as been produced.
        """
        img_path = os.getcwd() + '/Unit Tests/Assets/test_resize.jpg'
        ela = convert_to_ela(img_path)

        self.assertIn('ela', ela)


class TestResize(unittest.TestCase):

    def test_resize(self):
        """
        Test that resizing of an image has occurred.
        """
        img_path = os.getcwd() + '/Unit Tests/Assets/test_resize.jpg'
        img = Image.open(img_path)

        current_dimension = img.size

        resized = resize_image(img)
        self.assertIsNot(current_dimension, resized.size, msg=(
            {'Old Dimension': current_dimension, 'New Dimension': resized.size}))

    def test_landscape(self):
        """
        Test that a landscape image has NOT been rotated but has been resized.
        """
        img_path = os.getcwd() + '/Unit Tests/Assets/test_resize.jpg'
        img = Image.open(img_path)

        results = process(img)
        w, h = results.size
        self.assertIsNot(img.size, results.size)
        self.assertGreater(w, h)

    def test_portrait(self):
        """
        Test that a portrait image has been rotated and has been resized.
        """
        img_path = os.getcwd() + '/Unit Tests/Assets/test_rotate.jpg'
        img = Image.open(img_path)

        results = process(img)
        w, h = results.size
        self.assertIsNot(img.size, results.size)
        self.assertGreater(w, h)


class TestBase64(unittest.TestCase):
    def test_encoding(self):
        """
        Test that encoding has taken place.
        """
        img_path = os.getcwd() + '/Unit Tests/Assets/test_rotate.jpg'
        img = Image.open(img_path)

        result = encode_base64(img)
        self.assertEqual(type(result), bytes)

    def test_decoding(self):
        """
        Test that decoding has occurred.
        """

        with open(os.getcwd() + '/Unit Tests/Assets/base64.json', 'r') as base64:
            data = base64.read()

        base64_img = json.loads(data)

        result = decode_base64(str(base64_img['base64_img']))

        self.assertEqual(result.format, "PNG")


if __name__ == "__main__":

    unittest.main()
