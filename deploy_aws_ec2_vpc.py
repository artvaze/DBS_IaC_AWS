import boto3

ec2 = boto3.resource('ec2', region_name='us-east-1')
client = boto3.client('ec2', region_name='us-east-1')

# Create a VPC
vpc = ec2.create_vpc(CidrBlock='10.0.0.0/16')
subnet = vpc.create_subnet(CidrBlock='10.0.1.0/24')

# Create Security Group
security_group = ec2.create_security_group(
    GroupName='MySecurityGroup',
    Description='Allow SSH access',
    VpcId=vpc.id
)
security_group.authorize_ingress(
    CidrIp='0.0.0.0/0',
    IpProtocol='tcp',
    FromPort=22,
    ToPort=22
)

# Launch EC2 Instances
instances = ec2.create_instances(
    ImageId='ami-0c55b159cbfafe1f0',  # Amazon Linux 2
    MinCount=3,
    MaxCount=3,
    InstanceType='t2.micro',
    KeyName='YourKeyPairName',
    NetworkInterfaces=[{
        'SubnetId': subnet.id,
        'DeviceIndex': 0,
        'AssociatePublicIpAddress': True,
        'Groups': [security_group.id]
    }]
)
for instance in instances:
    instance.wait_until_running()
    instance.reload()
    print(f"Instance {instance.id} launched at {instance.public_ip_address}")
