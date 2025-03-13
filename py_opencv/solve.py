import cv2
import numpy as np

# Load the input image and convert it to grayscale
img = cv2.imread('image1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply a Gaussian filter to reduce noise
gray = cv2.GaussianBlur(gray, (5, 5), 0)

# Compute the gradient magnitude and direction
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
gradient_mag = np.sqrt(sobel_x**2 + sobel_y**2)
gradient_dir = np.arctan2(sobel_y, sobel_x)

# Apply non-maximum suppression
gradient_mag = cv2.nonmaxSuppression(gradient_mag, 10)

# Apply threshold to gradient magnitude
thresh = 100
gradient_mag[gradient_mag < thresh] = 0

# Label connected components
labels = cv2.connectedComponents(gradient_mag)

# Filter out connected components smaller than threshold area
min_area = 1000
for label in labels:
    area = cv2.contourArea(label)
    if area < min_area:
        continue
    x, y, w, h = cv2.boundingRect(label)
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Draw bounding box around connected components
cv2.drawContours(img, labels, -1, (0, 255, 0), 2)

# Display the output image
cv2.imshow('Output', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
