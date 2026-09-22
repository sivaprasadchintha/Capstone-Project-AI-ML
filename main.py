import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url)

print(response.status_code)

soup = BeautifulSoup(response.content, 'html.parser')

# first_book = soup.find("article", class_="product_pod")
# title = first_book.h3.a["title"]
# price = first_book.find("p",class_="price_color").text

# # rating_p_tag=first_book.p 
# # rating_classes= rating_p_tag["class"]
# # #['star-rating','three']
# # rating = rating_classes[1]

# rating=first_book.p["class"][1]

# print(f"Title: {title}")
# print(f"Price: {price}")
# print(f"Rating: {rating} stars")

all_books = soup.find_all("article", class_="product_pod")
# print(len(all_books))
books_data= []

for book in all_books: 
    title = book.h3.a["title"]
    price = book.find("p",class_="price_color").text
    rating = book.p["class"][1]
    book_info = {
        "title": title,
        "price": price,
        "rating": f"{rating} stars"
    }
    books_data.append(book_info)

print(books_data)