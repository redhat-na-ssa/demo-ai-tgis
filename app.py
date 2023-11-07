import os
import gradio as gr
from huggingface_hub import InferenceClient

url = os.getenv('INFERENCE_URL')
print(f'INFERENCE_URL = {url}')
client = InferenceClient(model=url)

def inference(message, history):
    partial_message = ""
    for token in client.text_generation(message, max_new_tokens=100, stream=True):
        partial_message += token
        yield partial_message

gr.ChatInterface(
    inference,
    chatbot=gr.Chatbot(height=300),
    textbox=gr.Textbox(placeholder="Chat with me!", container=False, scale=7),
    description="This is the demo for Gradio UI consuming TGI endpoint with a LLama-2 model.",
    title="Gradio 🤝 TGI",
    examples=["What is a fibonacci sequence?", "def fibonacci(n: int) -> int:\n", "class Circle():\n"],
    retry_btn="Retry",
    undo_btn="Undo",
    clear_btn="Clear",
).queue().launch(server_name='0.0.0.0', server_port=8080)