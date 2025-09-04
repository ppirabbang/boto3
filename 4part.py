import boto3

aws_management_console = boto3.session.Session(profile_name="default")

iam_console_resource = aws_management_console.resource('iam')
iam_console_client = aws_management_console.client('iam')

for each_user in iam_console_resource.users.all():
  print(each_user.name)

for each in iam_console_client.list_users()['Users']:
  print(each['UserName'])

# resources 와 client는 기본적으로 로그인 첫 화면에서 다양한 옵션에 접근할 수 있는 것은 맞으나 resources로 접근할 수 있는 옵션이 제한적. 그래서 client를 쓰는데 튜플이라 문법이 조금 다르다

# dir(aws_management_console)
# print(aws_management_console.get_available_resources())