import os
import torch
from ultralytics import YOLO
import wandb
from wandb.integration.ultralytics import add_wandb_callback

def main():
    
    # Initialize a Weights & Biases run
    wandb.init(project="SOFT3888 Capstone", job_type="training")

    model = YOLO("Seb_best_person.pt")

    # Add W&B Callback for Ultralytics
    add_wandb_callback(model, enable_model_checkpointing=True)

    if torch.cuda.is_available():
        device = [i for i in range(torch.cuda.device_count())]
    else:
        device = torch.device("cpu")


    # Start training
    model.train(data="data_roboflow_2.yaml",
                epochs=30,
                imgsz=640,
                batch=64,
                device=device,
                name='PPE_TEST_',
                save=True,
                cache=True,
                freeze=[i for i in range(5)],
                pretrained=True,
                lr0=0.0001
                )

    model.val()

    # Finalize the W&B Run
    wandb.finish()

    model.export()


if __name__ == "__main__":
    main()
