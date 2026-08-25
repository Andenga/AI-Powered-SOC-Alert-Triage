# Alert Triage Eval

An AI-assisted SOC alert triage tool — with an honest, documented account of where it fails and why, not just where it works.

## Why this exists

Most "AI for security" portfolio projects show the happy path: the model classified the alerts, the demo works, done. That's not how AI-assisted tools behave in a real SOC, and pretending otherwise is a red flag to anyone who's actually worked in one. This project treats the *failure analysis* as the main deliverable, not an afterthought — because knowing where an automated system breaks is what determines whether an analyst can trust it.

## What it does

- Ingests a set of security alerts (SIEM/EDR-style: source, severity, MITRE ATT&CK mapping, raw log context)
- Uses an LLM/ML model to triage each alert: prioritize, classify as likely true/false positive, and generate a suggested next action
- Compares model output against ground-truth labels
- Produces a **failure analysis report**: false positives, false negatives, and the patterns behind each

## Dataset

*(Fill in what you actually used, e.g.)*
Alerts modeled on [dataset name / source], structured to resemble realistic SIEM/EDR alert schemas with fields for severity, source, MITRE ATT&CK technique, and analyst-labeled ground truth (true positive / false positive / needs investigation).

## Triage pipeline

```
alerts/           # Raw + labeled alert data
triage/           # Model inference: prioritization + classification
eval/             # Scoring against ground truth (precision, recall, confusion matrix)
failure-analysis/ # Documented breakdown of where and why triage failed
```

## Sample failure analysis

| Alert pattern | Model prediction | Ground truth | Why it failed |
|---|---|---|---|
| Multiple failed logins, off-hours, VPN source | Low priority | True positive (credential stuffing) | Model underweighted time-of-day as a signal |
| Single PowerShell execution, signed binary | High priority | False positive (scheduled admin task) | Model over-indexed on "PowerShell" keyword without execution context |

*(Replace with your actual results — this table is the core value of the project.)*

## Metrics

- Precision / recall / F1 on triage classification
- False negative rate on high-severity ground-truth alerts (the metric that matters most operationally — a missed true positive is far more costly than a false alarm)
- Breakdown of failure modes by alert type

## Getting started

```bash
git clone https://github.com/<your-username>/alert-triage-eval.git
cd alert-triage-eval
pip install -r requirements.txt
python triage.py --input alerts/sample_alerts.json
python evaluate.py --predictions output/predictions.json --labels alerts/ground_truth.json
```

## What I'd add next

- Human-in-the-loop feedback loop to retrain/tune on analyst corrections
- Confidence scoring so low-confidence triage decisions are flagged for manual review instead of auto-actioned

## Limitations

This is an evaluation of an AI-assisted triage *approach*, not a production-ready SOC tool. Results are specific to the dataset used and should not be read as a general claim about model performance on live alert streams.

## License

MIT
