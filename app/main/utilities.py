import os
import uuid

# def get_img_file_path(instance, filename):
#     # Генерируем уникальное имя файла
#     filename = f'{uuid.uuid4().hex}.{filename.split(".")[-1]}'
#     # Возвращаем путь сохранения
#     return os.path.join('files_picture', 'main', 'content_ip', filename)

def get_img_file_path(instance, filename):
    ''' Сохраняем исходное имя с добавлением постфикса из 4 символов. '''
    ext = filename.split('.')[-1]  # Получаем расширение файла
    new_filename = f"{filename.split('.')[0]}_{uuid.uuid4().hex[:4]}.{ext}"
    return f"files_picture/main/content_ip/{new_filename}"