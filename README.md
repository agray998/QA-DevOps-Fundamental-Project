# QA-DevOps-Fundamental-Project- MCQ App
This repository contains my deliverable for the QA devops fundamental project.  

## Project Brief  
The brief for this project was to design and produce a web app of my choosing. The app needed to have CRUD (create, read, update and delete) functionality, needed to use the Flask micro-framework, and had to store information in a MySQL database comprised of a minimum of two tables sharing a one-to-many relationship. This structure is represented below:
img here  
I chose to build a multiple-choice question (MCQ) quiz app, which allows users to write questions and options (create functionality), view questions and options (read functionality), update questions and options (update functionality) and delete questions and options (delete functionality). The database for the MVP for this project comprises a Questions table and an Options table, with each question associated with multiple options (one-to-many relationship). The ERD for this MVP is shown below:  
![ERD](https://github.com/agray998/QA-DevOps-Fundamental-Project/blob/main/figures/ProjectmvpERD.png)  

## CI Pipeline  
In addition to the above requirements, the project required the implementation of several stages of a typical CI pipeline. These were project tracking, version control, development environment and CI server. For project tracking Trello was used to create a project tracking board. Items were assigned story points, acceptance criteria and MoSCoW prioritisation, and moved from project backlog, to sprint backlog, to review and then complete as the project progressed. The state of the Trello board at the beginning of sprint one was:  
img here  
The trello board can be accessed [here](https://trello.com/b/KMCaNgMA/fundamental-project).  
A burndown chart for this project was also produced:  
img here  
For version control, git was used, with the project repository hosted on github. The development environment used was a python3 virtual environment (venv) hosted on a virtual machine running Ubuntu 20.04.  
Jenkins was used as a CI server, providing automation of building and testing. This automation was achieved by setting up a freestyle project which executes the test.sh script when it recieves a webhook from github upon pushing a commit.  
The full pipeline utilised in this project was:  
img here  

## Risk Assessment
Prior to building the app, a risk assessment was undertaken to identify risks and propose measures to control these risks. These measures could then be implemented in the app. This initial risk assessment is shown below:   
![RA](https://github.com/agray998/QA-DevOps-Fundamental-Project/blob/main/figures/project%20ra%2011-05.png)  
The key for the probability and impact ratings is:  
![key](https://github.com/agray998/QA-DevOps-Fundamental-Project/blob/main/figures/project%20ra%20key.png)  
Some of the control measures implemented in the project as a result of this risk assessment were as follows:  
* User profiles were not implemented, as this would require sending some form of authentication over unsecured HTTP connection.  
* SQLAlchemy was used with Flask to prevent SQL commands being sent directly to the database.  

## Testing  
Testing the app was an essential part of the development process. Two types of testing were implemented:  
* Unit testing tests _units of functionality_ (i.e functions) within the app. Unit tests were written for create, read, update and delete functionality, to ensure that these worked.
* Integration testing tests the function of the app in an as-live environment, being able to simulate keyboard input and mouse clicks to ensure that these elements of the app function as intended. Integration tests were written for many of the forms employed in the app.  
Tests such as security tests and performance tests were not part of the scope of this project, only testing for functionality was performed. As mentioned previously, these tests were automated using Jenkins using webhooks. A successful build, in which all tests passed, is shown below:  
img here  
The coverage reports were output as html files, which were archived post-build. The coverage report for the above build was:  
img here  
Showing 96% coverage overall. All tests must pass for a build to be successful, a single failed test marks the build overall as failed:  
img here  

