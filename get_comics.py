from requests import get
from bs4 import BeautifulSoup

comics_list = []

class Comic:
    def __init__(self, name, name_url, img_url):
        self.name = name
        self.name_url = name_url
        self.img_url = img_url

def get_list(page):
    comics_list = []
    url = 'https://readcomicsonline.ru/latest-release?page='+str(page)
    response = get(url)

    html_soup = BeautifulSoup(response.text, 'html.parser')
    type(html_soup)

    comics_container = html_soup.find_all('h3', class_ = 'manga-heading pull-left')

    for comic in comics_container:
        comic_name = comic.a.text
        comic_name_url = ((comic.a['href']).rsplit('/', 1)[1])
        comic_img = ("https://readcomicsonline.ru/uploads/manga/"+((comic.a['href']).rsplit('/', 1)[1])+"/cover/cover_250x350.jpg")

        comics_list.append(Comic(comic_name, comic_name_url, comic_img))
    
    return comics_list

def get_pagination_max():
    url = 'https://readcomicsonline.ru/latest-release?page=1'
    response = get(url)

    html_soup = BeautifulSoup(response.text, 'html.parser')
    type(html_soup)

    pagination_block = html_soup.find('ul', class_ = 'pagination')

    pages = pagination_block.findAll('li')

    print(int(pages[len(pages)-2].text))

    return int(pages[len(pages)-2].text)