# Defining the Person class

class Person:
    #Initializing attributes 
    
    def __init__(self, name, age, gender):
        # Private attribute
        self.__private_attribute = f"This person's name is {name}"
        
        # Protected attribute
        self._protected_attribute = f"This person is {age} years old"
        
        # Public attribute
        self.public_attribute = f"This person is a {gender}"
        
        # Regular attributes
        self.name = name
        self.age = age
        self.gender = gender
        
        # Defining methods for Person class

    def greet(self):
        print(f"Hello, my name is {self.name}.")

    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy birthday:- You are now {self.age} years old.")

    def __str__(self):
        return f"{self.name}, {self.age} years old, {self.gender}"
    
    # Accessor methods for private and protected attributes

    def get_private_attribute(self):
        return self.__private_attribute

    def set_protected_attribute(self, value):
        self._protected_attribute = value
        
        
        # Defining the Employee class

class Employee(Person):
    def __init__(self, name, age, gender, employee_id, department, job_title, salary, hire_date, performance_rating=None):
        # Calling parent class constructor
        super().__init__(name, age, gender)
        
        # Additional attributes specific to Employee class
        
        self.employee_id = employee_id
        self.department = department
        self.job_title = job_title
        self.salary = salary
        self.hire_date = hire_date
        self.performance_rating = performance_rating

    # Private attribute
        self.__confidential_info = f"This employee has access level: Confidential"

    def work(self):
        print(f"{self.name} is working in the {self.department} department as a {self.job_title}.")

    def evaluate_performance(self, rating):
        self.performance_rating = rating
        print(f"{self.name}'s performance rating has been updated to {rating}")

    def __str__(self):
        return f"{super().__str__()}, Employee ID: {self.employee_id}, Department: {self.department}, Job Title: {self.job_title}"

    def get_confidential_info(self):
        return self.__confidential_info

# Function to demonstrate usage of Person and Employee classes
def main():
    print("Demonstrating Person class:")
    person = Person("Dipyomoy Barua", 20, "Male")
    print(person)
    person.greet()
    person.celebrate_birthday()

    print("\n Demonstrating Employee class:")
    employee = Employee("Sporty", 20, "Female",
        "E12345",
        "IT Department",
        "Software Engineer",
        20000,
        "2019-01-01")
    
    print("This is employee details that is being declared above:- ", employee)
    employee.work()
    
    # Accessing private attribute through method
    print(f"\n Private attribute: {employee.get_private_attribute()}")
    
    # Accessing protected attribute
    print(f"Protected attribute: {employee._protected_attribute}")
    
    # Modifying protected attribute
    employee.set_protected_attribute("New protected value")
    print(f"Updated protected attribute: {employee._protected_attribute}")
    
    # Trying to access private attribute directly will raise an Exception
    try:
        print(employee.__private_attribute)
    except Exception as e:
        print("Error: Cannot access private attribute directly",e)

    # Employee-specific operations
    print("\n Employee-specific operations:")
    print(f"Salary: ${employee.salary:,}")
    print(f"Hire Date: {employee.hire_date}")
    employee.evaluate_performance(4.5)
    print(f"Performance Rating: {employee.performance_rating}")

    # Accessing confidential info
    print(f"\n Confidential Info: {employee.get_confidential_info()}")
        
        # Running the script
if __name__ == "__main__":
    main()
    
    
    