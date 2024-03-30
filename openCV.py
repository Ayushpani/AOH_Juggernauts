import cv2
import numpy as np

# Parameters
min_contour_area = 5000  # Minimum contour area to consider as a person
entry_line_position = 300  # Position of the entry line (y-coordinate)
exit_line_position = 700   # Position of the exit line (y-coordinate)
max_disappeared = 50       # Maximum number of consecutive frames a centroid can be marked as disappeared

# Initialize variables
entry_count = 0
exit_count = 0
persons_inside = 0
centroids = []
disappeared = {}

# Capture video from webcam or video file
cap = cv2.VideoCapture(0)  # Use 0 for webcam, or provide the path to the video file

# Background subtraction
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Apply background subtraction
    fgmask = fgbg.apply(frame)
    
    # Remove noise
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    
    # Find contours
    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw entry and exit lines
    cv2.line(frame, (0, entry_line_position), (frame.shape[1], entry_line_position), (0, 255, 0), 2)
    cv2.line(frame, (0, exit_line_position), (frame.shape[1], exit_line_position), (0, 0, 255), 2)
    
    # Update centroids
    new_centroids = []
    for contour in contours:
        # Filter contours based on area
        if cv2.contourArea(contour) > min_contour_area:
            x, y, w, h = cv2.boundingRect(contour)
            cx = x + w // 2
            cy = y + h // 2
            new_centroids.append((cx, cy))
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    # Match centroids
    if len(centroids) == 0:
        for centroid in new_centroids:
            centroids.append(centroid)
            disappeared[centroid] = 0
    else:
        for centroid in centroids:
            min_dist = float('inf')
            match = None
            for new_centroid in new_centroids:
                dist = np.linalg.norm(np.array(centroid) - np.array(new_centroid))
                if dist < min_dist:
                    min_dist = dist
                    match = new_centroid
            if match is not None:
                centroids[centroids.index(centroid)] = match
                disappeared[match] = 0
                new_centroids.remove(match)
            else:
                disappeared[centroid] += 1
                if disappeared[centroid] > max_disappeared:
                    centroids.remove(centroid)
                    disappeared.pop(centroid)
    
    # Count entry and exit
    for centroid in centroids:
        cx, cy = centroid
        if cy > entry_line_position and (cx, cy) not in disappeared:
            entry_count += 1
            persons_inside += 1
            print(entry_count)
        elif cy < exit_line_position and (cx, cy) not in disappeared:
            exit_count += 1
            persons_inside -= 1
            print(exit_count)
        disappeared[(cx, cy)] = 0
    
    # Display counts
    cv2.putText(frame, "Entry: {}".format(entry_count), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, "Exit: {}".format(exit_count), (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.putText(frame, "Inside: {}".format(persons_inside), (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    
    # Display frame
    cv2.imshow('Frame', frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
