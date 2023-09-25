import gradio as gr
from utils.text_image_utils import TextImage

text_image = TextImage()

def get_index(evt: gr.SelectData):
    text_image.cur_index = evt.index + 1


def apply_image_text_generation(localizer):
    with gr.Tab(label=localizer("Midjourney")):
        with gr.Row():
            with gr.Column(scale=3):
                images_upload = gr.File(label=localizer("上传图片"),file_count="single",file_types=['.png','.jpeg'])
                # images = gr.Gallery(label=localizer("图片"),columns=4)
                prompt = gr.Textbox(label=localizer("提示词"))
                with gr.Accordion(label=''):
                    # upload_btn = gr.Button(localizer("上传"))
                    generate_btn = gr.Button(localizer("生成"), variant='primary')
            with gr.Column(scale=2):
                channel_id = gr.Textbox(label=localizer("Channel ID"))
                authorization = gr.Textbox(label=localizer("Authorization"))
                application_id = gr.Textbox(label=localizer("Application ID"))
                guild_id = gr.Textbox(label=localizer("Guild ID"))
                session_id = gr.Textbox(label=localizer("Session ID"))
                version = gr.Textbox(label=localizer("Version"))
                id = gr.Textbox(label=localizer("ID"))
                flags = gr.Textbox(value="--v 5.2", label=localizer("Flags"))
                with gr.Accordion(label=''):
                    set_config_btn = gr.Button(localizer("设置"))

    images_upload.upload(data_pro.upload_embed_exchange_data,[embed_exchange_upload,embed_exchange_models],[embed_exchange_out],show_progress=True)
    # upscale_btn.click(text_image.upscale,outputs=[sub_image],show_progress=True)
    generate_btn.click(text_image.get_whole_image,inputs=[prompt],outputs=[images],show_progress=True)
    set_config_btn.click(text_image.setv,inputs=[channel_id,authorization,application_id,guild_id,session_id,version,id,flags],show_progress=True)
    # images.select(get_index,show_progress=True)
