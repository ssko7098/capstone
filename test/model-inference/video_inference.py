from ultralytics import YOLO
import matplotlib.pyplot as plt
import cv2

## choose the model you want to run inference on
model = YOLO('best.pt')

video_path = 'test.mp4'
cap = cv2.VideoCapture(video_path)

# Define video codec and create VideoWriter object
output_video_path = 'out.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

# Process each frame of the video
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run inference using the first model
    results = model(frame)

    # Annotate the frame with detection results from the first model
    annotated_frame = results[0].plot()

    # Write the final frame with both models' annotations to the output video
    out.write(annotated_frame)

    # Optional: Display the frame during processing
    cv2.imshow('YOLOv8 Multiple Models Inference', annotated_frame)

    # Press 'q' to exit the video display
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture, video writer, and close any OpenCV windows
cap.release()
out.release()
cv2.destroyAllWindows()