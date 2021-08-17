from flask import Flask, jsonify, request
import requests
from datetime import datetime
from bs4 import BeautifulSoup

library={}

app = Flask(__name__)
@app.route('/scrape', methods=['POST'])
def scrape():
    
    try:
        url = request.form['URL']
        code = requests.get(url)
        plain = code.text
        s = BeautifulSoup(plain, 'html.parser')
        info = {
                'url':url,
                'date':str(datetime.now()),
                'contents': s,
                'title': str(s.findAll('title'))
            }
        newid= str(id(url))
        library[newid]=info
        return newid
    except:
        return "Inconsistent URL - try again"
    
@app.route('/retrieve/<ID>', methods=['GET'])
def retrieve(ID):
    try:
        entry = library[str(ID)]
    except:
        entry = {}
    return jsonify(entry)

app.run(threaded=True)