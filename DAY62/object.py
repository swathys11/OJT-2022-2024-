# Import the necessary libraries
import cv2
import matplotlib.pyplot as plt

# Load the pretrained Haar Cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load an image for testing
image = cv2.imread('face.jpg')

# Check if the image was loaded successfully
if image is None:
    raise ValueError("Image not found or unable to load.")

# Convert the image to grayscale
grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(grey_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

print(f"Number of faces detected: {len(faces)}")

# Draw rectangles around detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Convert BGR image to RGB for displaying with matplotlib
img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display the image with matplotlib
plt.imshow(img_rgb)
plt.axis('off')  # Hide axes
plt.show()