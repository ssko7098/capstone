import unittest
from unittest.mock import patch, MagicMock
from train1 import load_model, train_model, validate_model, export_model

class TestYOLOFunctions(unittest.TestCase):

    @patch('ultralytics.YOLO')
    def test_load_model(self, mock_yolo):
        # Mock the YOLO model loading process
        mock_model = MagicMock()
        mock_yolo.return_value = mock_model

        # Call the function
        model = load_model()

        # Assert the model was loaded correctly
        mock_yolo.assert_called_with(model="yolov8n.pt")
        self.assertEqual(model, mock_model)

    @patch('ultralytics.YOLO')
    def test_train_model(self, mock_yolo):
        # Mock the YOLO model
        mock_model = MagicMock()
        
        # Call the function with mock model
        train_model(mock_model, data="model/test.yaml", epochs=100, imgsz=512, batch=8, save=True)

        # Assert training was called with the correct arguments
        mock_model.train.assert_called_with(data="model/test.yaml", epochs=100, imgsz=512, batch=8, save=True)

    @patch('ultralytics.YOLO')
    def test_validate_model(self, mock_yolo):
        # Mock the YOLO model
        mock_model = MagicMock()

        # Call the function with mock model
        validate_model(mock_model)

        # Assert validation was called
        mock_model.val.assert_called_once()

    @patch('ultralytics.YOLO')
    def test_export_model(self, mock_yolo):
        # Mock the YOLO model
        mock_model = MagicMock()

        # Call the function with mock model
        export_model(mock_model, format="onnx")

        # Assert export was called with the correct format
        mock_model.export.assert_called_with(format="onnx")

if __name__ == "__main__":
    unittest.main()
