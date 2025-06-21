from bs4 import BeautifulSoup
import requests
from datetime import datetime

def extract_data(max_items=1000, max_pages=50):
    data_collection = []
    collected = 0

    for page_num in range(1, max_pages + 1):
        if page_num == 1:
            url = "https://fashion-studio.dicoding.dev/"
        else:
            url = f"https://fashion-studio.dicoding.dev/page{page_num}"

        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        for item in soup.find_all('div', class_='collection-card'):
            if collected >= max_items:
                break

            product_details = item.find('div', class_='product-details')
            if not product_details:
                continue

            title_tag = product_details.find('h3')
            price_tag = product_details.find('span', class_='price')

            title = title_tag.get_text(strip=True) if title_tag else None
            price = price_tag.get_text(strip=True) if price_tag else None

            rating, color, size, gender = None, None, None, None
            for p in product_details.find_all('p'):
                text = p.get_text(strip=True)
                if text.startswith("Rating:"):
                    rating = text.replace("Rating:", "").replace("⭐", "").replace(" / 5", "").strip()
                elif "Color" in text:
                    color = text.replace("Colors", "").replace("Color", "").strip()
                elif text.startswith("Size:"):
                    size = text.replace("Size:", "").strip()
                elif text.startswith("Gender:"):
                    gender = text.replace("Gender:", "").strip()

            timestamp = datetime.now().isoformat()

            data_collection.append({
                "Title": title,
                "Price": price,
                "Rating": rating,
                "Color": color,
                "Size": size,
                "Gender": gender,
                "Timestamp": timestamp
            })

            collected += 1

        if collected >= max_items:
            break

    return data_collection