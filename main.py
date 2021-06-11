from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from get_comics import get_list, get_pagination_max
from get_issues import get_issues
from get_info import get_info
from get_pages import get_pages, cant_pages
from get_search import get_search

app = FastAPI(title='Comics API',
            description='API that delivers comics, issues and pages.',
            version='1.0.1')

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#get comics from page number
@app.get('/page/{page_number}')
async def read_page(page_number: int):
    if page_number > 0:
        return get_list(page_number)
    else:
        return 'Not found'

#get pages quantity
@app.get('/pages_number')
async def get_max_Pages():
    return get_pagination_max()

#get comic issues by name_url
@app.get('/comic/issues_list/{comic_name_url}')
async def comic_issues_list(comic_name_url: str):
    return get_issues(comic_name_url)

#get comic info by name_url
@app.get('/comic/info/{comic_name_url}')
async def comic_info(comic_name_url: str):
    return get_info(comic_name_url)

#get specific issue pages by comic_name_url and issue_number
@app.get('/comic/{comic_name_url}/{issue_number}')
async def comic_issue(comic_name_url: str, issue_number: str):
    return get_pages(comic_name_url, issue_number)

#get pages quantity of a issue by comic_name_url and issue_number
@app.get('/comic/cant/{comic_name_url}/{issue_number}')
async def comic_issue_pages_quantity(comic_name_url: str, issue_number: str):
    return cant_pages(comic_name_url, issue_number)

#get results of a search
@app.get('/search/{search_words}')
async def search(search_words: str):
    return get_search(search_words)
