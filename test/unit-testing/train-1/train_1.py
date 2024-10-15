from ultralytics import YOLO
import torch
def load_model(model_name="yolov8n.pt"):
    """Loads the YOLO model with the given model name."""
    return YOLO(model=model_name)
def train_model(model, data="model/test.yaml", epochs=100, imgsz=512, batch=8, save=True):
    """Trains the YOLO model with the provided configuration."""
    model.train(data=data, epochs=epochs, imgsz=imgsz, batch=batch, save=save)
def validate_model(model):
    """Validates the YOLO model."""
    return model.val()
def export_model(model, format="onnx"):
    """Exports the YOLO model in the specified format."""
    return model.export(format=format)
def main():
    model = load_model()
    train_model(model)
    results = validate_model(model)
    success = export_model(model)
    return results, success
if __name__ == "__main__":
    main()