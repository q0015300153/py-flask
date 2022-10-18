from flask import Blueprint, render_template

from configs import Db

appExcel = Blueprint('appExcel', __name__)


@appExcel.route('/', methods = ['GET'])
@appExcel.route('/<date>', methods = ['GET'])
def query_excel(date = None):
    db = Db()
    db.into("INSERT INTO test (id, data) VALUES (%s, %s)", "A", "B")
    return render_template('excel/index.html', date = date)


@appExcel.route('/', methods = ['POST'])
def update_excel():
    return "update excel"
