from requests import get
from bs4 import BeautifulSoup

issues_list = []

class Issue:
    def __init__(self, name, issue_number):
        self.name = name
        self.issue_number = issue_number


def get_issues(comic_name_url):
    issues_list = []
    url = 'https://readcomicsonline.ru/comic/'+comic_name_url
    response = get(url)

    html_soup = BeautifulSoup(response.text, 'html.parser')
    type(html_soup)

    issues_container = html_soup.find_all('li', class_ = 'volume-0')

    for issue in issues_container:
        name = issue.a.text
        issue_number = ((issue.a['href']).rsplit('/', 1)[1])

        issues_list.append(Issue(name, issue_number))
    
    return issues_list