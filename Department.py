import Database
import pymysql

class Department:
	'department_ID, name, group_name, modified_Date'
	#constructor
	def __init__(self):
		self.department_ID = ""
		self.name = ""
		self.group_name = ""
		self.modified_Date = ""
		
	def showDepartment(self):
		print(
			str(self.department_ID) + "\t" + 
			str(self.name) + "\t" + 
			str(self.group_name) + "\t" + 
			str(self.modified_Date)
			)
	
	
	def getDepartment(self, id):

		instance = Database.Database()
		con = instance.connection()
		cur = con.cursor()

                #employee_ID, login_ID, department_ID, manager_ID, title, birthDate, maritalStatus, hireDate, vacationHours, sickLeaveHours, modified_Date, gender'


		try:
			sql = "select * from department where department_id = (select department_id from iemployee where employee_id = '%d')"% (id)
			cur.execute(sql)
			resultSet = cur.fetchall()
			
			for i in resultSet:
				dep = Department()
				dep.department_ID = i[0]
				dep.name = i[1]
				dep.group_name = i[2]
				dep.modified_Date = i[3]
				dep.showDepartment()
			
		except pymysql.InternalError:
			printf('Failed to select from employee\n')
			printException(exception)
			exit(1)
		finally:
			cur.close()
			#con.close()
			#exit(0)
