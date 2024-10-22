import cv2
import numpy as np
from ultralytics import YOLO

### ********** ###
# Getting whites/yellows. Need to adjust the colour ranges for red and orange.
# Will try a different approach to get the colours.
### ********** ###

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
    Classifies the average colour into a colour category.
    """
    avg_colour_bgr = np.uint8([[avg_colour]])  # Convert to uint8 for OpenCV function
    avg_colour_hsv = cv2.cvtColor(avg_colour_bgr, cv2.COLOR_BGR2HSV)[0][0]

    # Extract the HSV values
    hue = avg_colour_hsv[0]
    saturation = avg_colour_hsv[1]
    value = avg_colour_hsv[2]

    # Define color ranges
    red_lower1, red_upper1 = np.array([0, 70, 50]), np.array([10, 255, 255]) # Red lower range
    red_lower2, red_upper2 = np.array([170, 70, 50]), np.array([180, 255, 255]) # Red upper range

    green_lower, green_upper = np.array([35, 150, 200]), np.array([85, 255, 255])  # Fluorescent green    
    blue_lower, blue_upper = np.array([90, 150, 200]), np.array([130, 255, 255])  # Fluorescent blue
    yellow_lower, yellow_upper = np.array([20, 150, 200]), np.array([35, 255, 255]) # Fluorescent yellow
    orange_lower, orange_upper = np.array([10, 100, 100]), np.array([25, 255, 255])
    
    # Classify colour
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


def process_image(model, filename):
    """
    Processes an image using the YOLO model and performs detection.
    """
    image = cv2.imread(filename)
    results = model(image)

    for result in results:
        for bbox in result.boxes:
            xyxy = bbox.xyxy[0].cpu().numpy() # Extract bounding box coordinates and convert to NumPy array
            x1, y1, x2, y2 = xyxy  # Unpack the bounding box coordinates
            
            label = model.names[int(bbox.cls[0])] # Get the label name from the model

            avg_colour = get_colour(image, (x1, y1, x2, y2))
            colour = classify_colour(avg_colour)
            colours = ['orange', 'red', 'white', 'green', 'blue', 'yellow']

            # Draw the bounding box and label
            if label == 'vest':
                if colour in colours:
                    cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                    cv2.putText(image, f'{colour}-{label}', (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
                else:
                    cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                    cv2.putText(image, f'{label}', (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
            
            elif label == 'helmet':
                if colour in colours:
                    cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                    cv2.putText(image, f'{colour}-{label}', (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
                else:
                    cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                    cv2.putText(image, f'{label}', (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
            
            else: # Other labels
                cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)
                cv2.putText(image, f'{label}', (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)




    # export the image
    # cv2.imwrite(f'output-images/{filename}.jpg', image)

def main():
    model = YOLO(model_file)

    # Load an image
    image_set = [images]

    for img in image_set:
        process_image(model, img)

    # cv2.imshow('Detection', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

if __name__ == '__main__':
    main()