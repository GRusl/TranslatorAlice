import os

import json

from RapidAPI import translated

from flask import Flask, request

app = Flask(__name__)


@app.route('/post', methods=['POST'])
def main():
    response = {
        'session': request.json['session'],
        'version': request.json['version'],
        'response': {
            'end_session': False
        }
    }
    handle_dialog(response, request.json)
    return json.dumps(response)


def handle_dialog(res, req):
    if req['session']['new']:
        res['response']['text'] = 'Привет! Попроси меня перевести слово в фомате: Переведи слово <Слово>.'
        return

    command = req['request']['command'].split()

    if len(command) > 2:
        word1, word2, *words = command
        if 'переведи' in word1 and word2[:4] in ('слов', 'фраз'):
            res['response']['text'] = translated(os.environ['TOKEN'],
                                                 ' '.join(words))['responseData']['translatedText']
            return

    res['response']['text'] = 'Я не услышала слово...'


if __name__ == '__main__':
    app.run()
