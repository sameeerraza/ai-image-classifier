import streamlit as st
import time
from PIL import Image
from app.model import load_model
from app.classify import classify_image
from app.style import apply_custom_css

def main():
    st.set_page_config(page_title="AI Image Classifier", page_icon="🎃", layout="centered")
    apply_custom_css()

    st.title("AI Image Classifier")
    st.markdown("### Upload an image and let **AI** guess what's inside 👇")

    @st.cache_resource
    def load_cached_model():
        return load_model()

    model = load_cached_model()
    uploaded_file = st.file_uploader("Drag and drop or browse image...", type=["jpg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", width="stretch")
        if st.button("Classify Image"):
            with st.spinner("Analyzing Image..."):
                image = Image.open(uploaded_file)
                start = time.time()
                predictions = classify_image(model, image)
                end = time.time()

                if predictions:
                    top_label, top_score = predictions[0][1], predictions[0][2]
                    st.success(f"Top Prediction: **{top_label}** ({top_score:.2%})")
                    st.info(f"Analysis completed in {end - start:.2f} seconds")

                    if top_score > 0.80:
                        st.balloons()

                    st.subheader("Predictions")
                    cols = st.columns(3)
                    for col, (_, label, score) in zip(cols, predictions):
                        col.metric(label=label, value=f"{score:.2%}")

if __name__ == "__main__":
    main()