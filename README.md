# Data Engineering Coding Challenge
Hi, thank you for your time in solving the coding challenge. The goal is to see how your approach to problem-solving, and how you structure your code and hand it over to the team for review.

You can solve any one of the following problem statements. This README describes evaluation criteria, problem statements, and also some of the choices which you might have to make. If you need any further information, please reach out we are happy to help.

## Evaluation Criteria
- Code structure, and README instructions to review and run code
- Basic engineering principles
- Testing strategies

## Problem Statement - 1 (Anonymize customer information)
Imagine you are working on a project where you have to process customer data and generate insights. Considering this data has customer information and to generate insights, multiple teams will be using this data. To ensure we handle customer information with care, and not make it visible to everyone on the team one requirement is to anonymize customer information before it's loaded into the warehouse for insights generation.

- You will get this data in CSV files which will have customer personal information like first_name, last_name, address, date_of_birth
- Write code to generate a CSV file containing first_name, last_name, address, date_of_birth
- Load generated CSV in the previous step, anonymize data, and output anonymized data to a different file
- Columns to anonymise are first_name, last_name and address

## Choices
- You can use any language or any platform
- You can use any package or library unless specified in coding challenge
- Bonus points if you bundle your code using Docker(Dockerfile) that can be used to run the code
- You can share code either using Github, bitbucket, or zip in the email
- We are not expecting to enter data on command prompt, you can use any faker library to generate mock data
- Include a README file describing how we can run and test
