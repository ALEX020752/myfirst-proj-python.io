from flask import Flask, render_template
from PIL import Image

def resize_image(input_image_path, output_image_path, size):
    original_image = Image.open(input_image_path)
    width, height = original_image.size
    resized_image = original_image.resize(size)
    resized_image.save(output_image_path)

# Пример использования
input_image_path = 'd:\Python\static\IMG_1.jpg'  # Путь к исходному изображению
output_image_path = 'd:\Python\static\IMG_1.jpg'  # Путь к уменьшенному изображению
new_size = (360, 480)  # Новые размеры (ширина, высота) изображения

resize_image(input_image_path, output_image_path, new_size)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return '<h2>Это страница "О нас". Здесь можно описать информацию о вашем проекте или компании.</h2>'

# Если пользователь переходит на "/auto_redirect", то он будет перенаправлен на главную страницу
@app.route('/auto_redirect')
def auto_redirect():
    return redirect(url_for('index'))

if __name__ == '__main__':
    # При запуске приложения автоматически открываем страницу "/auto_redirect"
    app.run(debug=True)
