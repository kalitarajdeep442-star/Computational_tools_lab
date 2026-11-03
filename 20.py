import requests
from bs4 import BeautifulSoup

def scrape_hacker_news():
    # URL for Hacker News
    url = "https://news.ycombinator.com/"
    
    # Send a GET request to the website
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve page. Status code: {response.status_code}")
        return

    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Hacker News titles and links are inside <span class="titleline"> 
    # which contains an <a> tag with the actual headline and link.
    story_spans = soup.find_all("span", class_="titleline")
    
    headlines_and_links = []
    
    for span in story_spans:
        # Find the first anchor tag inside the span
        anchor = span.find("a")
        if anchor:
            title = anchor.text
            link = anchor.get("href")
            headlines_and_links.append({"title": title, "link": link})
            
    # Output the results
    print(f"Extracted {len(headlines_and_links)} articles:\n")
    for index, item in enumerate(headlines_and_links, start=1):
        print(f"{index}. {item['title']}")
        print(f"   Link: {item['link']}\n")

if __name__ == "__main__":
    scrape_hacker_news()
