import pandas as pd

rupiah = 16000  # Dolar ke Rupiah

def convert_price_to_rupiah(price_str):
    try:
        price_num = float(price_str.replace("$", "").replace(",", "").strip())
        return round(price_num * rupiah)
    except:
        return None

def clean_rating(rating_str):
    try:
        if "Not Rated" in rating_str or "Invalid" in rating_str:
            return None
        rating = float(rating_str.split()[0])
        return rating
    except:
        return None

def transform_data(data):
    df = pd.DataFrame(data)

    # Hapus data dengan title "Unknown Product" dan rating tidak valid
    df = df[~df["Title"].str.contains("Unknown Product", na=False)]
    df = df[~df["Rating"].str.contains("Not Rated|Invalid", na=False)]

    # Drop baris yang kolom pentingnya null
    df = df.dropna(subset=["Title", "Price", "Rating", "Timestamp"])

    # Konversi kolom harga dan rating
    df["Price"] = df["Price"].apply(convert_price_to_rupiah)
    df["Rating"] = df["Rating"].apply(clean_rating)

    # Konversi tipe data
    df["Title"] = df["Title"].astype("object")
    df["Price"] = df["Price"].astype("float64")
    df["Rating"] = df["Rating"].astype("float64")
    df["Color"] = df["Color"].astype("int64")
    df["Gender"] = df["Gender"].astype("object")
    df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce")

    # Drop baris jika timestamp gagal diubah
    df = df.dropna(subset=["Timestamp"])

    # Hapus duplikat
    df = df.drop_duplicates()

    return df.reset_index(drop=True)