import cv2
import numpy as np
from ultralytics import YOLO

"""
This script incorporates video inference and post-processing to detect and classify objects in a video.
"""

def get_colour(image, bbox):
    """
    Extracts the average colour from a bounding box in an image.
    """
    x1, y1, x2, y2 = map(int, bbox)
    roi = image[y1:y2, x1:x2]
    
    # Calculate the average color in the region (BGR format)
    avg_colour_per_row = np.average(roi, axis=0)
    avg_colour = np.average(avg_colour_per_row, axis=0)
    
    return avg_colour

def classify_colour(avg_colour):
    """
    Classifies the average colour of an object into a colour category.
    """
    avg_colour_bgr = np.uint8([[avg_colour]])
    avg_colour_hsv = cv2.cvtColor(avg_colour_bgr, cv2.COLOR_BGR2HSV)[0][0]

    # Extract HSV values
    hue = avg_colour_hsv[0]
    saturation = avg_colour_hsv[1]
    value = avg_colour_hsv[2]

    # Define color ranges
    red_lower1, red_upper1 = np.array([0, 55, 65]), np.array([10, 100, 100])
    red_lower2, red_upper2 = np.array([160, 150, 200]), np.array([180, 255, 255])
    green_lower, green_upper = np.array([35, 150, 200]), np.array([85, 255, 255])
    blue_lower, blue_upper = np.array([90, 150, 200]), np.array([130, 255, 255])
    yellow_lower, yellow_upper = np.array([20, 150, 100]), np.array([35, 255, 255])
    orange_lower, orange_upper = np.array([20, 150, 200]), np.array([24, 255, 255])  # TODO: Update orange range.

    # Classify the colour based on the HSV values
    if saturation <= 35 and value >= 120:
        return 'white'

    if yellow_lower[0] <= hue <= yellow_upper[0] and saturation >= 50 and value >= 50:
        return 'yellow'
    
    if orange_lower[0] <= hue <= orange_upper[0] and saturation >= 50 and value >= 50:
        return 'orange'

    if ((red_lower1[0] <= hue <= red_upper1[0]) or (red_lower2[0] <= hue <= red_upper2[0])) and saturation >= 50 and value >= 50:
        return 'red'

    if green_lower[0] <= hue <= green_upper[0] and saturation >= 50 and value >= 50:
        return 'green'

    if blue_lower[0] <= hue <= blue_upper[0] and saturation >= 50 and value >= 50:
        return 'blue'
    
    return



def process_results(model, results, frame):
    """
    Gets frame from video and processes it using the YOLO model.
    """
    for result in results:
        for bbox in result.boxes:
            xyxy = bbox.xyxy[0].cpu().numpy() # Bounding box coordinates
            x1, y1, x2, y2 = xyxy 
            
            # Get the label name from the model
            label = model.names[int(bbox.cls[0])]

            avg_colour = get_colour(frame, (x1, y1, x2, y2))
            colour = classify_colour(avg_colour)
            
            if label.lower() == 'goggles':
                continue

            if label.lower() == 'vest':
                colours = ['orange', 'purple', 'white', 'yellow']
                if colour in colours:
                    cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                    cv2.putText(frame, f'{colour}-{label}', (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
                else:
                    cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                    cv2.putText(frame, f'{label}', (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

            elif label.lower() == 'helmet':
                colours = ['blue', 'red', 'white', 'green', 'orange', 'yellow']
                if colour in colours:
                    cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                    cv2.putText(frame, f'{colour}-{label}', (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
                else:
                    cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                    cv2.putText(frame, f'{label}', (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
            
            elif label.lower() == ('person' or 'boots'):
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 1)
                cv2.putText(frame, f'{label}', (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 1)

    return frame


def main():
    model = YOLO(f'{model_name}.pt')

    video_path = f'{video_name}.mp4'
    cap = cv2.VideoCapture(video_path)

    # Define video codec and create VideoWriter object
    output_video_path = f'/{video_export_path}'
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
        results = model(frame)
        annotated_frame = process_results(model, results, frame)
        # Write the final frame with both models' annotations to the output video
        out.write(annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture, video writer, and close any OpenCV windows
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

