import requests
from bs4 import BeautifulSoup
import csv

def scrape_books_to_csv():
    url = "https://books.toscrape.com/"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to retrieve page. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.content, "html.parser")
    
    # Each book is contained within an <article> tag with the class "product_pod"
    books = soup.find_all("article", class_="product_pod")
    
    # Open a CSV file for writing
    with open("books_data.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(["Title", "Price", "Availability"])
        
        for book in books:
            # Extract Title: The title attribute of the <a> tag inside the <h3> tag
            title = book.find("h3").find("a")["title"]
            
            # Extract Price: The text inside the <p> tag with class "price_color"
            price = book.find("p", class_="price_color").text
            
            # Extract Availability: The text inside the <p> tag with class "instock availability"
            availability = book.find("p", class_="instock availability").text.strip()
            
            # Write the extracted data to the CSV file
            writer.writerow([title, price, availability])

    print("Data successfully scraped and saved to 'books_data.csv'.")

if __name__ == "__main__":
    scrape_books_to_csv()
