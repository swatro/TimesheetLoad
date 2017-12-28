[![Build Status](https://travis-ci.org/swatro/TimesheetLoad.svg?branch=master)](https://travis-ci.org/swatro/TimesheetLoad)

## Introduction
The purpose of this project is to learn about AWS Lambda.

## Deployment
Travis CI is handling the deployment to AWS lambda. Most of the values will not need to be changed even as the code evolves.
However the field below could change as the code changes.
* `module_name` : The file location of the AWS trigger function
* `handler_name` : The method name of the AWS trigger function
* `zip` : Directory of code that is uploaded. 


## Trigger: 
Current the lambda is triggered based on time using the cron expression `cron(0 0 ? * SAT *)`. This is equivalent to every SAT at
midnight UTC. 

## Things not done in code :(
* Permissions on user to allow deployment
* Trigger rule

## Todo List and Open Questions:
- [x] Build a hello world lamdba
- [x] Add automatic deploy for lambda
- [x] Add automatic trigger for lamdba based on time
- [ ] Add writing to file in Google (or maybe Amazon instead?)
- [ ] Can the trigger rule be done in code?