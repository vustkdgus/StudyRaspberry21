from flask import Flask

app = Flask(__name__)

@app.route('/')  # controller
def index():
    return '''
        <!DOCTYPE html>

        <html lang="en" xmlns="http://www.w3.org/1999/xhtml">
        <head>
            <meta charset="utf-8" />
            <title></title>
        </head>
        <body>

        </body>
        </html>
    '''


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)