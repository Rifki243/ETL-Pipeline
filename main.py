from utils.extract import extract_data
from utils.transform import transform_data
from utils.load import save_to_csv

def main():
    print("Memulai proses ETL...")

    # Extract
    print("Menjalankan proses Extract...")
    raw_data = extract_data(max_items=1000, max_pages=50)
    print(f"Extract selesai. Total data yang diambil: {len(raw_data)}")

    # Transform
    print("Menjalankan proses Transform...")
    cleaned_data = transform_data(raw_data)
    print(f"Transform selesai. Total data setelah dibersihkan: {len(cleaned_data)}")

    # Load
    print("Menjalankan proses Load (simpan ke CSV)...")
    save_to_csv(cleaned_data.to_dict(orient='records'), filename="Products.csv")
    print("Proses ETL selesai!")

if __name__ == "__main__":
    main()
