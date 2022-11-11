import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_cdk_scheduled_fargate_task.aws_cdk_scheduled_fargate_task_stack import AwsCdkScheduledFargateTaskStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_cdk_scheduled_fargate_task/aws_cdk_scheduled_fargate_task_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsCdkScheduledFargateTaskStack(app, "aws-cdk-scheduled-fargate-task")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
