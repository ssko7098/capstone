import os
import glob
from ultralytics import YOLO
import torch

def main():
    # Check if CUDA (GPU) is available, otherwise use CPU
    if torch.cuda.is_available():
        device = 'cuda' 
    else:
        device = 'cpu'
    print(f"Device: {device}")

    print("Training images directory contents:")
    print(os.listdir('/data/fmg_data/train'))

    print("Validation images directory contents:")
    print(os.listdir('/data/fmg_data/val'))

    # *** Load Model ***
    model = YOLO("yolov8l.pt")
    

    # *** Training Configuration ***
    epochs = 100
    imgsz = 640
    data = "data.yaml"
    # device = [0,1] # If u need more devices add more integers to the list


    # *** Train Model ***
    model.train(data=data, epochs=epochs, imgsz=imgsz, resume=False)
    
    results = model.val()
    success = model.export(format="onnx")

if __name__ == "__main__":
    main()