from comickaze import Comickaze, Converter

comics_list = []

class Comic:
    def __init__(self, title, name):
        self.title = title
        self.name = name

def get_search(search_words):
    comics_list = []
    c = Comickaze(log_level="VERBOSE")
    search_results = c.search_comics(search_words) # Returns a list of Suggestion object

    for comic in search_results:
        comics_list.append(Comic(comic.title, (comic.link).rsplit('/', 1)[1]))

    return comics_list
