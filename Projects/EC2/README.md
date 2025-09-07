# AWS Chatbot File Processing Project

## Overview
This project demonstrates using **AWS services** to build a chatbot that can handle file uploads and processing automatically.

---

## AWS Services Used
- **Amazon SQS:** Queue messages from chatbot requests.  
- **AWS Lambda:** Process files triggered by SQS.  
- **Amazon S3:** Store uploaded and processed files.  
- **EC2:** Host the chatbot web app.  
- **IAM:** Manage secure access.  

---

## Workflow
1. User interacts with the chatbot on EC2.  
2. Files are uploaded to S3 and a message is sent to SQS.  
3. Lambda function processes the file.  
4. Results are stored in S3 and user is notified.  

---

