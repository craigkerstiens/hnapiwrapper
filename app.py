import os
import requests
import simplejson as json
from flask import request, render_template, abort, g, redirect, \
                  url_for, Response
from flask import Flask
app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def hello():
    try:
        r = requests.get('http://api.thriftdb.com/api.hnsearch.com/items/_search?q=%s' % request.args['q'])
        return request.args ['jsoncallback'] + '(' + r.content + ');'
    except:
        return "To use this api pass in a url: http://hnapiwrapper.herokuapp.com/?q=YOURQUERYHERE&jsoncallback=YOURJSFUNCTIONHERE"

@app.route("/button.html", methods=['POST', 'GET'])
def button():
    try:
        r = requests.get('http://api.thriftdb.com/api.hnsearch.com/items/_search?q=%s' % request.args['url'])
        data = json.loads(r.content)
        if data['hits'] > 0:
            if data['results'][0]['item']['points'] > 0:
                return render_template('button.html', **{
                    'points': data['results'][0]['item']['points'],
                    'url': request.args['url'],
                    'title': request.args['title']
                    })
            else:
                return render_template('buttonempty.html', **{
                'url': request.args['url'],
                'title': request.args['title']
                })
        else:
            return render_template('buttonempty.html', **{
            'url': request.args['url'],
            'title': request.args['title']
            })
            
    except:
        return "To use this api pass in a url: http://hnapiwrapper.herokuapp.com/?q=YOURQUERYHERE&jsoncallback=YOURJSFUNCTIONHERE"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
