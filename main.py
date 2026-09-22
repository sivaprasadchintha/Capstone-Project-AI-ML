import requests
from bs4 import BeautifulSoup
import time # for rate limiting 


all_books_data= []

for page_num in range(1,4):
    # Call url pagenation
    url = f"https://books.toscrape.com/catalogue/page-{page_num}.html"

    # Scrapped data by using pagination with url confirmation
    print(f" Scraping page {page_num}:{url}")

    # get books data
    response = requests.get(url)

    # if url call limitations notice with error message and break the loop
    if response.status_code != 200:
        print(f" page {page_num} not found. Stopping")
        break



# url = "https://books.toscrape.com/"

# response = requests.get(url)

# print(response.status_code)ṇ

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

    breadcrumb = soup.find("ul", class_="breadcrumb")

    if breadcrumb:
        category  = breadcrumb.find_all('li')[1].text.strip()
    else:
        category = "Unknown"

    print(breadcrumb)

    all_books_on_page = soup.find_all("article", class_="product_pod")
    # print(all_books_on_page)
    
    

    for book in all_books_on_page: 
        title = book.h3.a["title"]
        price = book.find("p",class_="price_color").text
        rating = book.p["class"][1]
        availability = book.find("p", class_="instock").text
        # category = book.find("ul", class_="breadcrumb")[2].text

        all_books_data.append({
            "title": title,
            "price": price,
            "rating": f"{rating} stars"
        })

    print(f"page{page_num} scraped. waiting 1 second")
    time.sleep(1)

print(f"\nscapping complete! found {len(all_books_data)} books. check for all_books")
