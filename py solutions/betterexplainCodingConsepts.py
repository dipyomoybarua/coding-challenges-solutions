from typing import Optional
import datetime

class Person:
    def __init__(self, name: str, age: int, gender: str):
        """
        Initialize a Person object.

        Args:
            name (str): The person's name.
            age (int): The person's age.
            gender (str): The person's gender.
        """
        self.__private_info = f"This person's name is {name}"
        self._protected_info = f"This person is {age} years old"
        self.public_info = f"This person is a {gender}"

        self.name = name
        self.age = age
        self.gender = gender

    def greet(self) -> None:
        """
        The function `greet` prints a greeting message including the name attribute of the object it is
        called on.
        """
        """Print a greeting message."""
        print(f"Hello, my name is {self.name}.")

    def celebrate_birthday(self) -> None:
        """Increment age and print birthday message."""
        self.age += 1
        print(f"Happy birthday! You are now {self.age} years old.")

    def __str__(self) -> str:
        """
        The function returns a string representation of an object with attributes for name, age, and
        gender.
        :return: The `__str__` method is returning a string representation of an object that includes
        the object's name, age, and gender.
        """
        return f"{self.name}, {self.age} years old, {self.gender}"

    def get_private_info(self) -> str:
        """
        The function `get_private_info` returns the private information stored in the `__private_info`
        attribute.
        :return: The method `get_private_info` is returning the private information stored in the
        `__private_info` attribute of the object.
        """
        """Return private information."""
        return self.__private_info

    def set_protected_info(self, value: str) -> None:
        """
        The function `set_protected_info` sets a protected information attribute with the provided
        value.
        
        :param value: The `value` parameter in the `set_protected_info` method is a string type that
        represents the information you want to set as protected information
        :type value: str
        """
        """Set protected information."""
        self._protected_info = value

class Employee(Person):
    def __init__(self, 
                 name: str, 
                 age: int, 
                 gender: str, 
                 employee_id: str, 
                 department: str, 
                 job_title: str, 
                 salary: float, 
                 hire_date: str, 
                 performance_rating: Optional[float] = None):
        """
        Initialize an Employee object.

        Args:
            name (str): The employee's name.
            age (int): The employee's age.
            gender (str): The employee's gender.
            employee_id (str): Unique identifier for the employee.
            department (str): Department where the employee works.
            job_title (str): Employee's job title.
            salary (float): Employee's salary.
            hire_date (str): Date of hiring in YYYY-MM-DD format.
            performance_rating (Optional[float]): Employee's performance rating (default=None).
        """
        super().__init__(name, age, gender)
        self.employee_id = employee_id
        self.department = department
        self.job_title = job_title
        self.salary = salary
        self.hire_date = hire_date
        self.performance_rating = performance_rating
        self.__confidential_info = f"This employee has access level: Confidential"

    def work(self) -> None:
        """Print information about working."""
        print(f"{self.name} is working in the {self.department} department as a {self.job_title}.")

    def evaluate_performance(self, rating: float) -> None:
        """Update and print performance rating."""
        self.performance_rating = rating
        print(f"{self.name}'s performance rating has been updated to {rating}")

    def __str__(self) -> str:
        return f"{super().__str__()}, Employee ID: {self.employee_id}, Department: {self.department}, Job Title: {self.job_title}"

    def get_confidential_info(self) -> str:
        """Return confidential information."""
        return self.__confidential_info

def main() -> None:
    """
    Demonstrate usage of Person and Employee classes.
    """
    print("Demonstrating Person class:")
    person = Person("Dipyomoy Barua", 20, "Male")
    print(person)
    person.greet()
    person.celebrate_birthday()

    print("\nDemonstrating Employee class:")
    employee = Employee("Sporty", 20, "Female",
                        "E12345", "IT Department", "Software Engineer",
                        20000, "2019-01-01")
    
    print("\nEmployee details:")
    print(employee)
    employee.work()

    # Accessing private attribute through method
    print(f"\nPrivate attribute: {employee.get_private_info()}")

    # Accessing protected attribute
    print(f"Protected attribute: {employee._protected_info}")

    # Modifying protected attribute
    employee.set_protected_info("New protected value")
    print(f"Updated protected attribute: {employee._protected_info}")

    # Trying to access private attribute directly will raise an Exception
    try:
        # The line `print(employee.__private_info)` in the code is attempting to directly access the
        # private attribute `__private_info` of the `Employee` object `employee`.
        print(employee.__private_info)
    except Exception as e:
        print("Error: Cannot access private attribute directly")
        print(e)

    # Employee-specific operations
    print("\nEmployee-specific operations:")
    print(f"Salary: ${employee.salary:,}")
    print(f"Hire Date: {datetime.datetime.strptime(employee.hire_date, '%Y-%m-%d').strftime('%B %d, %Y')}")
    employee.evaluate_performance(4.5)
    print(f"Performance Rating: {employee.performance_rating}")

    # Accessing confidential info
    print(f"\nConfidential Info: {employee.get_confidential_info()}")

if __name__ == "__main__":
    main()
