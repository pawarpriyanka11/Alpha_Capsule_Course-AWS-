# EC2 (Elastic Compute Cloud) – Website Hosting

## What is EC2?
EC2 provides resizable compute capacity in the cloud. You can launch virtual servers (instances) quickly.

### Steps to Launch EC2
1. Open EC2 dashboard → Launch Instance  
2. Choose **AMI** (Amazon Machine Image)  
3. Select **Instance Type** (t2.micro for free tier)  
4. Configure **Instance Details** (network, IAM role)  
5. Add **Storage** (EBS volume)  
6. Add **Tags** (optional)  
7. Configure **Security Group** (allow HTTP/HTTPS, SSH)  
8. Review → Launch → Select or create a **Key Pair**  
9. Connect via SSH:  
```bash
ssh -i "keypair.pem" ec2-user@<public-ip>
