import requests

url = 'https://translated-mymemory---translation-memory.p.rapidapi.com/api/get'


def translated(token, text, langpair=('ru', 'en')):
	querystring = {
		'langpair': '|'.join(langpair),
		'q': text,
		'mt': '1',
		'onlyprivate': '0'
	}
	headers = {
		'X-RapidAPI-Host': 'translated-mymemory---translation-memory.p.rapidapi.com',
		'X-RapidAPI-Key': token
	}

	response = requests.request("GET", url, headers=headers, params=querystring)

	return response.json()
