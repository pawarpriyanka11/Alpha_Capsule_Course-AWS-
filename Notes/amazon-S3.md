```markdown
# S3 Bucket – Website Hosting

## What is S3?
Amazon S3 is object storage for storing and retrieving data (files, images, backups).

### Creating an S3 Bucket
1. Open S3 dashboard → Create bucket  
2. Enter **bucket name** (must be unique)  
3. Choose **Region**  
4. Configure settings (Versioning, Encryption)  
5. Set **Public Access** (for static website hosting)  
6. Upload files

### Static Website Hosting
- Enable **Static Website Hosting** in bucket properties  
- Set **Index Document** and **Error Document**  
- Access via S3 endpoint: ``
