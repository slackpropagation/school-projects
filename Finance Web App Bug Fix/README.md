# Financial Year Selection Bug Fix – Endothon Finance Web App

This repository contains my completed project for fixing a major logic bug in the **Endothon Finance** loan web app.  
The project focuses on correcting the way the application selects fiscal years when businesses apply for loans.  

**Purpose of the Project:**  
The existing app incorrectly pulled the first five fiscal years after a business started, even if that data was outdated. The goal of this project was to update the system so that it selects the five most recent *completed* fiscal years instead — ensuring that loan profiles reflect up-to-date financial information.  

**Real-World Importance:**  
For financial institutions, using the most current financial data is critical in assessing loan risk and making approval decisions. This project simulates a real-world bug fix scenario that teaches skills like backend logic correction, system constraints handling, user experience optimization, and iterative Agile development. Students completing this project practice modular code design, edge case handling, version control, and unit testing with real business rules in mind.

## Project Summary

- Identified and fixed logic that incorrectly pulled the first five fiscal years instead of the latest five.
- Implemented forecast year logic for businesses younger than five years.
- Developed unit tests to ensure robust handling of various business scenarios (new vs. old businesses).
- Used Agile methodology to build, test, and validate the fix iteratively.
- Delivered an updated backend that improves data relevance for loan decision-making without impacting user experience.

## Key Components

- **Fiscal Year Calculation Function:**  
  Calculates the five fiscal years needed based on the business start year and the current year, excluding the current year.
  
- **Forecast Logic Handler:**  
  Detects when businesses have less than five completed years and calculates how many projected (future) years are needed to complete the set.

- **Unit Tests:**  
  Comprehensive tests to ensure the functionality handles all expected and edge-case inputs correctly.

- **Internal Documentation:**  
  Clear comments and small documentation for future maintenance and scalability.

- **Development Tools Used:**  
  - Java for backend logic
  - IntelliJ IDEA for development and debugging
  - JUnit for testing
  - Git and GitHub for version control

## Algorithms Used

- **Conditional Year Selection:**  
  Based on comparing the business start year to the current system year, dynamically generates the needed fiscal year range.

- **Forecast Year Calculation:**  
  When less than five years are available, determines how many additional years must be forecasted and fills them in accordingly.

- **Validation Checks:**  
  Ensures no invalid future-dated years are processed and only valid numeric years are accepted.

## Task Requirements Covered

- **Problem Statement Clearly Identified:**  
  Fixes outdated financial year selection in the loan application process.

- **Functional Requirements Met:**  
  Always retrieve the most recent 5 completed years or a combination of completed + forecasted years.

- **Non-Functional Requirements Met:**  
  Year fields load in under 2 seconds and behave consistently across Chrome, Firefox, and Safari.

- **Scope Clearly Defined:**  
  Focused only on fixing backend fiscal year logic, not vendor APIs or frontend redesign.

- **Full QA Coverage Provided:**  
  System tests for old/new businesses, performance tests for loading speed, and compatibility tests across browsers.

## What I Learned

- How to translate real-world business requirements into technical software fixes.
- How to design modular, maintainable backend functions that handle both typical and edge case scenarios.
- How to plan and execute unit testing to validate business-critical logic.
- How Agile development practices help rapidly test and validate software fixes while minimizing bugs.
- The importance of clear in-scope and out-of-scope definitions in software project planning.
- How even small backend bugs can significantly impact business outcomes if not properly caught and fixed.

---
