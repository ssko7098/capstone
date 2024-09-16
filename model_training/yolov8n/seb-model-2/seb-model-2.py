import torch
from ultralytics import YOLO

def main():

    model = YOLO("yolov8n.pt")

    if torch.cuda.is_available():
        device = torch.device("cuda:0")
    else:
        device = torch.device("cpu")

    model.to(device)

    # Start training
    results = model.train(data="data.yaml",
                            epochs=3,
                            imgsz=1024,
                            batch=-1,
                            device=device)

    results = model("test.jpg")  # predict on an image
    for result in results:
        result.show()  # display to screen


if __name__ == "__main__":
    main()
