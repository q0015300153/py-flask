from flask import Flask

from view.excel import appExcel
from view.index import appIndex

app = Flask(__name__, template_folder = 'templates')
app.register_blueprint(appIndex)
app.register_blueprint(appExcel, url_prefix = '/excel')

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 80)
