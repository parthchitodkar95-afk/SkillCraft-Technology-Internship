# ============================================
#   SkillCraft Technology - Internship Task 04
#   Web Scraper - Product Info Extractor
#   Author: Parth Jivan Chitodkar
# ============================================

import requests
from bs4 import BeautifulSoup
import csv
import os

# We use books.toscrape.com - a free legal website made for scraping practice
BASE_URL = "https://books.toscrape.com/catalogue/"
START_URL = "https://books.toscrape.com/catalogue/page-1.html"

# Rating words to numbers
RATING_MAP = {
    "One": 1, "Two": 2, "Three": 3,
    "Four": 4, "Five": 5
}


def scrape_products(pages=3):
    all_products = []
    url = START_URL

    for page in range(1, pages + 1):
        print(f"Scraping page {page}...")

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching page {page}: {e}")
            break

        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.find_all("article", class_="product_pod")

        for book in books:
            # Product Name
            name = book.find("h3").find("a")["title"]

            # Price
            price = book.find("p", class_="price_color").text.strip()
            price = price.replace("Â", "").replace("£", "").strip()

            # Rating
            rating_class = book.find("p", class_="star-rating")["class"][1]
            rating = RATING_MAP.get(rating_class, 0)

            # Availability
            availability = book.find("p", class_="instock availability").text.strip()

            all_products.append({
                "Name": name,
                "Price (£)": price,
                "Rating (out of 5)": rating,
                "Availability": availability
            })

        # Go to next page
        next_btn = soup.find("li", class_="next")
        if next_btn:
            next_page = next_btn.find("a")["href"]
            url = BASE_URL + next_page
        else:
            print("No more pages found.")
            break

    return all_products


def save_to_csv(products, filename="products.csv"):
    if not products:
        print("No products to save!")
        return

    fieldnames = ["Name", "Price (£)", "Rating (out of 5)", "Availability"]

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(products)

    print(f"\nData saved to '{filename}' successfully!")


def display_products(products):
    print("\n" + "=" * 70)
    print(f"{'No.':<5} {'Name':<45} {'Price':>8} {'Rating':>8}")
    print("=" * 70)
    for i, p in enumerate(products, 1):
        name = p["Name"][:42] + "..." if len(p["Name"]) > 42 else p["Name"]
        print(f"{i:<5} {name:<45} £{p['Price (£)']:>6}  {'★' * p['Rating (out of 5)']}")
    print("=" * 70)


# ---- Main Program ----
print("=" * 50)
print("   SkillCraft Technology - Task 04")
print("   Web Scraper - Product Info Extractor")
print("=" * 50)
print("\nWebsite : books.toscrape.com")
print("Data    : Product Name, Price, Rating, Availability")
print("Output  : products.csv")
print("-" * 50)

try:
    pages = int(input("How many pages to scrape? (1-5 recommended): ").strip())
    if pages < 1:
        pages = 1
    if pages > 10:
        pages = 10
except ValueError:
    pages = 3
    print("Invalid input, defaulting to 3 pages.")

print(f"\nStarting scraper for {pages} page(s)...\n")

products = scrape_products(pages)

if products:
    print(f"\nTotal products scraped: {len(products)}")
    display_products(products)
    save_to_csv(products)
    print(f"\nFile saved at: {os.path.abspath('products.csv')}")
    print("\nSkillCraft Technology - Task 04 Complete!")
else:
    print("No products found. Check your internet connection.")