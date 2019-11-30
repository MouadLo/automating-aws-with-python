# coding: utf-8
import boto3
session = boto3.Session()
ec2 = session.resource('ec2')
key_name = 'python_automation_key'
key_path = key_name + '.pem'
key = ec2.create_key_pair(KeyName=key__name)
key = ec2.create_key_pair(KeyName=key_name)
key
key.key_material
with open(key_path, 'w') as key_file:
    key_file.write(key.key_material)
    
get_ipython().run_line_magic('ls', '-l python_automation_key.pem')
import os, stat
os.chmod(key_path, stat.S_IRUSR | stat.S_IWUSR)
get_ipython().run_line_magic('ls', '-l python_automation_key.pem')
ec2.images.filter(Owners=['amazon'])
list(ec2.images.filter(Owners=['amazon']))
img = ec2.Image('ami-0dacb0c129b49f529 ')
img.name
session.region_name
img = ec2.Image('ami-00068cd7555f543d5  ')
img.mane
img.name
img = ec2.Image('ami-00068cd7555f543d5')
img.name
ami_name = 'amzn2-ami-hvm-2.0.20191116.0-x86_64-gp2'
filters = [{'Name' : 'name', 'Values': [ami_name]}]
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
ec2_apse2 = session.resource('ec2', region_name='ap-southeast-2')
list(ec2_apse2.images.filter(Owners=['amazon'], Filters=filters))
img
key
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
instances
inst = instances[0]
inst.terminate()
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
inst = instances[0]
inst.public_dns_name
inst.wait_until_running()
inst.reload()
inst.public_dns_name
inst.security_groups
# Look up the security group
# Authorize incoming connections from our public IP address, on port 22 (the port SSH uses)
sg = ec2.SecurityGroup(inst.security_groups[0]['GroupId'])
sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'ToPort': 22, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp': '41.251.41.211/32'}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'ToPort': 22, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp': '3.16.136.25/32'}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort': 80, 'ToPort': 80, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}])
inst.public_dns_name
get_ipython().run_line_magic('history', '')
