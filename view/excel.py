import uuid

from flask import Blueprint, jsonify, request

from configs import Db

appExcel = Blueprint('appExcel', __name__)


@appExcel.route('/', methods = ['GET'])
@appExcel.route('/<date>', methods = ['GET'])
def query_excel(date = None):
    id = request.values.get('id')

    db = Db()
    result = db.query("SELECT * FROM test WHERE id = %s", id)
    return result
    # return render_template('excel/index.html', date = date)


@appExcel.route('/', methods = ['POST'])
def update_excel():
    id = str(uuid.uuid4())
    data = request.values.get('data')

    db = Db()
    db.exec("INSERT IGNORE INTO test (id, data) VALUES (%s, %s)", id, data)
    return jsonify({'id': id, 'data': data})
