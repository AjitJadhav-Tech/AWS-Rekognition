# AWS Rekognition Image Processing Pipeline

[![AWS](https://img.shields.io/badge/AWS-Cloud-orange?logo=amazon-aws)](https://aws.amazon.com/)
[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![CDK](https://img.shields.io/badge/AWS_CDK-2.118.0-green)](https://aws.amazon.com/cdk/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A production-ready, serverless image processing pipeline built with AWS CDK, Python, and Amazon Rekognition. This system automatically classifies images, stores results in DynamoDB, forwards data to downstream systems, and provides rich analytics through Amazon QuickSight.

## 🎯 Overview

This project demonstrates a complete AWS serverless architecture for image processing and classification using:

- **Amazon Rekognition** - AI-powered image label detection
- **AWS Lambda** - Serverless compute for all processing steps
- **Amazon DynamoDB** - NoSQL database for classification results
- **Amazon S3** - Scalable image and data storage
- **Amazon SQS & SNS** - Reliable message queuing and pub/sub
- **Amazon Athena & QuickSight** - Federated queries and visualization
- **AWS CDK** - Infrastructure as Code in Python

## 🏗️ Architecture

![Architecture Diagram](AWS_ReKognition_AI_IDE_AWS_KIRO/Concepts/Recognition.drawio.png)

### Key Features

✅ **Serverless & Scalable** - Auto-scales from zero to millions of images  
✅ **Event-Driven** - Fully asynchronous processing with SQS/SNS  
✅ **Fault Tolerant** - Dead-letter queues and CloudWatch alarms  
✅ **Production Ready** - Complete IAM policies and security best practices  
✅ **Analytics Ready** - QuickSight dashboards via Athena federated queries  
✅ **Well Documented** - Comprehensive setup and troubleshooting guides  

## 📁 Project Structure

```
AWS-Rekognition/
├── AWS_ReKognition_AI_IDE_AWS_KIRO/
│   ├── Concepts/                    # Architecture diagrams and concepts
│   │   ├── Recognition.drawio.png   # Main architecture diagram
│   │   ├── VibeCoding.png          # Development methodology
│   │   └── ...
│   ├── Examples/                    # Sample data and reports
│   └── solution-files/
│       └── solution-files/
│           ├── README.md            # 📖 Detailed documentation (START HERE)
│           └── python/              # Python CDK implementation
│               ├── app.py           # CDK app entry point
│               ├── api/             # APIStack - Image ingestion
│               ├── recognition/     # RekognitionStack - AI classification
│               ├── integration/     # IntegrationStack - Data forwarding
│               ├── visualization/   # VisualizationStack - Analytics
│               ├── iam/             # IAM policies and roles
│               ├── deploy.sh        # 🚀 Deployment automation
│               └── requirements.txt # Python dependencies
```

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Node.js (for AWS CDK CLI)
- AWS CLI v2 configured
- AWS account with QuickSight subscription

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/AWS-Rekognition.git
cd AWS-Rekognition/AWS_ReKognition_AI_IDE_AWS_KIRO/solution-files/solution-files/python

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Deploy all stacks
./deploy.sh
```

### Testing

```bash
# Upload an image
curl "https://<api-endpoint>/prod/?url=https://example.com/image.jpg&name=test.jpg"

# List classified images
curl "https://<rekognition-api-endpoint>/prod/"

# Seed test data
python scan_classifications.py --seed --region us-east-1
```

## 📚 Documentation

For detailed documentation, see:

👉 **[Complete Documentation](AWS_ReKognition_AI_IDE_AWS_KIRO/solution-files/solution-files/README.md)** - Setup, deployment, troubleshooting, and architecture details

👉 **[Project Assets Summary](AWS_ReKognition_AI_IDE_AWS_KIRO/solution-files/solution-files/PROJECT_ASSETS_SUMMARY.md)** - Complete inventory of all project files

## 🏗️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Language** | Python 3.11 |
| **IaC** | AWS CDK v2 |
| **Image AI** | Amazon Rekognition |
| **Compute** | AWS Lambda |
| **Storage** | Amazon S3, DynamoDB |
| **Messaging** | SNS, SQS |
| **Analytics** | Athena, Glue, QuickSight |
| **Config** | SSM Parameter Store |
| **Monitoring** | CloudWatch |

## 📊 What Gets Deployed

The CDK app deploys 4 interconnected stacks:

1. **APIStack** - REST API for image ingestion, S3 storage, SNS/SQS pipeline
2. **RekognitionStack** - Lambda for AI classification, DynamoDB storage
3. **IntegrationStack** - XML data forwarding to downstream systems
4. **VisualizationStack** - Athena connector, Glue crawler, QuickSight integration

## 🔒 Security & IAM

- Complete IAM policy templates included
- Least-privilege access patterns
- S3 bucket encryption and SSL enforcement
- No hardcoded credentials
- VPC-ready (configurable)

## 💰 Cost Optimization

- Lambda with optimized memory/timeout settings
- DynamoDB on-demand pricing
- S3 lifecycle policies
- Dead-letter queues to prevent lost messages
- CloudWatch alarms for cost monitoring

## 🛠️ Development

Built using AWS CDK best practices:
- Modular stack architecture
- Cross-stack parameter passing (no CloudFormation exports)
- Context-driven configuration (cdk.json)
- Automated deployment scripts
- Comprehensive error handling

## 📝 Key Design Decisions

- **SQS visibility timeout** - Set to 6× Lambda timeout to prevent duplicates
- **DLQs everywhere** - All queues have dead-letter queues with CloudWatch alarms
- **Bucket retention** - Image bucket and DynamoDB table use `RETAIN` policy
- **boto3 optimization** - Clients instantiated at module level for connection reuse
- **Logging** - Structured logging with Python `logging` module

## 🤝 Contributing

Contributions welcome! Areas for improvement:
- Unit tests for Lambda functions
- Integration test suite
- CI/CD pipeline (GitHub Actions)
- Additional Rekognition features (face detection, text extraction)
- Multi-region deployment support

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Ajit Jadhav**

## 🙏 Acknowledgments

- Built with AWS CDK
- Uses Amazon Rekognition for AI-powered image classification
- Inspired by serverless architecture best practices

## 📞 Support

For issues and questions:
- 📖 Check the [detailed documentation](AWS_ReKognition_AI_IDE_AWS_KIRO/solution-files/solution-files/README.md)
- 🐛 Open an issue on GitHub
- 💬 Review the Known Issues section in the docs

---

⭐ If you find this project useful, please consider giving it a star!
