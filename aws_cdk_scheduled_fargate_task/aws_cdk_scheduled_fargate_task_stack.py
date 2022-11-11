from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns,
    aws_applicationautoscaling as appscaling,
    aws_logs,
)

from constructs import Construct


class AwsCdkScheduledFargateTaskStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Tạo VPC với 9 subnets trên 3 AZs
        my_vpc = ec2.Vpc(
            self,
            "myvpc",
            cidr="172.31.0.0/16",
            max_azs=3,
            nat_gateways=1,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    cidr_mask=20, name="public", subnet_type=ec2.SubnetType.PUBLIC
                ),
                ec2.SubnetConfiguration(
                    cidr_mask=20,
                    name="application",
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_NAT,
                ),
                ec2.SubnetConfiguration(
                    cidr_mask=20,
                    name="data",
                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
                    reserved=True,
                ),
            ],
        )

        # Tạo ECS Cluster
        my_cluster = ecs.Cluster(
            self,
            "service-cluster",
            cluster_name="service-cluster",
            container_insights=True,
            vpc=my_vpc,
        )

        image = ecs.ContainerImage.from_registry("amazonlinux:2")

        ecs_patterns.ScheduledFargateTask(
            self,
            "amazon-linux-echo-task",
            cluster=my_cluster,
            platform_version=ecs.FargatePlatformVersion.LATEST,
            schedule=appscaling.Schedule.expression("rate(1 minute)"),
            scheduled_fargate_task_image_options=ecs_patterns.ScheduledFargateTaskImageOptions(
                image=image,
                memory_limit_mib=1024,
                log_driver=ecs.LogDriver.aws_logs(
                    stream_prefix="scheduled-fargate-task",
                    log_retention=aws_logs.RetentionDays.ONE_DAY,
                ),
                environment={"APP_NAME": "scheduled-fargate-task"},
                command=["echo", "Xin chào VNTechies!"],
            ),
        )
