# автоматически изменяет размер всех изображений в указанной папке, сохраняя пропорции

import os
from PIL import Image
import argparse

def resize_images(input_folder, output_folder, width):
    os.makedirs(output_folder, exist_ok=True)
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)
            aspect_ratio = img.height / img.width
            height = int(width * aspect_ratio)
            resized_img = img.resize((width, height))
            resized_img.save(os.path.join(output_folder, filename))
            print(f"✅ {filename} resized")
        else:
            print(f"❌ {filename} is not an image")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_folder', help='Папка с изображениями')
    parser.add_argument('output_folder', help='Папка для сохранения изменённых изображений')
    parser.add_argument('width', type=int, help='Ширина изменённых изображений')
    args = parser.parse_args()
    resize_images(args.input_folder, args.output_folder, args.width)
