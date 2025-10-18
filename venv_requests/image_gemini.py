from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

# Initialize the client
client = genai.Client(api_key='API_KEY')

prompt = (
    "Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme"
)

# 1. Use the correct API method and model for image generation
result = client.models.generate_images(
    model="imagen-3.0-generate-002",
    prompt=prompt,
    config=dict(
        number_of_images=1,
        output_mime_type="image/png",
        aspect_ratio="1:1"
    )
)

# 2. Access the generated images from the result object
if result.generated_images:
    # Get the image data from the first (and only) generated image
    image_data = result.generated_images[0].image.image_bytes
    
    # Use BytesIO to open the image data
    image = Image.open(BytesIO(image_data))
    
    # Save the image
    image.save("generated_image.png")
    print("Image saved as generated_image.png")
else:
    print("Image generation failed or returned no images.")