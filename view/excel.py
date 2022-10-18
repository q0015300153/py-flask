import uuid
from datetime import datetime

from flask import Blueprint, render_template

from configs import Db

appExcel = Blueprint('appExcel', __name__)


@appExcel.route('/', methods = ['GET'])
@appExcel.route('/<date>', methods = ['GET'])
def query_excel(date = None):
    id = str(uuid.uuid4())
    data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    db = Db()
    db.exec("INSERT IGNORE INTO test (id, data) VALUES (%s, %s)", id, data)
    print(db.query("SELECT * FROM test WHERE id = %s", id))
    db.exec("DELETE FROM test WHERE id = %s", id)
    
    return render_template('excel/index.html', date = date)


@appExcel.route('/', methods = ['POST'])
def update_excel():
    return "update excel"
