
# Tác vụ Fargate được lập lịch (Scheduled Fargate Tasks) với AWS CDK

## Chạy project

- Clone project

```
git clone https://github.com/vntechies/011-aws-cdk-scheduled-fargate-task.git aws-cdk-scheduled-fargate-task
```

- Tạo virtualenv

```shell
cd aws-cdk-scheduled-fargate-task
python3 -m venv .venv
source .venv/bin/activate
# Trên windows
.venv\Scripts\activate.bat
pip install -r requirements.txt
cdk synth
```

## Một số câu lệnh hữu ích 

 * `cdk ls`          list tất cả các stacks trong ứng dụng
 * `cdk synth`       tạo ra các CloudFormation template tổng hợp
 * `cdk deploy`      triển khai stack này lên tài khoản và region AWS mặc định
 * `cdk diff`        so sánh stack đã triển khai với hiện tại
 * `cdk docs`        mở tài liệu CDK

