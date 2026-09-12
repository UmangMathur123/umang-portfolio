from PIL import Image

def remove_white_bg(input_path, output_path):
    img = Image.open(input_path)
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        # If pixel is near white, make it transparent
        if item[0] > 230 and item[1] > 230 and item[2] > 230:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save(output_path, "PNG")

remove_white_bg(
    "C:/Users/User/.gemini/antigravity/brain/9faa7a56-8f85-44f4-9aa7-e1be2d1f1180/.user_uploaded/media_1789209565385.png",
    "assets/phone.png"
)
