# Employee Payroll System App Documentation
This is a copy of an original document, which is held by myself; the original document goes into further detail.

## Contents
- [Introduction](#introduction)
- [System Requirements](#system-requirements)
- [Installation and Setup](#installation-and-setup)
- [User Guide](#user-guide)
- [Technical Specifications](#technical-specifications)
- [Release Notes](#release-notes)
- [Troubleshooting and Support](#troubleshooting-and-support)
- [Appendix](#appendix)

## Introduction

### Overview of the Software
The **Employee Payroll System App** is a sophisticated, integrated solution designed for efficient payroll management. This application addresses multiple payroll processing aspects, aiming to streamline operations, enhance accuracy, and ensure compliance with tax and labor regulations. It offers a centralized platform for effective management, covering key payroll functions such as computation, record-keeping, compliance, and reporting.

#### Core Functionalities:
- **Data Management:** Centralizes and manages payroll data.
- **Payroll Calculation:** Calculates wages, bonuses, taxes, and more.
- **Compliance and Reporting:** Generates essential reports and adheres to tax and labor laws.
- **Employee Information Handling:** Manages detailed employee information.
- **Search and Filter Capabilities:** Advanced search and filtering for payroll data.
- **Wage Slip Display:** Displays and allows printing/saving of wage slips.
- **Data Visualisation and Analysis (Future Enhancement):** Envisioned for insightful payroll data visualizations.

### Purpose and Audience of the Documentation
This documentation is for payroll administrators, HR professionals, IT support staff, software engineers, business analysts, and managers in small startups to large enterprises.

### Scope of the Documentation
Covers the architecture, design, functionalities, system requirements, installation, user interface, operations, and advanced features of the Employee Payroll System App.

## System Requirements

### Minimum Hardware Requirements
- **Processor:** 1.0 GHz Single-Core.
- **Operating System:** Windows 11/10/8.1, macOS 10.15+, Unix systems (with variances).
- **Memory:** 2GB RAM.
- **Storage:** 200MB free space.
- **Network:** Internet connection recommended.

### Recommended Hardware Requirements
- **Processor:** 2.0 GHz Dual-Core or better.
- **Memory:** 4GB RAM or more.
- **Storage:** 1GB free space or more.
- **Network:** Reliable internet connection.

## Installation and Setup

### Installation Requirements
- **Python 3:** Download and install the latest version.
- **Pandas Library:** Install using `pip install pandas`.
- **Operating System Dependencies:** Specific dependencies for Windows and macOS.

### Data Requirements
Data file in CSV format placed within the "ELATT Coursework" directory.

### User Proficiency
Assumes fundamental understanding of software installation and operation.

### Beta Version Notice
The program is in beta phase and does not require a full installation.

## User Guide

### Getting Started
The application features a command-line interface (CLI) operated through an IDE like Visual Studio Code.

### How to Perform Common Tasks
- Launching, navigating, and interacting with the application.
- Functionality insights and data file requirements.

## Technical Specifications

### Architecture and Design
Focus on modularity and separation of concerns for a robust and maintainable codebase.

### System Components and Modules
- **Data Management Module**
- **Payroll Calculation Module**
- **User Interface Module**
- **Compliance and Reporting Module (Future)**
- **Search and Filter Module**

### Review of Appendices and Source Code
Detailed understanding of the application's structure and functionality.

## Release Notes

### List of New Features and Improvements
- Enhanced data sorting and filtering.
- Advanced employee search.
- Improved data output options.
- Palindrome check feature.
- Sorted department and business unit reports.
- Wage slip generation.

### Known Issues and Limitations
- Limited tax and deduction processing.
- Dependency on specific data format.
- Limited visualisation capabilities.
- Manual tax code input.

### Compatibility with Previous Versions
Designed to be compatible with standard payroll data formats.

### Upgrade Instructions
Updating software, data file compatibility, and review documentation.

## Troubleshooting and Support

### Common Error Messages and Resolutions
Guidance on resolving common errors like file not found, invalid input, and data format errors.

### Contact Information for Technical Support
Email and phone contact details for support.

### How to Report Bugs and Provide Feedback
Procedure for reporting bugs and sharing feedback.

### Development Insights
Insights into the development process, client interaction, and methodologies used.

## Appendix

### Repository Schema
Layout and structure of the project repository.
<img width="472" alt="image" src="https://github.com/SMCallan/PAYROLL_SYSTEM_DEMO/assets/126923185/d42f1750-2dc9-4ed0-870b-5ce562451196">

### Source Code
Available in 'main' and 'Pd_lib'

### Data Format


Data Formatting Guidelines for the Employee Payroll System App

To ensure the Employee Payroll System App functions correctly, it's crucial that your data is formatted properly. The application expects data in a CSV (Comma-Separated Values) format, with specific column headers and data types. Below are the guidelines for formatting your data:
	Required Columns: Your data file must include the following columns in the exact order listed:
	EEID (Employee ID): A unique identifier for each employee.
	Full Name: The employee's full name.
	Job Title: The employee's job title.
	Department: The department where the employee works.
	Business Unit: The business unit to which the employee belongs.
	Gender: The gender of the employee.
	Ethnicity: The employee's ethnicity.
	Age: The age of the employee.
	Hire Date: The date the employee was hired (format: DD/MM/YYYY).
	Annual Salary: The employee's annual salary.
	Bonus %: The percentage of the bonus (if applicable).
	Country: The country where the employee is located.
	City: The city where the employee is located.
	Exit Date: The date the employee exited the company (if applicable, format: DD/MM/YYYY).
	File Naming and Placement:

	Name your file according to the expected format, which is example.csv.
	Place the CSV file in the data folder within the project's repository. This is crucial for the application to locate and read the data correctly.
 
	Formatting Tips:
	Ensure there are no extra spaces before or after the commas in your CSV file.
	Text fields should be enclosed in quotes if they contain commas.
	Check for consistent data types in each column (e.g., all entries in the 'Age' column should be numeric).


By following these formatting guidelines, you ensure that the Employee Payroll System App can successfully read and process your data, enabling efficient and accurate payroll management.
