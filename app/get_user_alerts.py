from contextlib import closing
from app import app
import config
import MySQLdb
import MySQLdb.cursors

def get_user_alerts(service, area):
	db = MySQLdb.connect(host=app.DB_HOST, user=app.DB_USER, passwd=app.DB_PASSWD, db=app.DB_NAME, cursorclass=MySQLdb.cursors.DictCursor)
	with closing(db.cursor()) as cursor:
		cursor.execute("SELECT * FROM user_alerts WHERE service = %s AND area = %s AND active = 1", [service, area])
		data = cursor.fetchall()
	return data