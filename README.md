# RequirementIQ

RequirementIQ is an AI-powered QA Reasoning Agent that transforms software requirements and user stories into structured Quality Assurance (QA) assets.

The application helps testers, Business Analysts, Product Owners, and development teams identify test scenarios, requirement gaps, risks, and validation opportunities before development begins.

Built as part of the Microsoft Agents League Hackathon under the Reasoning Agents challenge track.

---

## Problem Statement

Creating comprehensive test cases from requirements is often a manual and time-consuming process.

Teams frequently miss:

* Edge Cases
* Negative Test Cases
* Requirement Gaps
* Risk Areas
* Test Data Requirements

RequirementIQ helps improve software quality by automatically analyzing requirements and generating structured QA recommendations.

---

## Features

### Requirement Analysis

The agent analyzes software requirements and user stories.

### Functional Test Cases

Generates functional test scenarios based on requirement type.

### Edge Case Identification

Highlights uncommon scenarios that may impact system behavior.

### Negative Test Cases

Identifies invalid actions and failure conditions.

### Missing Requirement Detection

Generates questions that help clarify ambiguous requirements.

### Test Data Suggestions

Recommends useful test data for validation.

### Risk Analysis

Assigns risk levels and explains potential impact areas.

### Supported Requirement Types

* Password Reset
* Login
* Registration / Sign Up
* Shopping Cart
* Generic Requirements

---

## Example

### Input

As a customer, I want to reset my password using email so that I can regain access to my account.

### Output

* Requirement Category
* Priority
* Risk Level
* Functional Test Cases
* Edge Cases
* Negative Test Cases
* Missing Requirements
* Test Data Suggestions

---

## Architecture

User

↓

Streamlit User Interface (UI)

↓

RequirementIQ Reasoning Engine

↓

Requirement Classification

↓

QA Analysis Generation

↓

Structured Output

---

## Technology Stack

### Frontend

* Streamlit

### Backend

* Python

### Version Control

* Git
* GitHub

### AI Reasoning Logic

* Rule-Based Requirement Classification
* Risk Analysis
* QA Knowledge Patterns

---

## Project Structure

```text
AI-TestCase-Agent/

├── app/
│   ├── generator.py
│   └── prompts.py
│
├── frontend/
│   └── streamlit_app.py
│
├── README.md
├── .gitignore
└── requirements.txt
```

---

## How To Run

### Clone Repository

```bash
git clone https://github.com/kurmapumadhuri2209/AI-TestCase-Agent.git
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

```powershell
.\venv\Scripts\Activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run frontend/streamlit_app.py
```

---

## Future Enhancements

* Microsoft Foundry Integration
* Additional Requirement Categories
* PDF Export
* Excel Export
* Advanced Risk Analysis
* Requirement Quality Scoring
* AI-Based Requirement Gap Detection

---

## Hackathon Information

Challenge Track:

Reasoning Agents

Project Name:

RequirementIQ

Hackathon:

Microsoft Agents League Hackathon 2026

---

## Author

Madhuri Kurmapu
