import unittest
import joblib

class PredictionTest(unittest.TestCase):

    def setUp(self):
        self.pipeline = joblib.load('./model/model_pipeline.joblib')

    def test_prediction(self):
        new_data = [[2000, 7, 3, 2.00, 1150]]
        predicted_price = self.pipeline.predict(new_data)

        expected_price = 447808893
        self.assertAlmostEqual(predicted_price[0], expected_price, places=2)

