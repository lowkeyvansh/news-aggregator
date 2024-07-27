import requests
from bs4 import BeautifulSoup

def get_bbc_headlines():
    url = "https://www.bbc.com/news"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = []
    for item in soup.find_all('h3'):
        headline = item.get_text()
        link = item.find_parent('a')['href']
        headlines.append({"headline": headline, "link": link})

    return headlines

def get_cnn_headlines():
    url = "https://edition.cnn.com/world"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = []
    for item in soup.find_all('h3', class_='cd__headline'):
        headline = item.get_text()
        link = item.find_parent('a')['href']
        headlines.append({"headline": headline, "link": "https://edition.cnn.com" + link})

    return headlines

def display_headlines(source, headlines):
    print(f"\n{source} Headlines:")
    for index, headline in enumerate(headlines):
        print(f"{index + 1}. {headline['headline']}")
        print(f"   Link: {headline['link']}")

if __name__ == "__main__":
    bbc_headlines = get_bbc_headlines()
    cnn_headlines = get_cnn_headlines()

    display_headlines("BBC", bbc_headlines)
    display_headlines("CNN", cnn_headlines)
