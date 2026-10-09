# A sample application of using openAI client
# Creating frontend using gradio to summarize a website using the scraper and summarizer modules

import gradio as gr

from summarizer import summarize

gr.Interface(
	fn=summarize,
	inputs=gr.Textbox(label="Website URL"),
	outputs=gr.Markdown(label="Summary"),
	title="AI Website Summarizer",
	description="Enter a website URL to get a concise summary of its content."
).launch(share=True)