import os
from celery import shared_task
import time
from PIL import Image, ImageDraw, ImageFont
from .models import Mockup
@shared_task
def generate_mockup(text):
    colors = ["white", "black", "red", "blue"]
    output_paths = []
    #replacing spaces with underscores
    safe_text = text.replace(" ", "_")

    for color in colors:
        template_path = f"mockups/templates/{color}.png"
        template = Image.open(template_path).convert("RGBA")

        txt_layer = Image.new("RGBA", template.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(txt_layer)
        
        # Currently this `font` variable isn't used beyond drawing, 
        # and the DB font field is hardcoded. Might be useful later if we allow custom fonts.
        font = ImageFont.truetype("arial.ttf", 40)
        draw.text((200, 300), text, fill=(255, 255, 255, 255))

        combined = Image.alpha_composite(template, txt_layer)

        output_path = f"media/mockups/{color}_{safe_text}.png"
        
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        combined.save(output_path)
        output_paths.append(output_path)

        #saving each data in database 1 by 1 
        Mockup.objects.create(
            text=text,
            image_url=f"http://127.0.0.1:8000/{output_path.replace('\\','/')}",
            font="arial",
            text_color="#FFFFFF",
            shirt_color=color
        )
    return output_paths

