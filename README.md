<img width="1919" height="881" alt="image" src="https://github.com/user-attachments/assets/e62a7ce8-342e-460f-99e5-8a074b95edbf" />
<img width="1920" height="884" alt="image" src="https://github.com/user-attachments/assets/13d468ac-cbda-4b59-ad3e-7c7d533ff502" />

# Backend Data Siswa – Django REST Framework

Backend ini dibuat menggunakan **Django** dan **Django REST Framework** untuk mengelola data siswa.  
Proyek ini mendukung **Token Authentication**, sehingga setiap request ke endpoint API harus menyertakan token di header.

## 🚀 Teknologi yang Digunakan
- Python 3.x  
- Django  
- Django REST Framework  
- DRF Token Authentication  
- SQLite (development)  
- Railway (deployment)

---

## 📂 Struktur Proyek
```

data_siswa/
│── data_siswa/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│── siswa_app/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│── db.sqlite3
│── manage.py

```

---

## 🔑 Autentikasi

Menggunakan **Token Authentication**.

Cara mengirim token dalam header:

```

Authorization: Token <TOKEN_KAMU>

````

Contoh request dengan cURL:

```sh
curl -H "Authorization: Token 128baac3e2a2d98a4026e3b9203cd4ac7b7f0a1d" \
     http://localhost:8000/api/siswa/
````

---

## ▶️ Menjalankan Lokal

1. Clone repository

   ```sh
   git clone https://github.com/ahmadfauzanarif/backend-data-siswa-django.git
   cd backend-data-siswa-django
   ```

2. Buat virtual environment

   ```sh
   python -m venv myenv
   source myenv/Scripts/activate
   ```

3. Install dependencies

   ```sh
   pip install -r requirements.txt
   ```

4. Migrate database

   ```sh
   python manage.py migrate
   ```

5. Jalankan server

   ```sh
   python manage.py runserver
   ```

---

## 🌐 Deployment ke Railway

1. Login Railway CLI

   ```sh
   railway login
   ```

2. Inisialisasi project

   ```sh
   railway init
   ```

3. Tambahkan environment variable (jika perlu)

   * `DJANGO_SECRET_KEY`
   * `DEBUG=False`

4. Deploy

   ```sh
   railway up
   ```

Railway akan otomatis:

* Install dependencies dari `requirements.txt`
* Menjalankan server dengan `gunicorn` (buat Procfile jika diperlukan)

---

## 🧪 Endpoint API (Contoh)

| Endpoint           | Method    | Deskripsi         |
| ------------------ | --------- | ----------------- |
| `/api/siswa/`      | GET       | Ambil semua siswa |
| `/api/siswa/`      | POST      | Tambahkan siswa   |
| `/api/siswa/<id>/` | GET       | Detail siswa      |
| `/api/siswa/<id>/` | PUT/PATCH | Update siswa      |
| `/api/siswa/<id>/` | DELETE    | Hapus siswa       |

---

## ✍️ Kontribusi

Silakan fork repo, buat branch baru, dan ajukan pull request jika ingin berkontribusi.

---

## 📄 Lisensi

MIT License – bebas digunakan dan dikembangkan.

---
