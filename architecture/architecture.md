# Silent Scalper Architecture

## Components

- **S3 Intake Bucket**
  Entry point for files (API or internal uploads)

- **AWS Lambda**
  Event-driven processor triggered by S3 ObjectCreated events

- **S3 Quarantine Bucket**
  Isolates corrupted or invalid files

- **API Gateway**
  Secure ingestion endpoint for external systems

- **CloudWatch**
  Logs, metrics, and failure visibility

## Design Principles

- Event-driven
- Serverless
- Least privilege
- Failure isolation
- Cost-efficient scaling
