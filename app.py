from flask import Flask

app = Flask(__name__)


@app.get('/')
def home():
    return 'Hello Home Page'

@app.get('/product')
def product():
    return 'Hello From Product Page'

@app.get('/about')
def about():
    return 'Hello From About Page'

@app.get('/contact')
def contact():
    return 'Hello From Contact Page'

if __name__ == '__main__':
    app.run()
