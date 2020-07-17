import requests

class theMovieDb:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3"
        self.api_key = "71eb39a15d9c4310d258c11d47879371"

    def getPopulars(self):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return  response.json()

    def getsearch(self,keyword):
        response = requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={keyword}&page=1")
        return response.json()

movieApi = theMovieDb()

while True:
    secim = input("1- populer filmler\n2-search movies\n3-exit\nseçim ")
    if secim == "3":
        break
    else:
        if secim == "1":
            movie= movieApi.getPopulars()
            for movies in movie['results']:
                print(movies['title'])
        elif secim == "2":
            keyword = input("keyword: ")
            movie = movieApi.getsearch(keyword)
            for movies in movie['results']:
                print(movies['name'])




