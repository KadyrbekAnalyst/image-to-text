# import os
# from transformers import pipeline
# import time

# # Устанавливаем путь кэша для transformers
# os.environ["TRANSFORMERS_CACHE"] = r"D:\.cache"

# start_time = time.time()
# # Создание пайплайна для генерации изображений
# image_generator = pipeline('image-generation', model='CompVis/stable-diffusion-v1-4', device=-1)  # device=-1 для использования CPU

# # Генерация изображения
# prompt = "A house in the forest"
# image = image_generator(prompt, num_inference_steps=50)[0]['image']  # Уменьшаем количество шагов для ускорения

# # Сохранение изображения
# image.save("./images/generated_image.png")

# # Вывод затраченного времени
# print("Time taken: ", time.time() - start_time, "seconds")


import os
from diffusers import DiffusionPipeline
import torch
import time

start_time = time.time()

# Задаем относительный путь к папке images относительно расположения main.py
output_dir = "images"
os.makedirs(output_dir, exist_ok=True)


# Убедитесь, что используете float32 вместо float16 для CPU
pipe = DiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    torch_dtype=torch.float32,  # Используем float32 для CPU
    use_safetensors=True,
    cache_dir='D:/HuggingFaceCache'
)

# Отключаем offload для CPU
# pipe.enable_model_cpu_offload(False)

# prompt = "An astronaut riding a green horse"

prompt = "The IT workers from Alamaty which work on Smart city to increase the city value on world arena , the Alamaty Development Avangers"

pipe = pipe.to('cpu')

# Явно указываем устройство 'cpu'
images = pipe(prompt=prompt).images[0]

# Проверяем, что изображение существует в объекте
if images:
    print("Image is generated.")
else:
    print("No image is generated.")

# Сохраняем изображение в указанной директории
output_path = os.path.join(output_dir, "generated_image.png")


try:
    images.save(output_path)
    print(f"Image successfully saved to {output_path}")
except Exception as e:
    print(f"Failed to save image: {e}")


# Вывод затраченного времени
print("Time taken: ", time.time() - start_time, "seconds")
