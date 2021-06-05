from fastapi import FastAPI
from get_comics import get_list, get_pagination_max

app = FastAPI(title='Hola',
            description='prueba de API',
            version='1.0.1')

#get comics from page number
@app.get('/{page}')
async def read_page(page: int):
    if page > 0:
        return get_list(page)
    else:
        return 'Not found'

#get pages quantity
@app.get('/about')
async def about():
    return get_pagination_max()