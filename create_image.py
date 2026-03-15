#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

# Создаем изображение
width, height = 800, 600
image = Image.new('RGB', (width, height), color='lightblue')
draw = ImageDraw.Draw(image)

# Рисуем прямоугольник
draw.rectangle([50, 50, 750, 550], outline='darkblue', width=5)

# Рисуем круг
draw.ellipse([200, 150, 600, 450], outline='red', width=5)

# Добавляем текст
try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 40)
except:
    font = ImageFont.load_default()

draw.text((250, 250), "OpenHands Test", fill='darkgreen', font=font)
draw.text((300, 300), "Image for GitHub", fill='darkgreen', font=font)

# Сохраняем изображение
image.save('downloaded_image.jpg', 'JPEG', quality=95)
print(f"Изображение создано: downloaded_image.jpg, размер: {os.path.getsize('downloaded_image.jpg')} байт")