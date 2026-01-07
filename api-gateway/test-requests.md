# API Gateway Test Requests

## Successful Upload

```powershell
Invoke-RestMethod `
  -Method POST `
  -Uri "https://<api-id>.execute-api.us-east-1.amazonaws.com/prod/upload" `
  -Headers @{ "Content-Type" = "application/json" } `
  -Body '{ "filename":"test-api.txt", "content":"hello-from-api-gateway" }'
