# ✈️ Aircraft Maintenance Due Date Checker

A Python-based aviation maintenance tracking tool that reads maintenance records from a CSV file and automatically identifies overdue maintenance tasks.

This project demonstrates how aircraft maintenance planning concepts can be automated using Python, helping maintenance planners quickly identify pending maintenance actions that have exceeded their due dates.

---

## 📌 Overview

Aircraft maintenance activities are often tracked using spreadsheets and planning systems. This project simulates a simplified maintenance monitoring workflow by:

* Reading maintenance data from a CSV file
* Comparing maintenance due dates against the current date
* Identifying overdue maintenance tasks
* Displaying pending maintenance items that require attention
* Handling common file and data errors

The project is inspired by maintenance planning and CAMO (Continuing Airworthiness Management Organisation) workflows.

---

## 🚀 Features

### Maintenance Monitoring

* Reads maintenance data from CSV files
* Checks due dates automatically
* Detects overdue maintenance activities

### Status Filtering

* Displays only pending maintenance tasks
* Ignores completed maintenance records

### Error Handling

* Detects missing CSV files
* Detects missing required columns
* Prevents unexpected program crashes

### Aviation Application

* Simulates aircraft maintenance planning workflows
* Demonstrates basic maintenance compliance monitoring
* Provides a foundation for more advanced CAMO tools

---

## 🛠 Technologies Used

* Python 3
* CSV Module
* Datetime Module
* Exception Handling

---

## 📂 Expected CSV Format

The program expects a file named:

```text
maintenance.csv
```

Example:

| Aircraft | Task            | due_date   |
| -------- | --------------- | ---------- |
| A320     | brake check     | 26-05-2026 | 
| B747     | ENGINE NO.4 REPLACMENT| 15-05-2026 | 
| B777  | spoiler actuators | 23-05-2026 |

---

## 📊 Example Output

```text
Overdue maintenance tasks:

 Aircraft: A320
task: brake check
due_date: 26-05-2026
------------------------------
 Aircraft: B747
task: ENGINE NO.4 REPLACMENT
due_date: 15-05-2026
------------------------------
 Aircraft: B777
task: spoiler actuators
due_date: 23-05-2026
------------------------------
## 🎯 Learning Objectives

This project helped me learn:

* File handling in Python
* CSV data processing
* Date comparison techniques
* Exception handling
* Aviation maintenance workflow automation

---

## 🔮 Future Improvements

Planned enhancements include:

* Excel file support
* Pandas integration
* Fleet-wide maintenance monitoring
* Maintenance forecasting
* Aircraft utilization tracking
* Email alerts for overdue tasks
* Dashboard interface
* SQLite database integration

---

## ✈ Aviation Relevance

This project reflects concepts commonly found in:

* CAMO Operations
* Aircraft Maintenance Planning
* MRO Organizations
* Airworthiness Management
* Maintenance Compliance Monitoring

Although simplified for educational purposes, it demonstrates how maintenance due-date monitoring can be automated using Python.

---

## 🤖 AI Assistance Disclosure

This project was developed as part of my Python learning journey using GitHub Copilot assistance while exploring aviation maintenance planning concepts and CAMO-related workflows.

---

## 👨‍💻 Author

Mohammed Faraz Ahmed

Aeronautical Engineering Student

Aspiring CAMO & Airworthiness Professional
