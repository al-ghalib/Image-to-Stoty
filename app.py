import streamlit as st
import tempfile
from models import img2text, generate_story, text_to_speech
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def tell_story(image_path, word_limit):
    scenario = img2text(image_path)
    story = generate_story(scenario, n=word_limit)
    audio_path = text_to_speech(story)
    return scenario, story, audio_path

def main():
    st.set_page_config(page_title="AI Image to Story", layout="centered")
    st.title("🖼️📖 Image to Story Teller")
    st.write("Upload an image, and the AI will generate a short story and read it out loud!")

    uploaded_file = st.file_uploader("Upload a JPG image", type=["jpg", "jpeg", "png"])
    
    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
        word_limit = st.selectbox("Story Word Limit", [10, 20, 30, 40, 50])

        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_image:
            temp_image.write(uploaded_file.getvalue())
            temp_image_path = temp_image.name

        with st.spinner("Generating story and audio..."):
            try:
                scenario, story, audio_path = tell_story(temp_image_path, word_limit)
            except Exception as e:
                st.error(f"Something went wrong: {e}")
                return

        st.success("Done!")

        with st.expander("📷 Scenario Detected"):
            st.write(scenario)

        with st.expander("📚 Generated Story"):
            st.write(story)

        st.audio(audio_path)

if __name__ == "__main__":
    main()
