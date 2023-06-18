import gradio as gr


def load_mesh(mesh_file_name):
    return mesh_file_name


demo = gr.Interface(
    fn=load_mesh,
    inputs=gr.Model3D(),
    outputs=gr.Model3D(
            clear_color=[0.0, 0.0, 0.0, 0.0],  label="3D Model"),
    allow_flagging="never"
)

if __name__ == "__main__":
    demo.launch(share=True)