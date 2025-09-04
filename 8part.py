import boto3
aws_management_console = boto3.session.Session(profile_name = "default")
ec2_console = aws_management_console.client(service_name = "ec2", region_name="ap-northeast-2")
response = ec2_console.stop_instances(
    InstanceIds=['i-1234567890abcdef0']
)
# start_instances 도 있어서 stop 된 걸 다시 실행시킬 수도 있다
# terminate_instances 를 하면 인스턴스 상태를 바꾼다