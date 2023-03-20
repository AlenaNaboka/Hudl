# Hudl
Technical Task
To cover by E2E tests implemented login functionality.

Description
For task implementation Python was used as automation language together with Selenium framework. 

# Scenarios to test
To the scenarios are included the following:
 - Successful login with valid data
 - Negative scenarios with invalid data (similar tests are united to the one and pytest parametrization is added)
 - Help Login functionality (user is able to use correct help links)
 - Go back functionality

What should be included from automation perspective:
 - Log in via organization link
 - Reset password functionally (with emails reader helpers and test email address)

What should be included into additional validation from manual perspective:
 - Remember me functionality (need to find out the requirements about lifetime of cookies and validate log out functionality after this period of time)

# Before you go

Please install on your local machine the following tech stack:
* Python3
* Chrome browser, the last version
* Python pip `python3 get-pip.py`

# How to spin up the project

1. Clone the repository via PyCharm UI or any other IDE. If you use console/terminal, execute the following command:
`git clone https://github.com/AlenaNaboka/Hudl.git`
2. In root folder "Hudl" create virtual environment using the following command:
`python3 -m venv venv`
3. Activate the venv using the command
`source venv/bin/activate`
4. Execute the following command to install all required libraries:
`pip install -r requirements.txt`
5. From Hudl/tests/E2E/tests folder run the command `pytest -v` to run all the tests in the folder
6. See the results in console
