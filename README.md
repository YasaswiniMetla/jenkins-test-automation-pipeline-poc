# Jenkins Pipeline POC for Test Automation

A reusable Jenkins pipeline framework for centralized automated test execution.

## Pipeline flow

GitHub → Jenkins → Branch Validation → Environment Setup → Test Selection → Test Execution → Reports → Notification

## Features

- Parameterized test execution
- Branch validation
- Smoke/regression selection
- Retry handling for transient failures
- JUnit report publishing
- Archived test artifacts
- Reusable execution structure
- Centralized pipeline visibility

## Parameters

- `TEST_SUITE`: smoke or regression
- `TEST_ENV`: dev, qa, or staging
- `RETRY_COUNT`: retry count for transient failures

## Run locally

```bash
pip install -r requirements.txt
pytest -m smoke
pytest -m regression
```

## Why this is different from the Quality Gate project

This project focuses on **test execution orchestration, reusable automation, environment selection, and retry handling**.

The Quality Gate project focuses on **release controls, quality enforcement, build verification, and deployment readiness**.

Together, the projects demonstrate two complementary CI/CD capabilities:
- **Test Automation Pipeline:** executing and orchestrating automated tests
- **Quality Gate Pipeline:** validating whether a build is ready for release
<img width="2880" height="1512" alt="image" src="https://github.com/user-attachments/assets/4b2f60bb-fdee-47b6-a916-cdd8614164d6" />

