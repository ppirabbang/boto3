import boto3

aws_management_console = boto3.session.Session(profile_name="default")
# 웹 상에서 로그인 하자마자 보이는 화면이 management_console 일텐데 이걸 프로그래밍으로 boto3(직접 aws랑 상호작용 가능) 사용해서 새로운 세션을 만들겠다, aws configure에 입력한 내용을 바탕으로 default profile을 만든 것
iam_console = aws_management_console.resource('iam')
# 로그인 한 화면에서 iam 클릭해서 들어가는 것 처럼 aws_management_console (로그인 후 첫 화면) 에서 iam 콘솔을 선택하겠다
for each_user in iam_console.users.all():
  print(each_user.name)
# iam에서도 왼쪽에 많은 옵션이 존재하는데 이 중 users에만 관심 있고, users에서 이름만 가져오겠다