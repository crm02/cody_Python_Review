#  2. ShiftSupervisor Class
#  In a particular factory, a shift supervisor is a salaried employee who supervises a shift. In
#  addition to a salary, the shift supervisor earns a yearly bonus when his or her shift meets
#  production goals. Write a ShiftSupervisor class that is a subclass of the Employee class
#  you created in Programming Exercise 1. The ShiftSupervisor class should keep a data
#  attribute for the annual salary, and a data attribute for the annual production bonus that
#  a shift supervisor has earned. Demonstrate the class by writing a program that uses a
#  ShiftSupervisor object.

from employed import Employee

class ShiftSupervisor(Employee):
    def __init__(self,employee_name,employee_id,annual_salary,annual_bonus):
        Employee.__init__(self,employee_name,employee_id)
        self.__annual_salary = annual_salary
        self.__annual_bonus = annual_bonus

    def set_annual_salary(self,)

