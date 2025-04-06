# 🖼️📖 AI Image-to-Story Teller

A fun and creative Streamlit app that transforms images into short stories — and even narrates them! Upload an image, let the AI describe it, generate a story based on the scene, and listen to it as audio.

---

## 🚀 Features

- 🔍 Image captioning using Hugging Face models
- ✍️ Short story generation from the image description
- 🔊 Text-to-speech narration of the generated story
- 🖥️ Built with Streamlit for a smooth, interactive UI

---

## 📸 How It Works

1. **Upload an Image** (`.jpg`, `.jpeg`, `.png`)
2. **AI generates a caption** describing the image content.
3. **Story is created** based on the caption using a language model.
4. **Audio is generated** so you can listen to the story.

---

## 🧠 Models Used

- 🧾 **Image Captioning**: [`Salesforce/blip-image-captioning-large`](https://huggingface.co/Salesforce/blip-image-captioning-large)
- 📚 **Story Generation**: [`mistralai/Mixtral-8x7B-Instruct-v0.1`](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1)
- 🗣️ **Text-to-Speech**: [`espnet/kan-bayashi_ljspeech_vits`](https://huggingface.co/espnet/kan-bayashi_ljspeech_vits)

---

## 🛠️ Installation (for local development)

```bash
git clone https://github.com/al-ghalib/image-story.git
cd image-story
pip install -r requirements.txt

```

### 🔐 Add Hugging Face API Token

Create a `.env` file in the project root:

```
HUGGINGFACEHUB_API_TOKEN=your_token_here
```

---

## 🧪 Run the App Locally

```bash
streamlit run app.py
```

---


## 📁 Project Structure

```
.
├── app.py                 # Streamlit app entry point
├── models.py              # Core logic for captioning, story, and speech
├── configure.py           # Hugging Face API handling
├── requirements.txt       # Dependencies
├── .env                   # Local env (ignored in git)
├── .gitignore             # Ignoring secrets & unnecessary files
└── .streamlit/
    └── secrets.toml       # Cloud secrets (not committed)
```

---


## 💡 Future Ideas

- Support for multiple story tones (funny, dark, sci-fi)
- Voice customization
- Allow saving and sharing stories

---

Enjoy telling stories with your images! 🌟

