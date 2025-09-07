# AWS Lambda

## What is Lambda?
AWS Lambda lets you **run code without provisioning servers**. You only pay for compute time consumed.

### Key Features
- Event-driven (triggered by S3, DynamoDB, API Gateway, etc.)  
- Automatic scaling  
- Supports multiple languages (Python, Node.js, Java, etc.)  

### Steps to Create Lambda
1. Open Lambda service → Create Function  
2. Choose **Author from scratch**  
3. Select runtime (e.g., Python 3.9)  
4. Set **Execution Role** (IAM role with permissions)  
5. Add **Trigger** (S3 event, API Gateway, etc.)  
6. Write code in inline editor or upload .zip  
7. Test the function → Monitor in CloudWatch
