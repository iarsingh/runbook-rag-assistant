# Runbook RAG Assistant: process flows

## Domain request

Endpoint: `POST /ask`. Stages summarize [src/runbookragas/answer.py](../src/runbookragas/answer.py). This is in-process Python, not a hosted model or production apply.

```mermaid
flowchart TD
  A["POST /ask"] --> B{"Valid input?"}
  B -->|"No"| E["HTTP 422"]
  B -->|"Yes: Question overlap >= 2"| C["Domain function in answer.py"]
  C --> O["extractive runbook citation or unanswered"]
  O --> X["No production side effect"]
```

See [INTERVIEW_QA.md](../INTERVIEW_QA.md) for fixture walkthroughs and [PROJECT_ARCHITECTURE.md](../PROJECT_ARCHITECTURE.md) for the component map.
