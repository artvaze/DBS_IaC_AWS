import boto3

ec2 = boto3.resource('ec2', region_name='us-east-1')
client = boto3.client('ec2', region_name='us-east-1')

# Create a VPC with multiple subnets and route table
vpc = ec2.create_vpc(CidrBlock='10.0.0.0/16')
subnets = [
    vpc.create_subnet(CidrBlock='10.0.1.0/24'),
    vpc.create_subnet(CidrBlock='10.0.2.0/24')
]
route_table = vpc.create_route_table()
for subnet in subnets:
    route_table.associate_with_subnet(SubnetId=subnet.id)

# Create Security Group
security_group = ec2.create_security_group(
    GroupName='ExtendedSecurityGroup',
    Description='Allow SSH and HTTP access',
    VpcId=vpc.id
)
security_group.authorize_ingress(
    CidrIp='0.0.0.0/0',
    IpProtocol='tcp',
    FromPort=22,
    ToPort=22
)
security_group.authorize_ingress(
    CidrIp='0.0.0.0/0',
    IpProtocol='tcp',
    FromPort=80,
    ToPort=80
)

# Launch EC2 Instances across subnets
instances = ec2.create_instances(
    ImageId='ami-0c55b159cbfafe1f0',  # Amazon Linux 2
    MinCount=2,
    MaxCount=2,
    InstanceType='t2.micro',
    KeyName='YourKeyPairName',
    NetworkInterfaces=[{
        'SubnetId': subnet.id,
        'DeviceIndex': 0,
        'AssociatePublicIpAddress': True,
        'Groups': [security_group.id]
    } for subnet in subnets]
)
for instance in instances:
    instance.wait_until_running()
    instance.reload()
    print(f"Instance {instance.id} launched at {instance.public_ip_address}")
