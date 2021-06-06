from requests import get
from bs4 import BeautifulSoup

comic_info = {
    'title': " ",
    'status': " ",
    'date': 0,
    'views': 0,
    'rating': 0,
    'max_issues': 0
}

def get_info(name):
    url = 'https://readcomicsonline.ru/comic/'+name
    response = get(url)

    html_soup = BeautifulSoup(response.text, 'html.parser')
    type(html_soup)

    info_container = html_soup.find_all('dd')

    comic_info['status'] = info_container[1].text #status
    comic_info['date'] = info_container[2].text #date
    comic_info['views'] = info_container[5].text #views
    comic_info['rating'] = info_container[6].text #rating

    info_container = html_soup.find_all('h2', class_ = 'listmanga-header')
    
    comic_info['title'] = info_container[0].text #title

    info_container = html_soup.find_all('li', class_ = 'volume-0')

    comic_info['max_issues'] = len(info_container)
    
    return comic_info