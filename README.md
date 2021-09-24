# Workload-and-Skill-Level-based-Automated-Scheduling
A web application for scheduling of employees of manufacturing industries based on skill level of employee and criticality index of machine for monthly production plan.

## Problem Statement: 
To develop an application for automated scheduling of manpower based on the skill matrix and load of the machine.

## High Level System Solution
The proposed system solution of workload and skill level based scheduling consists of 4 modules in design.
<br/>
![alt text](https://github.com/BasavarajMS11/Workload-and-Skill-Level-based-Automated-Scheduling/blob/master/Images/systemmodel.JPG?raw=true)
<br/>
1. Requirement Analysis and Data Pre-processing
2. Design (UI & Scheduling Algorithm)
3. Testing (WebDev)
4. Deploment (PaaS-Heroku)

## Requirement Analysis
The requirements are considered from the perspective of authorized user. Authorized user is the dispatcher who schedules the work load to the employees based on
constraints and has all the privileges to manipulate the data. Whereas employee can only view the data. In further sections we discuss the functional and non-functional requirements indicating client's expectations.
Link: https://drive.google.com/file/d/1rHB682Rx6eFy-pqZHnEF5t0rv9K_z9p-/view?usp=sharing

## Data Pre-processing
Data pre-processing phase consists of process transforming the raw data to the required format. Different techniques are used in data reprocessing raw data collected is in Excel format which in turn has several sheets in it. Broadly there are three Excel sheets: Manning review, Skill Matrix and Machine criticality index.
1) Manning review: This consists of several sheets in it which provide information about Workload and Skill Level based Automated Scheduling of Operator to Machine cell wise production schedule. It also consists of the important information required to calculate the total manpower, capacity for the month etc.
![alt text](https://github.com/BasavarajMS11/Workload-and-Skill-Level-based-Automated-Scheduling/blob/master/Images/preprocess3plan.JPG?raw=true)
<br/>

2) Skill matrix: This consists of employee details such as name, experience, date of join and the skill level for each machine. These details are provided for each cell. There are 19 cells in total.
![alt text](https://github.com/BasavarajMS11/Workload-and-Skill-Level-based-Automated-Scheduling/blob/master/Images/preprocess1emp.JPG?raw=true)
<br/>

3) Machine criticality index: This consists of cell wise machine details along the required skill level to operate it.
![alt text](https://github.com/BasavarajMS11/Workload-and-Skill-Level-based-Automated-Scheduling/blob/master/Images/preprocess2machine.JPG?raw=true)
<br/>



## Design Principles for UI design
1. MVC - Model View Controller architecture diagram

![alt text](https://github.com/BasavarajMS11/Workload-and-Skill-Level-based-Automated-Scheduling/blob/master/Images/designprinciple1.JPG?raw=true)



2. Client Server architecture diagram

![alt text](https://github.com/BasavarajMS11/Workload-and-Skill-Level-based-Automated-Scheduling/blob/master/Images/designprinciple2.JPG?raw=true)


## Scheduling Algorithm design

![alt text](https://github.com/BasavarajMS11/Workload-and-Skill-Level-based-Automated-Scheduling/blob/master/Images/newflowchart.JPG?raw=true)

## UI Pages
### Home
![alt text](https://github.com/BasavarajMS11/Workload-and-Skill-Level-based-Automated-Scheduling/blob/master/Images/home1.JPG?raw=true)
<br/>

### Home - Once logged in
![alt text](https://github.com/BasavarajMS11/Workload-and-Skill-Level-based-Automated-Scheduling/blob/master/Images/home2.JPG?raw=true)
<br/>


