# Person and Request Management System

This Python program demonstrates the use of abstract classes and inheritance to create a simple system for managing people (employees, team leads, and admins) and requests within an organization.

## Abstract Class -> Person Creation

The code defines an abstract class `Person` with several abstract methods:

- `getFullName`: Get the full name of a person.
- `addRequest`: Add a request.
- `checkRequest`: Check a request.
- `addUser`: Add a user.

### Employee Class

The `Employee` class inherits from `Person` and represents an employee in the organization. It includes methods for getting and setting employee attributes and implements the abstract methods.

### TeamLead Class

The `TeamLead` class, like `Employee`, inherits from `Person` and represents a team lead. It includes methods for managing team members and implements the abstract methods.

### Admin Class

The `Admin` class, also inheriting from `Person`, represents an admin user and implements the abstract methods.

### Request Class

The `Request` class is used to create request objects with attributes like name, requester, data requested, and status. It includes methods to close, cancel, or update requests.

## Usage

In the `if __name__ == '__main__':` block at the end of the code, several instances of employees, team leads, and admins are created, along with request objects. Assertions are used to check the correctness of various methods.

## Getting Started

To run the code, make sure you have Python installed on your system. Simply execute the script using:

```bash
python your_script_name.py

```python
    # Create an employee
employee1 = Employee("John", "Doe", "djohn@mail.com", "Marketing")

# Check their full name
assert employee1.getFullName() == "John Doe", "Full name should be John Doe"

# Log in
assert employee1.login() == "djohn@mail.com has logged in"

# Add a request
assert employee1.addRequest() == "Request has been added"

# Log out
assert employee1.logout() == "djohn@mail.com has logged out"
```