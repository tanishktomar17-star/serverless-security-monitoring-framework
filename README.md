# Serverless Security Monitoring Framework (SSMF) — Phase III Prototype

**Team:** Tanishk Tomar, Sameer Chodhary, Raj Tiwari, Vickey Raj  
**Project guide:** Bipin Bharti · **Institution:** IILM University, Greater Noida  
**Target design:** AWS serverless stack, Python 3.12, AWS SAM/CloudFormation.

## Included
- Canonical event normalization.
- Explainable rules for failed/unauthorized access, sensitive IAM actions, credential-exposure markers, invocation spikes and error bursts.
- Risk scoring, local SQLite persistence and an interactive dashboard.
- Manual JSON event ingestion, synthetic demo data, Lambda handler adapter, unit tests and benchmark.

## Scope honesty
This is a **local demonstrator**, not a live AWS deployment. It does not yet wire CloudWatch subscriptions, CloudTrail/EventBridge, DynamoDB, S3, SNS or production authentication. Do not claim cloud integration or real-world accuracy until deployed and tested.

## Run
Python 3.10+; no third-party packages required.
```bash
python app.py
```
Open http://127.0.0.1:8000 and click **Load demo events**. The server binds to localhost only.

## Test and benchmark
```bash
python -m unittest discover -s tests -v
python benchmark.py
```
Record your actual console output, date, Python version, OS and machine specs in the report. Performance varies by machine.

## Demo sequence
1. Explain that the dashboard is a local prototype.
2. Load demo events; show the benign event and triggered security-like findings.
3. Submit a benign request, then an `authentication_failed` event.
4. Run tests and benchmark from terminal.
5. Explain AWS integration as the next deployment step.

## Canonical schema
`event_id`, `timestamp`, `source`, `event_type`, `principal`, `resource`, `source_ip`, `outcome`, `invocations`, `error_count`, `details`.

## Security limitations
No cloud credentials are required. Do not add secrets or real personal data to events. Rules are illustrative and not a production IDS or SIEM replacement. A real deployment needs least-privilege IAM, encrypted storage, retention controls, dead-letter queues, input validation, authenticated dashboard access and budget alerts.
