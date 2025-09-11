import cv2
import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

def preprocess_image(image):
    img = np.array(image)
    img = cv2.resize(img, (224, 224))
    img = preprocess_input(img)
    img = np.expand_dims(img, axis=0)
    return img