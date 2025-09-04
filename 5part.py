# import all the modules and libraries
import boto3
from pprint import pprint

# open management console
aws_management_console = boto3.session.Session(profile_name="default")

# open iam console
iam_console = aws_management_console.client(service_name="iam")

result = iam_console.list_users()
#pprint(result['Users'])
for each_user in  result['Users']:
  print(each_user['UserName'])