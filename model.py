from tensorflow.keras.applications.mobilenet_v2 import (MobileNetV2, preprocess_input, decode_predictions)

def load_model():
    model = MobileNetV2(weights="imagenet")
    return model

def classify_image(model, image, preprocess_image):
    try:
        processed_image = preprocess_image(image)
        predictions = model.predict(processed_image)
        decoded_predictions = decode_predictions(predictions, top=3)[0]
        del predictions
        return decoded_predictions
    except Exception as e:
        raise RuntimeError(f"Error classifying image: {str(e)}")
