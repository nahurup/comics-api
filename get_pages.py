from requests import get
from bs4 import BeautifulSoup

pages_list = []

def get_pages(comic_name_url, issue_number):
    pages_list = []

    max_pages = cant_pages(comic_name_url, issue_number)
    
    for number in range(1, max_pages+1, 1):
        if number < 10:
            page_url = ("https://readcomicsonline.ru/uploads/manga/"+comic_name_url+"/chapters/"+issue_number+"/0"+str(number)+".jpg")
        else:
            page_url = ("https://readcomicsonline.ru/uploads/manga/"+comic_name_url+"/chapters/"+issue_number+"/"+str(number)+".jpg")

        pages_list.append(page_url)
    
    return pages_list

def cant_pages(comic_name_url, issue_number):
    url = 'https://readcomicsonline.ru/comic/'+comic_name_url+'/'+issue_number
    response = get(url)

    html_soup = BeautifulSoup(response.text, 'html.parser')
    type(html_soup)

    pages_number_block = html_soup.find('select', class_ = 'selectpicker')

    pages_options = html_soup.find_all('option')

    pages_limit = pages_options[len(pages_options)-1].text

    return int(pages_limit)