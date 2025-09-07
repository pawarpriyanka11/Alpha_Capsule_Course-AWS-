# AWS Lambda Function

## Overview
Lambda is used to run serverless functions automatically when triggered by events like SQS messages or S3 uploads.

---

## Steps
1. Go to **AWS Console → Lambda → Create Function**.
2. Choose **Author from Scratch**, give a name, and select runtime (Python/Node.js).
3. Assign an **IAM role** with permissions to S3, SQS, etc.
4. Write your function code (e.g., process files, transform data).
5. Set a **trigger**:
   - SQS message
   - S3 upload
6. Test the function with sample events.

---

## Tips
- Monitor execution with **CloudWatch logs**.
- Keep functions small and focused for faster execution.
