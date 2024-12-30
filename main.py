import requests
from bs4 import BeautifulSoup
from store import insert_book_data

search_term='Mystery'
url = f'https://www.readanybook.online/genre/{search_term}-3'
headers ={
    'user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)
# print(response.content)
soup = BeautifulSoup(response.text, 'html.parser')
book_listing= soup.find_all('div',class_='col-xs-12 col-md-8')

page_number=int(input("enter page you want to visit:"))
next_page =soup.find("li",class_="next").get("href")
detail_url = f"https://www.readanybook.online/genre/mystery-3/page-{page_number}"
print(detail_url)

listings=[]
book_listing= soup.find_all("div",class_="preview-name")
ratings=[]
rating_detail =soup.find_all('div',class_='preview-rate')

for listing in book_listing:
    book_link = listing.find('a', href=True)
    book_title = listing.get_text(strip=True)
    book_url = book_link['href']
    
    for rating in rating_detail:
        rating = rating.find('b').get_text(strip=True) 
   
    print(f"Title: {book_title}")
    print(f"URL: {book_url}")
    print(f"Rating: {rating} / 10")
     
    insert_book_data(book_title, book_url, rating)






           