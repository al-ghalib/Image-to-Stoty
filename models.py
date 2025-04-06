from transformers import pipeline
from configure import call_hf_api


def img2text_local(image_path):
    model = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")
    result = model(image_path)
    caption = result[0]['generated_text'] if result else "No caption generated."
    return caption


def img2text(image_path):
    with open(image_path, "rb") as f:
        image_data = f.read()
    result = call_hf_api("Salesforce/blip-image-captioning-large", data=image_data)
    return result[0]["generated_text"] if isinstance(result, list) else result["generated_text"]


def generate_story(scenario, n=20):
    prompt = f"""
    You are a story teller.
    Write a short story based on the following scenario. 
    Limit the story to {n} words.
    
    Scenario: {scenario}
    Story:
    """

    result = call_hf_api("mistralai/Mixtral-8x7B-Instruct-v0.1", payload={"inputs": prompt})
    text = result[0]["generated_text"] if isinstance(result, list) else result["generated_text"]
    return text.split("Story:\n")[-1].strip()


def text_to_speech(text, output_path="audio.wav"):
    result = call_hf_api("espnet/kan-bayashi_ljspeech_vits", payload={"inputs": text}, is_binary=True)

    with open(output_path, "wb") as f:
        f.write(result)

    return output_path