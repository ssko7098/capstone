"""
This module processes video to extract the colour of vest & helmet detections. 
It uses a YOLO model for object detection and OpenCV for image processing.
"""

import cv2
import numpy as np
from ultralytics import YOLO


def get_colour(image, bbox):
    """
    Extract the average colour from a bounding box in an image.
    
    Args:
    image (ndarray): The input image.
    bbox (list): A list of coordinates defining the bounding box.
    
    Returns:
    ndarray: The average color in the bounding box in BGR format.
    """
    x1, y1, x2, y2 = map(int, bbox)
    roi = image[y1:y2, x1:x2]

    # Calculate the average color in the region (BGR format)
    avg_colour_per_row = np.average(roi, axis=0)
    avg_colour = np.average(avg_colour_per_row, axis=0)

    return avg_colour


def classify_colour(avg_colour):
    """
    Classify the colour based on its HSV values.
    
    Args:
    avg_colour (ndarray): The average BGR color values.
    
    Returns:
    str: The classified color as a string ('white', 'yellow', 'orange', 'red', 
          'green', 'blue') or None if it doesn't match any defined color.
    """
    avg_colour_bgr = np.uint8([[avg_colour]])  # Convert to uint8 for OpenCV function
    avg_colour_hsv = cv2.cvtColor(avg_colour_bgr, cv2.COLOR_BGR2HSV)[0][0]

    hue, saturation, value = avg_colour_hsv

    # Define color ranges
    red_lower1, red_upper1 = np.array([0, 55, 65]), np.array([10, 100, 100])
    red_lower2, red_upper2 = np.array([160, 150, 200]), np.array([180, 255, 255])
    green_lower, green_upper = np.array([35, 150, 200]), np.array([85, 255, 255])
    blue_lower, blue_upper = np.array([90, 150, 200]), np.array([130, 255, 255])
    yellow_lower, yellow_upper = np.array([20, 150, 200]), np.array([35, 255, 255])
    orange_lower, orange_upper = np.array([20, 150, 200]), np.array([24, 255, 255])

    if saturation <= 35 and value >= 120:
        return 'white'

    if yellow_lower[0] <= hue <= yellow_upper[0] and saturation >= 50 and value >= 50:
        return 'yellow'

    if orange_lower[0] <= hue <= orange_upper[0] and saturation >= 50 and value >= 50:
        return 'orange'

    if ((red_lower1[0] <= hue <= red_upper1[0]) or
        (red_lower2[0] <= hue <= red_upper2[0])) and saturation >= 50 and value >= 50:
        return 'red'

    if green_lower[0] <= hue <= green_upper[0] and saturation >= 50 and value >= 50:
        return 'green'

    if blue_lower[0] <= hue <= blue_upper[0] and saturation >= 50 and value >= 50:
        return 'blue'

    return None


def process_results(model, filename):
    """
    Process the detection results and annotate the image with bounding boxes.
    
    Args:
    model: The YOLO detection model.
    filename (str): The filename of the image to process.
    
    Returns:
    None: Annotates and displays the image.
    """
    image = cv2.imread(f'inference-images/{filename}.jpg')
    print(f'Shape: ', image.shape)

    # Perform detection
    results = model(image)

    # Iterate through detections
    for result in results:
        for bbox in result.boxes:
            # Extract bounding box coordinates and convert to NumPy array
            xyxy = bbox.xyxy[0].cpu().numpy()
            x1, y1, x2, y2 = xyxy  # Unpack the bounding box coordinates

            # Get the label name from the model
            label = model.names[int(bbox.cls[0])]

            avg_colour = get_colour(image, (x1, y1, x2, y2))
            colour = classify_colour(avg_colour)

            if label == 'vest':
                colours = ['orange', 'purple', 'white', 'yellow']

                if colour in colours:
                    cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                    cv2.putText(image, f'{colour}-{label}', (int(x1), int(y1) - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
                else:
                    cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                    cv2.putText(image, f'{label}', (int(x1), int(y1) - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)


            if label == 'helmet':
                colours = ['blue', 'red', 'white', 'green', 'orange']

                if colour in colours:
                    cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                    cv2.putText(image, f'{colour}-{label}', (int(x1), int(y1) - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
                else:
                    cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                    cv2.putText(image, f'{label}', (int(x1), int(y1) - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

            else:
                cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                cv2.putText(image, f'{label}', (int(x1), int(y1) - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

    # export the image
    cv2.imwrite(f'output-images/{filename}.jpg', image)

def main():
    """
    Main function to run the YOLOv8 model on a video file and process its frames.
    """
    model = YOLO(model_file)

    # Load an image
    image_set = [images]

    for img in image_set:
        process_results(model, img)

    # cv2.imshow('Detection', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
