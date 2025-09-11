from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2

def load_model():
    return MobileNetV2(weights="imagenet")