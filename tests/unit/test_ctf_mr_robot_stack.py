import aws_cdk as core
import aws_cdk.assertions as assertions

from ctf_mr_robot.ctf_mr_robot_stack import CtfMrRobotStack

# example tests. To run these tests, uncomment this file along with the example
# resource in ctf_mr_robot/ctf_mr_robot_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CtfMrRobotStack(app, "ctf-mr-robot")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
