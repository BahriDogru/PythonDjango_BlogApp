### Türkçe
# BlogApp

BlogApp, kullanıcıların blog yazılarını ekleyebileceği, kategorilere göre ayırabileceği ve diğer kullanıcıların blog yazılarını okuyabileceği bir Django uygulamasıdır.

## Proje Özellikleri

- Kullanıcılar blog yazıları ekleyebilir.
- Kullanıcılar blog yazılarına kategoriler ekleyebilir.
- Kullanıcılar blog yazılarını CKEditor5 kullanarak zenginleştirilmiş metin alanlarında yazabilir.
- Blog yazıları ve kategoriler veritabanında saklanır.
- Blog yazıları ana sayfada listelenir ve her blog yazısı için detay sayfası bulunmaktadır.
- Blog yazıları ve kategoriler admin panelinden yönetilebilir.

## Kurulum

### Gereksinimler

- Python 3.x
- Django 3.x veya daha üstü
- Pillow
- django-ckeditor-5

### Adımlar

1. Bu projeyi klonlayın:
    ```bash
    git clone https://github.com/kullanici_adiniz/BlogApp.git
    cd BlogApp
    ```

2. Gerekli paketleri yüklemek için bir sanal ortam oluşturun ve etkinleştirin:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows kullanıcıları için: venv\Scripts\activate
    ```

3. Gerekli bağımlılıkları yükleyin:
    ```bash
    pip install -r requirements.txt
    ```

4. Veritabanını migrate edin:
    ```bash
    python manage.py migrate
    ```

5. Admin kullanıcısı oluşturun:
    ```bash
    python manage.py createsuperuser
    ```

6. Sunucuyu başlatın:
    ```bash
    python manage.py runserver
    ```

7. Web tarayıcınızı açın ve `http://127.0.0.1:8000/` adresine gidin.

## Proje Yapısı

- `BlogApp/`: Django projesi ana dizini.
- `Blogapp/`: Blog uygulamasının ana dizini.
- `templates/`: HTML şablon dosyaları.
- `static/`: Statik dosyalar (CSS, JS, resimler).
- `media/`: Kullanıcı tarafından yüklenen dosyalar.
- `models.py`: Veritabanı modelleri.
- `views.py`: Uygulama iş mantığı ve HTTP isteklerinin işlendiği yer.
- `urls.py`: URL yönlendirmeleri.
- `admin.py`: Admin paneli yapılandırmaları.

## Kullanılan Teknolojiler

- **Django**: Web uygulaması geliştirme çatısı.
- **CKEditor5**: Zengin metin editörü.
- **Pillow**: Görüntü işleme kütüphanesi.

## Katkıda Bulunma

Katkıda bulunmak isterseniz, lütfen bir pull request gönderin veya bir sorun (issue) açın. Her türlü geri bildirime açığız.





*********************************************************************************************************************************************************************
### English

# BlogApp

BlogApp is a Django application where users can add blog posts, categorize them, and read other users' blog posts.

## Project Features

- Users can add blog posts.
- Users can add categories to blog posts.
- Users can write blog posts in rich text fields using CKEditor5.
- Blog posts and categories are stored in the database.
- Blog posts are listed on the homepage, and each post has a detail page.
- Blog posts and categories can be managed from the admin panel.

## Installation

### Requirements

- Python 3.x
- Django 3.x or higher
- Pillow
- django-ckeditor-5

### Steps

1. Clone this project:
    ```bash
    git clone https://github.com/your_username/BlogApp.git
    cd BlogApp
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Migrate the database:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

6. Start the server:
    ```bash
    python manage.py runserver
    ```

7. Open your web browser and go to `http://127.0.0.1:8000/`.

## Project Structure

- `BlogApp/`: Main Django project directory.
- `Blogapp/`: Main blog application directory.
- `templates/`: HTML template files.
- `static/`: Static files (CSS, JS, images).
- `media/`: User-uploaded files.
- `models.py`: Database models.
- `views.py`: Application logic and HTTP request handling.
- `urls.py`: URL routing.
- `admin.py`: Admin panel configurations.

## Technologies Used

- **Django**: Web application framework.
- **CKEditor5**: Rich text editor.
- **Pillow**: Image processing library.

## Contribution

If you want to contribute, please submit a pull request or open an issue. We welcome all feedback.

