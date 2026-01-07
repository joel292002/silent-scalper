# Silent Scalper — Serverless Data Ingestion Pipeline (AWS)

Silent Scalper is a **fault-tolerant, serverless data ingestion pipeline** built on AWS.  
It is designed to handle unpredictable traffic, isolate bad data automatically, and operate on a strict pay-per-use cost model.

The system supports **secure ingestion via API Gateway** as well as **direct S3 uploads**, while ensuring corrupted or invalid data never disrupts healthy processing.

---

## Architecture Overview

**Core AWS Services**
- Amazon S3 (intake + quarantine buckets)
- AWS Lambda (event-driven processing)
- Amazon API Gateway (secure ingestion endpoint)
- Amazon CloudWatch (logs & metrics)
- AWS IAM (least-privilege access control)

**High-level flow**
1. Files arrive via:
   - API Gateway (external clients)
   - Direct S3 upload (internal or batch ingestion)
2. S3 ObjectCreated events trigger Lambda
3. Lambda inspects file metadata
4. Valid files are processed normally
5. Invalid files are moved to a quarantine bucket
6. All activity is logged and monitored in CloudWatch

---

## Why This Architecture Matters

This design solves two common real-world problems:

### Cost Efficiency
- No idle servers
- Compute runs **only** when files arrive
- Scales automatically with traffic spikes

### Failure Isolation
- Corrupted or malformed files are quarantined
- Bad data never crashes or blocks the pipeline
- Failures are observable and auditable

This pattern is commonly used in:
- Data ingestion platforms
- Security pipelines
- IoT backends
- Healthcare and financial data processing systems



---
## Lambda Processing Logic

The Lambda function is triggered automatically by S3 `ObjectCreated` events.

### Behavior
- Extracts bucket name and object key from the event
- Simulates corruption detection using filename rules
- Copies failed files into a quarantine prefix
- Allows healthy files to continue processing
- Logs every step for observability

This logic demonstrates how production systems isolate bad data without stopping the pipeline.







---

## Failure Handling (Quarantine Logic)

For demonstration purposes, files containing `"fail"` in the filename are treated as corrupted and automatically moved to a quarantine bucket.

In production systems, this logic would typically be replaced with:
- Schema validation
- Checksum verification
- Antivirus scanning
- File size or format enforcement
- Content inspection rules

---

## Security Design

- No public S3 access
- External uploads handled **only** through API Gateway
- Lambda operates with **least-privilege IAM policies**
- Explicit AccessDenied debugging performed during development
- Clear separation between intake and quarantine storage

---

## API Gateway Ingestion Example

Example PowerShell request used to upload a file securely via API Gateway:

```powershell
Invoke-RestMethod `
  -Method POST `
  -Uri "https://<api-id>.execute-api.us-east-1.amazonaws.com/prod/upload" `
  -Headers @{ "Content-Type" = "application/json" } `
  -Body '{ "filename":"test-api.txt", "content":"hello-from-api-gateway" }'



