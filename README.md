# QA-DevOps-Fundamental-Project- MCQ App:  
This repository contains my deliverable for the QA devops fundamental project. 

## Contents:
* [Project Brief](#Project-Brief)  
* [App Design](#App-Design)
* [CI Pipeline](#CI-Pipeline)  
* [Risk Assessment](#Risk-Assessment)
* [Testing](#Testing)
* [The App](#The-App)
* [Known Issues](#Known-Issues)
* [Future Work](#Future-Work)

## Project Brief:  
The brief for this project was to design and produce a web app of my choosing. The app needed to have CRUD (create, read, update and delete) functionality, needed to use the Flask micro-framework, and had to store information in a MySQL database comprised of a minimum of two tables sharing a one-to-many relationship. This structure is represented below:  
![app structure](https://github.com/agray998/QA-DevOps-Fundamental-Project/blob/main/figures/app%20diagram%20(1).png)  

## App Design:
I have chosen to build a multiple-choice question (MCQ) quiz app, which allows users to write questions and options (create functionality), view questions and options (read functionality), update questions and options (update functionality) and delete questions and options (delete functionality). The database for the MVP for this project comprises a Questions table and an Options table, with each question associated with multiple options (one-to-many relationship). The ERD for this MVP is shown below:  
![ERD](https://github.com/agray998/QA-DevOps-Fundamental-Project/blob/main/figures/ProjectMVPERD.png)  
Additional functionality was added on top of this MVP, specifically functionality to allow users to answer the questions added to the app and to view their score. An answers table and a results table were added to the database to facilitate this. The ERD for the project in its' current form is:  
![Current ERD](https://github.com/agray998/QA-DevOps-Fundamental-Project/blob/main/figures/ProjectERD.png)  
The goal for future iterations of this project will be to add categorisation of questions by topic via a quizzes table, and to make results specific to specific quizzes, a proposed ERD for this is:  
![Future ERD](https://github.com/agray998/QA-DevOps-Fundamental-Project/blob/main/figures/ProjectERDfuture.png)  

## CI Pipeline:  
In addition to the above requirements, the project required the implementation of several stages of a typical CI pipeline. These were project tracking, version control, development environment and build server. For project tracking Trello was used to create a project tracking board. Items were assigned story points, acceptance criteria and MoSCoW prioritisation, and moved from project backlog, to sprint backlog, to review and then complete as the project progressed. The state of the Trello board at the beginning of sprint one was:  
![trello](https://github.com/agray998/QA-DevOps-Fundamental-Project/blob/main/figures/trelloboard.png)  
The trello board can be accessed [here](https://trello.com/b/KMCaNgMA/fundamental-project). A burndown chart for this project was also produced:  
![burndown](https://github.com/agray998/QA-DevOps-Fundamental-Project/blob/main/figures/burndown.png)  

For version control, git was used, with the project repository hosted on github. Version control via git allows changes to the project to be made and committed whilst keeping the commit history for access to earlier versions. GitHub as a repository hosting service allows the repository to be stored away from the development environment, as well as providing webhooks, which send http POST requests to the build server to automate building and testing.  

The development environment used was a python3 virtual environment (venv) hosted on a virtual machine running Ubuntu 20.04. Python is used as Flask is a python-based framework. A venv allows pip installs to be performed and the app to be run without affecting any conflicting pip installs on the same machine.  

Jenkins was used as a build server, providing automation of building and testing. This automation is achieved by setting up a freestyle project which executes the test.sh script when it recieves a webhook from github upon pushing a commit. Jenkins is also used to run the app via gunicorn once testing is complete. Gunicorn is a WSGI server which allows multiple processes to run the app simultaneously. The full pipeline utilised in this project is:  
![CI Pipeline](https://github.com/agray998/QA-DevOps-Fundamental-Project/blob/main/figures/projCI.png)  

## Risk Assessment:
Prior to building the app, a risk assessment was undertaken to identify risks and propose measures to control these risks. These measures could then be implemented in the app. This initial risk assessment is shown below:   
![RA](https://github.com/agray998/QA-DevOps-Fundamental-Project/blob/main/figures/project%20RA.png)  
Some of the control measures implemented in the project as a result of the risk assessment are as follows:  
* User profiles were not implemented, as this would require sending some form of authentication over unsecured HTTP connection.  
* SQLAlchemy was used with Flask to prevent SQL commands being sent directly to the database.  
* Credentials stored as secret texts on Jenkins VM and exported as environment variables to avoid accidentally publishing confidential details.  

The likelihood and impact level (out of 5) of each risk identified were estimated before and after the implementation of control measures, to quantify the effect of implementing the measures.

## Testing:  
Testing the app was an essential part of the development process. Two types of testing were implemented:  
* Unit testing tests _units of functionality_ (i.e functions) within the app. Unit tests were written for create, read, update and delete functionality, to ensure that these worked.
* Integration testing tests the function of the app in an as-live environment, being able to simulate keyboard input and mouse clicks to ensure that these elements of the app function as intended. Integration tests were written for many of the forms employed in the app.  

As this is not a production app, tests such as security tests and performance tests were not part of the scope of this project; only testing for functionality was performed. As mentioned previously, these tests are automated using Jenkins via webhooks. A successful build, in which all tests passed, is shown below:  
![build](https://github.com/agray998/QA-DevOps-Fundamental-Project/blob/main/figures/tests%20run%2016-05.png)  
The coverage reports, showing what percentage of statements were included in the tests, were output as html files, which were archived post-build. The coverage report for the above build was:  
![cov](https://github.com/agray998/QA-DevOps-Fundamental-Project/blob/main/figures/covreport%2016-05.png)  
Showing 96% coverage overall. All tests must pass for a build to be successful, a single failed test marks the build overall as failed.

# The App:  
Upon navigating to the app the user is presented with the homepage:  
![home](https://github.com/agray998/QA-DevOps-Fundamental-Project/blob/main/figures/homepage.png)  
The nav bar provides links which allow users to add a question, view questions and take the quiz. To add a question, the user simply fills in the name of the question on the form:  
![add question](https://github.com/agray998/QA-DevOps-Fundamental-Project/blob/main/figures/addq.png)  
The user is then redirected to a page which allows them to add up to four options for the question. The view questions page displays a list of the questions which have been added so far, which are hyperlinked to allow the user to view, update and delete the associated options:  
![view questions](https://github.com/agray998/QA-DevOps-Fundamental-Project/blob/main/figures/viewqos.png)  
Users can also update and delete questions, the app is set up so that deleting a question also removes the associated options.  
![view questions](https://github.com/agray998/QA-DevOps-Fundamental-Project/blob/main/figures/viewqs.png)  
Finally, users can take the quiz by following the 'Take Quiz' link; answers are submitted via a form and, once all questions have been answered a score is calculated and the user can view the result. Upon returning to the home page the score is recorded for long-term statistics and the answers deleted, readying the app for the next time the user takes the quiz.

## Known Issues:
* There is nothing to stop two options for the same question being assigned the same letter
* Submitted answers are not cleared post-quiz unless the user clicks the 'return to home' link.

## Future Work:
In future sprints, in addition to fixing the issues identified above, I would like to add the additional functionality of question categorisation and a statistics page which provides a break-down of results over time by quiz. If the appropriate security measures were adhered to, future sprints could also reconsider adding user profiles which would allow users to view and write quizzes specific to them.
