import os
import torch
from ultralytics import YOLO
import wandb
from wandb.integration.ultralytics import add_wandb_callback

def main():
    
    # Initialize a Weights & Biases run
    wandb.init(project="SOFT3888 Capstone", job_type="training")

    model = YOLO("yolov8m.pt")

    # Add W&B Callback for Ultralytics
    add_wandb_callback(model, enable_model_checkpointing=True)

    if torch.cuda.is_available():
        device = [i for i in range(torch.cuda.device_count())]
    else:
        device = torch.device("cpu")

    print(f'Device: {device}')


    # Start training
    model.train(data="data.yaml",
                epochs=100,
                imgsz=1024,
                batch=48,
                device=device,
                save=True,
                cache=True,                    
                verbose=True,                  
                )

    model.val()

    # Finalize the W&B Run
    wandb.finish()

    model.export()


if __name__ == "__main__":
    main()
