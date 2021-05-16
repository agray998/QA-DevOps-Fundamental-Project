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
Jenkins was used as a CI server, providing automation of testing. This automation was achieved by setting up a freestyle project which executes the test.sh script when it recieves a webhook from github upon pushing a commit.  
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

