# coding: utf-8
ami-062f7200baf2fa504
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
key.key_name
list(key.key_name)
key.key_material
import boto3
session = boto3.Session(profile_name='pythonAutomation')
as_client = session.client('autoscaling')
as_client.describe_auto_scaling_groups()
as_client.describe_policies()
as_client.execute_policy(AutoScalingGroupName='Notifon Example Group', PolicyName='Notifon Example Group')
as_client.execute_policy(AutoScalingGroupName='Notifon Example Group', PolicyName='Scale Down')
as_client.execute_policy(AutoScalingGroupName='Notifon Example Group', PolicyName='Scale Up')
as_client.execute_policy(AutoScalingGroupName='Notifon Example Group', PolicyName='Scale Up')
get_ipython().run_line_magic('save', 'autoscale_example.py 80-94')
