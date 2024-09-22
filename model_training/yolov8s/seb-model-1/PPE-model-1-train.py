import os
import torch
from ultralytics import YOLO

def main():

    model = YOLO("yolov8s.pt")

    if torch.cuda.is_available():
        device = [i for i in range(torch.cuda.device_count())]
    else:
        device = torch.device("cpu")

    print(f'Device: {device}')


    # Start training
    results = model.train(data="data.yaml",
                            epochs=100,
                            imgsz=1024,
                            batch=64,
                            device=device,
                            save=True,
                            cache=True,                    # Cache images for faster training
                            verbose=True,                  # Verbose output for training insights
                            )

    results = model.val()
    model.export()


if __name__ == "__main__":
    main()
