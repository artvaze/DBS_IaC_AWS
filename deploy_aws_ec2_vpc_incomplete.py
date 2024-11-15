import boto3

ec2 = boto3.resource('ec2', region_name='us-east-1')

# Missing VPC creation step
# Create Subnet (no VPC specified, should cause an error)
subnet = ec2.create_subnet(CidrBlock='10.0.1.0/24')

# Incorrect Security Group (missing VPC ID)
security_group = ec2.create_security_group(
    GroupName='IncompleteSecurityGroup',
    Description='Allow SSH access'
)
# Missing authorization step for SSH access

# Attempt to launch EC2 Instances (missing security group)
instances = ec2.create_instances(
    ImageId='ami-0c55b159cbfafe1f0',  # Amazon Linux 2
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='YourKeyPairName'
)
