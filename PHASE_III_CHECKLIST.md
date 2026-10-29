# Phase III Completion Checklist

## Implementation
- [x] Local event normalization and canonical schema
- [x] Rule-based detection and risk scoring
- [x] Local SQLite persistence
- [x] Dashboard and manual test-event ingestion
- [x] Lambda handler adapter (not deployed)
- [ ] Connect actual CloudWatch and CloudTrail/EventBridge events
- [ ] Configure DynamoDB/S3/SNS in AWS
- [ ] Deploy via SAM with least-privilege IAM
- [ ] Static analysis and code review

## Testing and validation
- [x] Unit tests for normalization and five detection scenarios
- [ ] Run tests on team's machine and save screenshot
- [ ] Verify findings against expected results
- [ ] Test malformed input and duplicate events
- [ ] Integration test in a disposable AWS environment if available

## Performance analysis
- [x] Reproducible local throughput benchmark script
- [ ] Run benchmark and paste actual output into report
- [ ] Record Python version, OS, CPU/RAM and event count
- [ ] Measure end-to-end AWS alert latency only after deployment
- [ ] Estimate cost using actual region and usage

## Exhibition evidence
- [ ] Dashboard screenshot after demo data
- [ ] Successful unit-test screenshot
- [ ] Benchmark screenshot
- [ ] Architecture and data-flow explanation
- [ ] 3–5 minute demo rehearsal
- [ ] Known limitations and next steps
- [ ] Guide review/sign-off if required

Never invent accuracy, precision, recall, latency, throughput, AWS deployment, cloud cost or test pass results. Use only observed results.
