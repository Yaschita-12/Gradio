import gradio as gr
gr.close_all()


def getDetails(name, age, preference, hobbies):
  return f"Name:{name}\nAge:{age}\nSubject Preference:{preference}\n Hobbies: {[ h for h in hobbies}] "

demo = gr.Interface(
    fn=getDetails,
    inputs = [gr.Textbox(label="Name: "),
        gr.Slider(label="Age: "),
        gr.Radio(label="Subject Preference: ", choices=[]),
        gr.Checkboxgroup(label='Hobbies:', choices=[])
    ],
    outputs=[gr.Textbox()]
)
demo.launch()
