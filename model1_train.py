from ultralytics import YOLO
from torch.utils.data import Subset

# load a pretrained model (recommended for training)
model = YOLO('yolov8s.pt')

results = model.train(data="safety_rd_v1/data.yaml", 
                      epochs=3, 
                      imgsz=640)

# Validate the model
metrics = model.val()  # no arguments needed, dataset and settings remembered

# Predict with the model
results = model("safety_rd_v1/valid/images/00004_jpg.rf.c0a352e33af42bb0d917c24d539ddc9d.jpg")  # predict on an image
for result in results:
    print(result.boxes)
    result.show()  # display to screen

# Export the model
model.export()
