
import pymysql 


class Database():
	'con, cur'
	con = ''

	def printf (format,*args):
  		sys.stdout.write (format % args)

	def printException (exception):
  		error, = exception.args
  		printf ("Error code = %s\n",error.code);
  		printf ("Error message = %s\n",error.message);

	def __init__(self):
		con = self.connection()

	def connection(self):
	    try:
	    	con = pymysql.connect(host = "localhost", user = 'root', passwd ='' , db = 'isilicondata', charset = 'utf8')		
	    	return con
	    except pymysql.DatabaseError:
		    printf('Failed to connect to %s\n', databaseName)
		    printException (exception)
		    exit(1)
	def close_connection(self, con):
		try:
			con.close()
			#con.commit()
			exit(0)
		except pymysql.DatabaseError:
			printException(exception)
			exit(1)
