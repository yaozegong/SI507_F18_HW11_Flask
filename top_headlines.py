from flask import Flask, render_template
from secrets_example import*
import requests
import json

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Welcome!</h1>'



#@app.route('/user/<name>')
#def user(name):
#    return render_template('user.html', name=name)




@app.route('/user/<name>')
def hello_user(name):
    baseurl ='https://api.nytimes.com/svc/topstories/v2/'
    extendedurl = baseurl + 'technology' +'.json'
    params={'api-key': api_key}
    content=requests.get(extendedurl, params).json()
    count=0
    list=[]
    for i in content['results']:
        count+=1
        list.append(str(count)+'.'+' '+i['title']+ ' ' +i['url'])
        if(count==5):
            break
    return render_template('user.html',name=name, my_list=list)



if __name__ == '__main__':
    app.run(debug=True)
