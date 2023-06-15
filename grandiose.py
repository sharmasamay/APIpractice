#importing all the necessary libraries
import os
import openai
import gradio as gr
#api-key
openai.api_key = "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"
#function that returns job description
def jobdesc(Role,Experience,Industry):
  response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write up a concise job description in bullet points of a "+Role+" with about "+Experience+" years of experience working in the "+Industry+" industry.",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
  )
  #stores the text returned by the json object
  result = response["choices"][0]["text"]
  return result;

#creates a gradio object
demo = gr.Interface(fn=jobdesc, inputs=["text","text","text"], outputs="text")
demo.launch(share=True)  
