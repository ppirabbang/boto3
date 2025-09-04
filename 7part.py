import boto3
aws_management_console = boto3.session.Session(profile_name = "default")
ec2_console = aws_management_console.client(service_name = "ec2" , region_name="ap-northeast-2")

response = ec2_console.run_instances(
  ImageId = 'ami-0ae2c887094315bed',
  InstanceType = 't3.micro',
  MaxCount=123,
  MinCount=123
)