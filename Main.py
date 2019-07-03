import requests, json

def get_url():
    api_key='da0d1f91'
    url = 'http://www.omdbapi.com/?apikey='
    query = input("Film: ")
    query = query.replace(' ', '+')
    
    param_type = str(input("title or IMDB-Id : "))
    accepted_vals = ['title', 'IMDB-Id']
    while param_type not in accepted_vals:
        print("Please enter valid search type")
        param_type = str(input("title or IMDB-Id : "))

    if param_type == 'title':
        url_param = '&t='
    elif param_type == 'IMDB-Id':
        url_param = '&i='
    
    response = requests.get(url + api_key + url_param + query)

    with open('movieinfo.json', 'w+') as data_file:
        json.dump(response.json(), data_file, indent=4, sort_keys=False)

    if response:
        print("I found something!")
    else:
        print("An error has occurred")
    if response.status_code == 200:
        print("Success!")
    elif response.status_code == 404:
        print("Not Found.")
    
    # print(response.json())

get_url()