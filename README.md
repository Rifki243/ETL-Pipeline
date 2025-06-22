# 🛠️ ETL Pipeline Project

Proyek ini merupakan implementasi dari *Extract-Transform-Load (ETL)* pipeline yang dirancang untuk memproses data secara efisien. Dilengkapi dengan unit testing dan analisis coverage untuk memastikan kualitas dan keandalan kode.

![Coverage](https://img.shields.io/badge/coverage-92%25-brightgreen)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)

---

## 🚀 Menjalankan Proyek

Untuk menjalankan pipeline utama, gunakan perintah:

```bash
python main.py
```

## 🧪 Menjalankan Unit Test
Semua unit test berada di dalam folder tests. Jalankan semua test dengan:
```bash
python -m unittest discover -s tests
```

## 📊 Test Coverage
Untuk mengetahui sejauh mana kode telah diuji, jalankan:
```bash
# Jalankan coverage untuk unittest
coverage run -m unittest discover -s tests

# Tampilkan laporan di terminal
coverage report
```

## 🔍 HTML Report (Visualisasi Coverage)
Untuk menampilkan laporan coverage dalam format HTML:
```bash
coverage html
start htmlcov/index.html  # Untuk Windows
# atau
open htmlcov/index.html   # Untuk Mac/Linux
```

## 📝 Struktur Direktori
```bash
ETL-Pipeline/
├── htmlcov/                # Output HTML coverage
├── tests/                  # Unit test
│   ├── .coverage 
│   ├── test_extract.py
│   ├── test_load.py
│   └── test_transform.py               
├── utils/                  # Folder modul ETL
│   ├── extract.py
│   ├── load.py
│   └── transform.py 
├── main.py                 # Skrip utama ETL
├── Products.csv           
├── requirements.txt     
├── Submission.txt        
└── README.md
```

## 📦 Instalasi & Dependencies
Pastikan kamu sudah menginstal coverage:
```bash
pip install coverage
```
