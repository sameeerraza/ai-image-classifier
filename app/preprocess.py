import numpy as np
from PIL import Image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

def preprocess_image(image):
    # If image is already a PIL Image, use it directly
    if not isinstance(image, Image.Image):
        image = Image.fromarray(image)
    
    # Resize using PIL
    img = image.resize((224, 224))
    
    # Convert to numpy array
    img = np.array(img)
    
    # Preprocess for MobileNetV2
    img = preprocess_input(img)
    img = np.expand_dims(img, axis=0)
    
    return img
