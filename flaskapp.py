from flask import Flask, jsonify, request
import requests
from datetime import datetime
from bs4 import BeautifulSoup



app = Flask(__name__)
library={}
@app.route('/crawl', methods=['POST'])
def crawl():
    try:
        url = request.form['URL']
        code = requests.get(url)
    except:
        return "Inconsistent URL - try again"

    plain = code.text
    s = BeautifulSoup(plain, 'html.parser')

    text = s.find_all(text=True)
    contents = ''
    blacklist = [
        '[document]',
        'noscript',
        'header',
        'html',
        'meta',
        'head', 
        'input',
        'script',
        'style'
    ]

    for t in text:
        if t.parent.name not in blacklist:
            contents += '{} '.format(t)

    info = {
            'url':url,
            'date':str(datetime.now()),
            'contents': contents,
            'title': str(s.findAll('title'))
        }

    newid= str(10000+len(library))
    library[newid]=info
    return newid
    
    
@app.route('/retrieve/<ID>', methods=['GET'])
def retrieve(ID):
    try:
        entry = library[str(ID)]
        print(library[str(ID)])
        print(type(library[str(ID)]))
        
    except:
        entry = {}
    return entry

app.run(threaded=True)
