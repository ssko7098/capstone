"""
This script runs inference on a video using a YOLO model and saves the annotated output.
"""

from ultralytics import YOLO
import cv2

# Choose the model you want to run inference on
model = YOLO('best.pt')

VIDEO_PATH = 'test.mp4'
cap = cv2.VideoCapture(VIDEO_PATH)  # pylint: disable=no-member

# Define video codec and create VideoWriter object
OUTPUT_VIDEO_PATH = 'out.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # pylint: disable=no-member
fps = cap.get(cv2.CAP_PROP_FPS)  # pylint: disable=no-member
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # pylint: disable=no-member
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # pylint: disable=no-member
out = cv2.VideoWriter(OUTPUT_VIDEO_PATH, fourcc, fps, (width, height))  # pylint: disable=no-member

# Process each frame of the video
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run inference using the model
    results = model(frame)

    # Annotate the frame with detection results from the model
    annotated_frame = results[0].plot()

    # Write the final frame with annotations to the output video
    out.write(annotated_frame)

    # Optional: Display the frame during processing
    cv2.imshow('YOLOv8 Inference', annotated_frame)

    # Press 'q' to exit the video display
    if cv2.waitKey(1) & 0xFF == ord('q'):  # pylint: disable=no-member
        break

# Release the video capture, video writer, and close any OpenCV windows
cap.release()
out.release()
cv2.destroyAllWindows()  # pylint: disable=no-member
