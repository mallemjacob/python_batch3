from PIL import Image
with Image.open("500.jpg") as im:
    im.rotate(45).show()