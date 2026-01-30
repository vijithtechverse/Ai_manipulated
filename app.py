import streamlit as st
from PIL import Image

from metadata import analyze_metadata
from ela import perform_ela
from noise import noise_variance
from decision import final_decision

st.title("🧠 AI Image Manipulation Detection")

uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Stage 1
    meta_flag, meta_reasons = analyze_metadata(image)

    # Stage 2
    ela_score, ela_img = perform_ela(image)

    # Stage 3
    noise_var = noise_analysis(image)

    # (Optional) Stage 4 – DL model
    model_pred = 1  # placeholder (0 = real, 1 = fake)

    # Final decision
    result, confidence = final_decision(
        meta_flag, ela_score, noise_var, model_pred
    )

    st.subheader("🔍 Analysis Results")
    st.write("Metadata Suspicious:", meta_flag)
    st.write("ELA Score:", ela_score)
    st.write("Noise Variance:", noise_var)
    st.write("Final Decision:", result)
    st.write("Confidence Score:", confidence)

    st.image(ela_img, caption="ELA Image")


