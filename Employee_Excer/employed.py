class Employee:
    def __init__(self,employee_name,employee_number):
        self.__employee_Name = employee_name
        self.__emplyee_Number =employee_number

    def get_employee_Name(self):
        return self.__employee_Name
    
    def get_emplyee_Number(self):
        return self.__emplyee_Number