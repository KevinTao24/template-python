from diffusers import DiffusionPipeline

pipeline = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
image = pipeline("美人鱼").images[0]
image.save("image_of_squirrel_painting-1.png")
