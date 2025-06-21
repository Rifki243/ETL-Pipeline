import csv
import os

def save_to_csv(data, filename='Products.csv'):
    """
    Menyimpan data ke file CSV.
    :param data: List of dicts hasil transformasi data.
    :param filename: Nama file output CSV.
    """
    if not data:
        raise ValueError("Data kosong, tidak bisa disimpan.")

    # Pastikan direktori output ada (jika ada path foldernya)
    if os.path.dirname(filename):
        os.makedirs(os.path.dirname(filename), exist_ok=True)

    keys = data[0].keys()  # Ambil kolom dari dictionary pertama

    # Simpan ke file CSV
    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

    print(f"Data berhasil disimpan dalam '{filename}'")
