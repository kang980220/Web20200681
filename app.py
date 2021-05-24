from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/baseball')
def baseball():
    return '야구 입니다'


@app.route('/volleyball')
def volleyball():
    return '배구 입니다'


@app.route('/soccer')
def soccer():
    return '''
    <html>
    <body>

    <h2>여기는 축구 페이지</h2>
    <img src="https://pds.joins.com//news/component/htmlphoto_mmdata/201805/05/1f9ce716-e664-4f2d-8643-835cb091fae9.jpg" alt="Trulli" width="500" height="333">

    </body>
    </html>

    '''

@app.route('/basketball')
def basketball():
    return '농구 입니다'

if __name__ == '__main__':
    app.run()