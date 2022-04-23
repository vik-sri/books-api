import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from books_api.defines import api_defines as api_def

module_name = "internal_create_book"


def get_book_data(book_id):
    book_metadata_link = api_def.ENDPOINT_GUTENBERG_BOOK_METADATA + book_id
    req_obj = requests.get(book_metadata_link)
    soup = BeautifulSoup(req_obj.text, 'html.parser')
    metadata = soup.find("div", {"id": "bibrec"})

    title = (metadata.find("td", {"itemprop": "headline"})).string.replace("\n", "")
    author = metadata.find("a", {"itemprop": "creator"}).string.replace(" ", "").split(",")
    author = " ".join(author[:-1])
    release_date = metadata.find("td", {"itemprop": "datePublished"}).string

    # Get categories from Google search
    session = HTMLSession()
    category_link = api_def.ENDPOINT_GOOGLE_SEARCH + title + "+" + "genre"
    r = session.get(category_link)
    soup2 = BeautifulSoup(r.text, 'html.parser')
    categories_soup = soup2.find("div", {"class": "KKHQ8c"})
    categories = [row.text for row in categories_soup]

    metadata_dict = {
        "title": title,
        "author": author,
        "categories": categories,
        "release_date": release_date
    }
    print(metadata_dict)
