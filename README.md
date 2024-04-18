# README for 0x02. AirBnB Clone - MySQL

## Project Overview

This project is part of the backend module for creating an AirBnB clone using Python and MySQL. It incorporates Object-Oriented Programming (OOP) and utilizes an ORM (SQLAlchemy) to manage MySQL operations. This project focuses on integrating SQL database storage into the existing file storage system, allowing switching between these storage types seamlessly using environment variables.

### Team Members

- Joshua Baka
- Tom Nyabuto

## Project Timeline

- **Start Date**: April 12, 2024, 6:00 AM
- **End Date**: April 18, 2024, 6:00 AM
- **Checker Release**: April 13, 2024, 6:00 PM
- **Auto-review Deadline**: April 18, 2024, 6:00 AM

## Environment Variables

To manage different configurations and environments:

- `HBNB_ENV`: Running environment ("dev", "test", "production" soon)
- `HBNB_MYSQL_USER`: Username for MySQL
- `HBNB_MYSQL_PWD`: Password for MySQL
- `HBNB_MYSQL_HOST`: Hostname for MySQL
- `HBNB_MYSQL_DB`: Database name for MySQL
- `HBNB_TYPE_STORAGE`: Storage type ("file" using FileStorage or "db" using DBStorage)

## Resources

**Reading Materials:**
- Python cmd module
- Python packages concept
- Python unittest module
- SQL, ORM, and SQLAlchemy tutorials
- MySQL user and permissions management

## Learning Objectives

By the end of this project, you should be able to:

- Implement unit testing in large projects.
- Use *args and **kwargs effectively.
- Handle named arguments in functions.
- Create and manage MySQL databases and users.
- Explain and implement ORM.
- Map Python classes to MySQL tables.
- Manage different storage engines within the same codebase.
- Utilize environment variables in Python projects.

## Requirements

### Python Scripts

- Use vi, vim, or emacs editors.
- Run on Ubuntu 20.04 LTS using Python 3.8.5.
- Adhere to PEP8/pycodestyle (version 2.8.*).
- Include appropriate documentation for modules, classes, and functions.
- Ensure all scripts are executable and well-documented.

### Python Unit Tests

- Place test files in a `tests` folder.
- Use the Python `unittest` module.
- Maintain the same project structure in the `tests` folder.
- Execute tests using `python3 -m unittest discover tests`.

### SQL Scripts

- Use MySQL 8.0 on Ubuntu 20.04 LTS.
- Execute with SQLAlchemy version 1.4.x.
- Include comments and adhere to SQL best practices.

### GitHub

- Maintain a single repository per group. Avoid duplicating repositories to prevent penalties.

## Plagiarism Warning

All solutions must be original. Plagiarism is strictly prohibited and will result in disqualification from the program.
