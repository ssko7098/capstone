from ultralytics import YOLO
import torch

def main():
    model = YOLO(model="yolov8n.pt")
    model.train(data="model/test.yaml", epochs=100, imgsz=512, batch=8, save=True)
    results = model.val()
    success = model.export(format="onnx")

if __name__ == "__main__":
    main()