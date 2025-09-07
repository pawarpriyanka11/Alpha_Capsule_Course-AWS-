# Chatbot Creation

## Overview
The chatbot interacts with users to upload files and request processing.

---

## Steps
1. Create a **frontend** interface (HTML/CSS/JS or React).
2. Create a **backend** (Node.js or Python Flask):
   - Connect to **S3** to upload files.
   - Send messages to **SQS** for processing.
   - Receive processed results from **S3**.
3. Deploy the backend on **EC2** or any server.
4. Integrate chatbot logic to notify users when processing is done.

---

## Tips
- Use AWS SDK (Boto3 for Python / AWS SDK for Node.js) to interact with AWS services.
- Keep chatbot interactions simple and user-friendly.
