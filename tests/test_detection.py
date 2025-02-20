import unittest
from src.detection import FireSmokeDetector
import numpy as np

class TestFireSmokeDetector(unittest.TestCase):
    def setUp(self):
        self.model_path = 'path_to_your_model.pth'  # Update with your model path
        self.detector = FireSmokeDetector(self.model_path)
        
    def test_detect(self):
        # Example test case
        # Generate a dummy frame or use a test image
        frame = np.zeros((224, 224, 3), dtype=np.uint8)  # Black frame
        result = self.detector.detect(frame)
        self.assertIsInstance(result, float)
        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
