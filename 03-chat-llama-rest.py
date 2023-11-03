import gradio as gr
from huggingface_hub import InferenceClient

client = InferenceClient(model="https://tgis-tgi.apps.ocp.sandbox2000.opentlc.com")

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
    examples=["What is a fibonacci sequence?", "def fibonacci(n: int) -> int:", "class Circle():"],
    retry_btn="Retry",
    undo_btn="Undo",
    clear_btn="Clear",
).queue().launch()