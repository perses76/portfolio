# Ivysaur

 - **Date:** November, 2016

Question/Answer education application. My resposibility was to provide backend API for iOS application.

## Technologies
Flask, PostgreSql, SqlAlchemy

## Challenges

Requirements change very often and although the architecture is quite simple (see below), 
it was chalange to cover all code  with tests and provide required flexibility.
I tried different tests: from simple method to complex test case with input and output data fabrics.

The application has simple architecture with 4 Layers:
 1. Views
 1. Managers
 1. Repo
 1. SqlAlchemy models and queries
 
## Test workflow
 
 1. Create input test data
 2. Run test and return result (result can be dict or strong type object)
 3. Create expected data
 4. assert Result vs Expected

## General Test Case Class Diagram
![General Test Case Class Diagram](testcase_class_diagram.png)

## Other files:
 * [General Test Case Class Diagram](testcase_workflow.png)
