#python3
from googlesearch import search
'''
[description]
INPUT
    -query: String to search
RETURN
    Generator (iterator) that yields found URLs.
'''
def get_google_response(query):
    return search(query, tld="co.in", num=5, stop=5, pause=1)
