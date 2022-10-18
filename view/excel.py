from flask import Blueprint, render_template

appExcel = Blueprint('appExcel', __name__)


@appExcel.route('/', methods = ['GET'])
@appExcel.route('/<date>', methods = ['GET'])
def query_excel(date = None):
    return render_template('excel/index.html', date = date)


@appExcel.route('/', methods = ['POST'])
def update_excel():
    return "update excel"
