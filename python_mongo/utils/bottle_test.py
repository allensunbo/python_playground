#!/usr/bin/python
import requests
import json
from bottle import route, run, error, hook, HTTPResponse, response


# @error(405)
# def method_not_allowed(res):
#     if request.method == 'OPTIONS':
#         new_res = HTTPResponse()
#         new_res.set_header('Access-Control-Allow-Origin', '*')
#         return new_res
#     res.headers['Allow'] += ', OPTIONS'
#     print('method_not_allowed')
#     return request.app.default_error_handler(res)


@hook('after_request')
def enableCORSAfterRequestHook():
    print('after_request')
    response.set_header('Access-Control-Allow-Origin', '*')


@route('/movies')
def movies():
    #
    index = 1
    app_key = 'a8e8e4c9ce101e94e09913cbdcc7a86d'
    baseUrl = 'http://api.themoviedb.org/3/'
    mode = 'configuration?'
    key = 'api_key=' + app_key
    url = baseUrl + mode + key
    r = requests.get(url)
    configuration = r.json()
    images_url = configuration['images']['base_url']
    poster_size = configuration['images']['poster_sizes'][index]
    # print(images_url)
    # print(configuration['images'])
    # print(poster_size)

    mode = 'search/movie?query='
    search = 'alien&'
    url = baseUrl + mode + search + key
    print(url)
    r = requests.get(url)
    print(r.status_code)
    movies = r.json()
    # print(images_url + poster_size + movies['results'][index]['poster_path'])
    response = '<ul>'
    for i in range(10):
        response = response + "<li><h2>" + movies['results'][i]['title'] + "</h2>" + "<p>" + movies['results'][i][
            'release_date'] + "</p>" + "<img src=\"" + images_url + poster_size + movies['results'][i]['poster_path'] + "\"></li>"
    response = response + '</ul>'
    return response


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)
