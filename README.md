# AWS Resource Deployment Scripts

This repository contains Python scripts for deploying infrastructure on AWS using boto3. Each script demonstrates different AWS setup scenarios, helping students understand how to create, configure, and troubleshoot resources on AWS.

## Files in the Repository

1. **deploy_aws_ec2_vpc.py**
   - This is the base script that sets up a VPC, a subnet, a security group allowing SSH access, and three EC2 instances. It serves as a starting point for deploying basic network infrastructure and instances.

2. **deploy_aws_ec2_vpc_extended.py**
   - This extended version deploys a more complex infrastructure, including:
     - A VPC with two subnets.
     - A route table associated with both subnets.
     - A security group that allows both SSH and HTTP access.
     - Two EC2 instances, each deployed in separate subnets.
   - This script is useful for understanding multi-subnet configurations and more advanced security group rules.

3. **deploy_aws_ec2_vpc_incomplete.py**
   - This script is intentionally incomplete and contains errors. Key configurations are missing, such as VPC and security group details. The purpose is for students to review and correct the code to ensure successful deployment.

## Running the Scripts

1. Clone this repository and navigate to the folder:
   ```bash
   git clone https://github.com/artvaze/DBS_IaC_AWS.git
   cd DBS_IaC_AWS
   ```

2. Install the necessary dependencies:
   ```bash
   pip install boto3
   ```

3. Run each script with:
   ```bash
   python script_name.py
   ```

## Educational Objective

These scripts provide practical examples of infrastructure as code on AWS, allowing students to learn by setting up resources and fixing deployment issues.
