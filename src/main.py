import gradio as gr
import numpy as np

def flip(im):
    return np.array(im)

demo = gr.Interface(
    flip,
    gr.Image(sources="webcam", streaming=True),
    "image",
    live=True
)

demo.launch()