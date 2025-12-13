import gradio as gr
from query_engine import ask


def chat(question):
    """
    Handles user input from the UI and forwards the query
    to the backend query engine.
    """
    return ask(question)


# Define the Gradio UI layout
with gr.Blocks() as demo:

    # Application title
    gr.Markdown(
        "<h1 style='text-align:center; font-size:36px;'>AI Chip Datasheet Assistant</h1>"
    )

    # Application description
    gr.Markdown(
        "<p style='text-align:center; font-size:16px;'>Ask questions about your chip datasheets</p>"
    )

    # Input and output layout
    with gr.Row():
        with gr.Column(scale=1):
            question = gr.Textbox(
                label="Question",
                placeholder="e.g. What is the supply voltage range of LM358?",
                lines=3
            )

        with gr.Column(scale=1):
            output = gr.Textbox(
                label="Output",
                lines=8
            )

    # Action buttons
    with gr.Row():
        clear = gr.Button("Clear", size="lg")
        submit = gr.Button("Submit", variant="primary", size="lg")

    # Button actions
    submit.click(chat, inputs=question, outputs=output)
    clear.click(lambda: ("", ""), outputs=[question, output])


# Launch the application
demo.launch(
    theme=gr.themes.Soft(),
    css="""
    textarea, input { font-size: 16px !important; }
    label { font-size: 18px !important; }
    """
)
