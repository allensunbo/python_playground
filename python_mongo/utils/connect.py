
import requests
from pymongo import MongoClient
import json


class MongoConnectUtil():

    """
        util class to connect to a mongo db
    """

    def __init__(self):
        super().__init__()

    def connect(self, dbName):
        client = MongoClient()
        self.db = client[dbName]

    def insert(self, data, collectionName):
        if not 'db' in self.__dict__ or self.db is None:
            raise Exception('db is not initialized')
        return self.db[collectionName].insert(data)


if __name__ == '__main__':
    util = MongoConnectUtil()
    util.connect('python_mongo')
    util.insert({'name': 'alex'}, 'users')

    #
    app_key = 'a8e8e4c9ce101e94e09913cbdcc7a86d'
    baseUrl = 'http://api.themoviedb.org/3/'
    mode = 'configuration?'
    key = 'api_key=' + app_key
    url = baseUrl + mode + key
    r = requests.get(url)
    configuration = r.json()
    images_url = configuration['images']['base_url']
    poster_size = configuration['images']['poster_sizes'][0]
    print(images_url)
    print(configuration['images'])
    print(poster_size)

    mode = 'search/movie?query='
    search = 'alien&'
    url = baseUrl + mode + search + key
    print(url)
    r = requests.get(url)
    print(r.status_code)
    movies = r.json()
    print(images_url + poster_size + movies['results'][0]['poster_path'])
