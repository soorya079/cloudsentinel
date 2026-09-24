# CloudSentinel

## Self-Healing DevSecOps Platform on AWS

CloudSentinel is a cloud-native DevSecOps platform that automates containerized application delivery, continuous deployment, monitoring, incident detection, alerting, and self-healing recovery on AWS.

## Architecture

GitHub
   ↓
GitHub Actions
   ↓
Docker Build
   ↓
Amazon ECR
   ↓
Amazon ECS Fargate
   ↓
Application Load Balancer
   ↓
CloudWatch
   ↓
EventBridge
   ↓
AWS Lambda
   ↓
ECS Self-Healing Deployment

CloudWatch Alarm
   ↓
Amazon SNS
   ↓
Email Alert

## Technology Stack

### Development
- Python
- FastAPI
- Docker
- Git
- GitHub

### AWS
- Amazon ECR
- Amazon ECS Fargate
- Application Load Balancer
- Amazon CloudWatch
- Amazon EventBridge
- AWS Lambda
- Amazon SNS
- AWS IAM
- Amazon VPC
- Security Groups

### CI/CD & Security
- GitHub Actions
- GitHub OIDC
- IAM least-privilege policies
- Containerized deployment

## Key Features

### CI/CD
- Automated Docker image build
- Pushes container images to Amazon ECR
- Automated ECS deployment through GitHub Actions
- GitHub OIDC authentication with AWS

### Containerized Deployment
- FastAPI application running in Docker
- ECS Fargate service
- Application Load Balancer
- Target group health checks

### Self-Healing
CloudSentinel detects ECS task state changes through EventBridge.

EventBridge triggers the `CloudSentinel-SelfHealing` Lambda function, which initiates a new ECS deployment to restore the service automatically.

### Monitoring & Alerting
- CloudWatch CPU monitoring
- CloudWatch alarm for high CPU utilization
- Amazon SNS notification topic
- Email alert delivery

### Security
- ECS application security group restricted to ALB traffic on port 8000
- ALB exposed on HTTP port 80
- GitHub OIDC instead of long-lived AWS credentials
- IAM policies for required AWS operations

## Self-Healing Validation

The self-healing mechanism was tested by intentionally stopping the running ECS task.

Expected recovery flow:

ECS Task Stopped
   ↓
ECS Task State Change Event
   ↓
Amazon EventBridge
   ↓
CloudSentinel-SelfHealing Lambda
   ↓
ECS Deployment
   ↓
New ECS Task
   ↓
ALB Target Registration
   ↓
Health Check
   ↓
Healthy Application

Validation result:

- ECS Desired Count: 1
- ECS Running Count: 1
- Pending Count: 0
- Deployment Rollout: COMPLETED
- ALB Target: HEALTHY

## Alerting Validation

SNS notification was manually tested successfully.

CloudSentinel successfully delivered an alert email through:

CloudWatch → SNS → Email

## Current Status

Production-style AWS DevOps workflow implemented and end-to-end self-healing and alerting mechanisms validated.

## Project Highlights

- AWS DevOps
- CI/CD automation
- Docker containerization
- ECS Fargate
- Infrastructure monitoring
- Event-driven automation
- Lambda self-healing
- CloudWatch monitoring
- SNS alerting
- GitHub Actions
- GitHub OIDC
- AWS IAM security

## Author

Soorya M
