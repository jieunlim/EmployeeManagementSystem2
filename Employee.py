import Database
import pymysql
import datetime


class Employee():
	'employee_ID, login_ID, department_ID, manager_ID, title, birthDate, maritalStatus, hireDate, vacationHours, sickLeaveHours, modified_Date, gender'
	#constructor
	def __init__(self):
		self.employee_ID = 0
		self.login_ID = 0
		self.department_ID = 0
		self.manager_ID = 0
		self.title = 0
		self.birthDate = 0
		self.maritalStatus = 0
		self.hireDate = 0
		self.vacationHours = 0
		self.sickLeaveHours = 0
		self.modified_Date = 0
		self.gender = 0

	def ShowEmployee(self):
		print(
			str(self.employee_ID) + "\t"+
			str(self.login_ID) + "\t"+ 
			str(self.department_ID) + "\t"+
			str(self.manager_ID) + "\t"+
			str(self.title) + "\t"+
			str(self.birthDate) + "\t"+ 
			str(self.maritalStatus) + "\t"+ 
			str(self.hireDate) + "\t"+ 
			str(self.vacationHours) + "\t"+ 
			str(self.sickLeaveHours) + "\t"+ 
			str(self.modified_Date) + "\t"+
			str(self.gender)
			)
		
	def getAllEmployee(self):

		instance = Database.Database()
		con = instance.connection()
		cur = con.cursor()
		#employee_ID, login_ID, department_ID, manager_ID, title, birthDate, maritalStatus, hireDate, vacationHours, sickLeaveHours, modified_Date, gender'
		try:
			sql = "select * from iemployee order by employee_id"
			cur.execute(sql)
			#columns = [column[0] for column in cur.description]
			#print (columns)
			
			resultSet = cur.fetchall()
			
			for i in resultSet:
				
				emp = Employee()
				emp.employee_ID = i[0]
				emp.login_ID = i[1] 
				emp.department_ID = i[2]
				emp.manager_ID = i[3]
				emp.title=i[4] 
				emp.birthDate = i[5]
				emp.maritalStatus = i[6] 
				emp.hireDate=i[7]
				emp.vacationHours = i[8] 
				emp.sickLeaveHours = i[9] 
				emp.modified_Date=i[10]
				emp.gender=i[11]
				emp.ShowEmployee()
				
		except pymysql.InternalError:
			printf('Failed to select from employee\n')
			printException(exception)
			exit(1)
		finally:
			cur.close()
	def getEmployee(self, id):

		instance = Database.Database()
		con = instance.connection()
		cur = con.cursor()

		try:
			sql = "select * from iemployee where employee_id = '%d'" % (id)

			cur.execute(sql)
			resultSet = cur.fetchall()
			
			for i in resultSet:
				emp = Employee()
				emp.employee_ID = i[0]
				emp.login_ID = i[1] 
				emp.department_ID = i[2]
				emp.manager_ID = i[3]
				emp.title=i[4] 
				emp.birthDate = i[5]
				emp.maritalStatus = i[6] 
				emp.hireDate=i[7]
				emp.vacationHours = i[8] 
				emp.sickLeaveHours = i[9] 
				emp.modified_Date=i[10]
				emp.gender=i[11]
				emp.ShowEmployee()

		except pymysql.InternalError:
			printf('Failed to select from employee\n')
			printException(exception)
			exit(1)
		finally:
			cur.close()
			#con.close()
			#exit(0)
	def updateEmployee(self, id, sel, sel_i, sel_str, sel_d):
		instance = Database.Database()
		con = instance.connection()
		cur = con.cursor()
		today = datetime.datetime.today().strftime('%Y-%m-%d')
		
		

                #employee_ID, login_ID, department_ID, manager_ID, title, birthDate, maritalStatus, hireDate, vacationHours, sickLeaveHours, modified_Date, gender'


		try:
			if sel == "1":
				sql = "update iemployee set login_id='%s',modified_Date ='%s' where employee_id='%d' " % (sel_str,today,id)
					
			elif sel == "2":
				sql = "update iemployee set department_ID='%d',modified_Date ='%s' where employee_id='%d' " % (sel_i,today,id)
				
			elif sel == "3":
				sql = "update iemployee set manager_ID='%d',modified_Date ='%s' where employee_id='%d' " % (sel_i,today,id)
		
			elif sel == "4":
				sql = "update iemployee set title='%s',modified_Date ='%s' where employee_id='%d' " % (sel_str,today,id)
			
			elif sel == "5":
				sql = "update iemployee set birthDate ='%s',modified_Date ='%s' where employee_id='%d' " % (sel_d,today,id)
			
			elif sel == "6":
				sql = "update iemployee set maritalStatus='%s',modified_Date ='%s' where employee_id= '%d' " % (sel_str,today,id);
			
			elif sel == "7":
				sql = "update iemployee set hireDate='%s' ,modified_Date  ='%s'where employee_id='%d' " % (sel_d,today,id)
			
			elif sel == "8":
				sql = "update iemployee set vacationHours='%d',modified_Date ='%s' where employee_id='%d' " % (sel_i,today,id)
				
			elif sel == "9":
				sql = "update iemployee set sickLeaveHours='%d',modified_Date =  ='%s' where employee_id= '%d' " % (sel_i,today,id)
				
			elif sel == "10":
				sql = "update iemployee set gender=?,modified_Date = '%s' where employee_id= '%d' " % (sel_str,today,id);
				
			
			if sel is not "11":
				cur.execute(sql)
				print("Updated successfully!")
				
		except pymysql.InternalError:
			printf('Failed to update from employee\n')
			printException(exception)
			exit(1)
		finally:
			cur.close()
			#con.close()
			#exit(0)

	def deleteEmployee(self, id):

		instance = Database.Database()
		con = instance.connection()
		cur = con.cursor()

                #employee_ID, login_ID, department_ID, manager_ID, title, birthDate, maritalStatus, hireDate, vacationHours, sickLeaveHours, modified_Date, gender'


		try:
			sql = "delete from iemployee where employee_id = '%d'" % (id)
			cur.execute(sql)
			print("Deleted Successfully.")


		except pymysql.DatabaseError:
			printf('Failed to delete from employee\n')
			printException(exception)
			exit(1)
		finally:
			cur.close()
			#con.close()
	def addEmployee(self, Employee_ID, Login_ID, Department_ID, Manager_ID, Title, BirthDate, MaritalStatus, HireDate, VacationHours, SickLeaveHours, Modified_Date, Gender):
		
		emp = Employee()
		self.employee_ID = Employee_ID
		self.login_ID = Login_ID
		self.department_ID = Department_ID
		self.manager_ID = Manager_ID
		self.title = Title
		self.birthDate = BirthDate
		self.maritalStatus = MaritalStatus
		self.hireDate = HireDate
		self.vacationHours = VacationHours
		self.sickLeaveHours = SickLeaveHours
		self.modified_Date = Modified_Date
		self.gender = Gender
		instance = Database.Database()
		con = instance.connection()
		cur = con.cursor()		
		try:
			sql = "insert into iemployee VALUES(%s,'%s',%s,%s,'%s','%s','%s','%s',%s,%s,'%s','%s')"  % (Employee_ID, Login_ID, Department_ID, Manager_ID, Title, BirthDate, MaritalStatus, HireDate, VacationHours, SickLeaveHours, Modified_Date, Gender);
			
			cur.execute(sql)
			print("Updated successfully!")
			
		except pymysql.InternalError:
			print('Failed to add from employee\n')
			printException(exception)
			exit(1)

	