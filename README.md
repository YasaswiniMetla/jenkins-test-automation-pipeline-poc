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

This project focuses on **test execution orchestration and framework reusability**.

The Quality Gate project focuses on **release controls and deployment readiness**.
