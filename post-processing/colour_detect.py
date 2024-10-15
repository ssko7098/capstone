import cv2
import numpy as np
from ultralytics import YOLO

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

    hue = avg_colour_hsv[0]
    saturation = avg_colour_hsv[1]
    value = avg_colour_hsv[2]

    print(f"HSV Values: {avg_colour_hsv}")  # Debugging output

    red_lower = np.array([136, 87, 111], np.uint8) 
    red_upper = np.array([180, 255, 255], np.uint8) 
  
    # Set range for green color and  
    # define mask 
    green_lower = np.array([25, 52, 72], np.uint8) 
    green_upper = np.array([102, 255, 255], np.uint8) 
 
    # Set range for blue color and 
    # define mask 
    blue_lower = np.array([94, 80, 2], np.uint8) 
    blue_upper = np.array([120, 255, 255], np.uint8) 

    # now see if the average colour falls in the range of any of the colours

    if (hue >= red_lower[0] and hue <= red_upper[0]) or (hue >= 0 and hue <= 10):
        return 'red'
    elif hue >= green_lower[0] and hue <= green_upper[0]:
        return 'green'
    elif hue >= blue_lower[0] and hue <= blue_upper[0]:
        return 'blue'


def process_image(model, filename):
    image = cv2.imread(filename)

    # Perform detection
    results = model(image)

    # Iterate through detections
    for result in results:
        for bbox in result.boxes:
            # Extract bounding box coordinates and convert to NumPy array
            xyxy = bbox.xyxy[0].cpu().numpy()
            x1, y1, x2, y2 = xyxy  # Unpack bounding box coordinates
            
            # Get the label name from the model
            label = model.names[int(bbox.cls[0])]

            avg_colour = get_colour(image, (x1, y1, x2, y2))
            colour = classify_colour(avg_colour)

            if label == 'vest':
                colour_range = ['orange', 'purple', 'white', 'yellow']
                
                if colour in colour_range:
                    cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                    cv2.putText(image, f'{colour}-{label}', (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
                else: # Not in colour range
                    cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                    cv2.putText(image, f'{label}', (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)


            if label == 'helmet':
                colour_range = ['blue', 'red', 'white', 'green', 'orange']
            
                if colour in colour_range:
                    cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                    cv2.putText(image, f'{colour}-{label}', (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
                else: # Not in colour range
                    cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                    cv2.putText(image, f'{label}', (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
            
            else: # Classes that are not helmet or vest, label them as they are
                cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                cv2.putText(image, f'{label}', (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)



    # export the image
    # cv2.imwrite(f'output-images/{filename}.jpg', image)

def main():
    model = YOLO(model_file)

    # Load an image
    image_set = ['image1', 'image2', 'image3', 'image4', 'image5', 'image6', 'image7']

    for img in image_set:
        process_image(model, img)

    # cv2.imshow('Detection', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

if __name__ == '__main__':
    main()