
import Database
import datetime
import Employee
import Department
import pymysql

class ManagementSystem():

	menuOption = 0
	
	def showColumn(self):
		print("\nID"+ "\tLog_ID"+ "\tDep"+ "\tMag"+ "\tTitle"+ "\tBirthDate"+ "\tS/M"+ "\tHireDate"+ "\tVac"+ "\tSick"+ "\tModified"+ "\tGender")
	
	def showColumnDep(self):
		print("Dep_ID\tName\tGroup\tModified_Date")
	
	def __init__(self) :


		while self.menuOption != "7" :
			self.menuOption = input("\n======= Select Menu========="
			+ "\n1.All Employees"
			+ "\n2.Display Employee by ID"
			+ "\n3.Display Employee's department by ID"
			+ "\n4.Update Employee's info"
			+ "\n5.Delete Employee"
			+ "\n6.Add new Employee"
			+ "\n7.Exit"
			+ "\n========= Select: > ")

			if self.menuOption == "1":
			#GetAllEmployee
				self.showColumn()
				instance = Employee.Employee()
				instance.getAllEmployee()

			elif self.menuOption == "2":
			#GetEmployee()
				id = int(input("\nPlease enter employee's ID: > "))
				instance = Employee.Employee()
				self.showColumn()
				instance.getEmployee(id)

			elif self.menuOption == "3":
			#DisplayDepartment()
				id = int(input("\nPlease enter employee's ID to see department: > "))
				instance1 = Department.Department()
				self.showColumnDep()
				instance1.getDepartment(id)
				

			elif self.menuOption == "4":
			#UpdateEmployee()
				selection = 0
				selection_int = 0
				selection_str = ""
				selection_d = ""

				id = int(input("\nPlease enter employee's ID to update: > "))
				instance1 = Employee.Employee()
				self.showColumn()
				instance1.getEmployee(id)
				while selection != "11" :
					selection = input("\nWhich information do you want to UPDATE\n  "
					+ "\n======= Select Menu========="
					+ "\n1.Login_ID"
					+ "\n2.Department_ID"
					+ "\n3.Manager_ID"
					+ "\n4.Title"
					+ "\n5.BirthDate"
					+ "\n6.MaritalStatus"
					+ "\n7.HireDate"
					+ "\n8.VacationHours"
					+ "\n9.SickLeaveHours"
					+ "\n10.Gender"
					+ "\n11.Exit"
					+ "\n========= Select: > ")
				#integer
					if(selection == '2' or selection == '3' or selection == '8' or selection == '9'):
						selection_int = input("\nUpdate to : > ")

				#string
					elif(selection == '1' or selection == '4' or selection == '6'  or selection == '10'):
						selection_str = input("\nUpdate to : > ")
				#date
					elif(selection == '5' or selection == '7') :
						selection_d = input("\nPlease follow this format \"20170101\"\n"
						+"Update to : > ")
					else:
						break
					
					instance1.updateEmployee(id, selection,selection_int,selection_str,selection_d)
					self.showColumn()
					instance1.getAllEmployee()

			elif self.menuOption == "5":
			#DeleteData()
				
				id = int(input("\nPlease enter employee's ID to delete: > "))
				
				instance = Employee.Employee()
				self.showColumn()
				instance.getEmployee(id)
				answer = input("\nAre you sure? (y/n) > ")
				if answer is "y":
					instance.deleteEmployee(id)
				
					

			elif self.menuOption == "6":
			#InsertData()
				instance = Employee.Employee()
				Modified_Date = datetime.datetime.today().strftime('%Y-%m-%d')
				Employee_ID = input("\nPlease enter Employee_ID to add: > ")
				Login_ID =  input("Please enter Login_ID to add: > ")
				Department_ID = input("Please enter Department_ID to add: > ")
				Manager_ID = input("Please enter Manager_ID to add: > ")
				Title = input("Please enter Title to add: > ")
				BirthDate = input("Please enter BirthDate to add. The format has to be \"2017-01-01\": > ")
				MaritalStatus = input("Please enter MaritalStatus to add (Single: S/ Married: M): > ")
				HireDate = input("Please enter HireDate to add. The format has to be \"2017-01-01\": > ")
				VacationHours = '0'
				SickLeaveHours = '0'
				Gender = input("Please enter Gender to add. (Female: F, Male: M, Others: O): > ")
				
				instance.addEmployee(Employee_ID, Login_ID, Department_ID, Manager_ID, Title, BirthDate, MaritalStatus, HireDate, VacationHours, SickLeaveHours, str(Modified_Date), Gender)
				
				self.showColumn()
				instance.getAllEmployee()
				


			elif self.menuOption == "7":
				print("Bye")
				instance = Database.Database()
				con = instance.connection()
				instance.close_connection(con)
				

				break

ms = ManagementSystem()

