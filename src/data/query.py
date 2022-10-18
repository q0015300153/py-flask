from configs import Db


def query_user():
    db = Db()
    user = db.query("SELECT * FROM users WHERE account = %s", "M317832")
    print(user)
