import streamlit as st
from PIL import Image
from model import load_model, classify_image
from utils import preprocess_image

def main():
    st.set_page_config(page_title="AI Image Classifier", page_icon="🐱‍👤", layout="centered")

    st.title("AI Image Classifier")
    st.write("Upload an image and let AI tell you what is in it!")

    @st.cache_resource
    def load_cached_model():
        return load_model()

    model = load_cached_model()

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", width="stretch")

        col1, col2 = st.columns(2)
        classify_btn = col1.button("Classify Image")
        reset_btn = col2.button("Reset")

        if classify_btn:
            with st.spinner("Analyzing Image..."):
                image = Image.open(uploaded_file)
                try:
                    predictions = classify_image(model, image, preprocess_image)
                    st.subheader("Predictions")
                    for _, label, score in predictions:
                        st.write(f"**{label}**: {score:.2%}")
                        st.progress(int(score * 100))
                except RuntimeError as e:
                    st.error(str(e))

        if reset_btn:
            st.rerun()

if __name__ == "__main__":
    main()
