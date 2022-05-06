# AWS Proton Sample Services

This repository contains samples of application code that can be deployed with AWS Proton using the AWS Proton Sample Templates [for CloudFormation](https://github.com/aws-samples/aws-proton-cloudformation-sample-templates) and [for Terraform](https://github.com/aws-samples/aws-proton-terraform-sample-templates). 

Each folder in this repository corresponds to a service. The sample templates contain pipeline a pipeline parameter that allow you to select a specific folder, so that you can select the correct folder for your type of service.

- ## ecs-backend

    Flask app that responds with a Hello message along with the Time.  [README](./ecs-backend)

- ## ecs-ping-backend-a-record

    Application code to ping Fargate backend service using service discovery. [README](./ecs-ping-backend-a-record)

- ## ecs-ping-backend-srv-record

    Application code to ping ECS on EC2 backend service using service discovery. [README](./ecs-ping-backend-srv-record)

- ## ecs-ping-sns

    Python application that sends a random 5-letter string along with the time to the shared SNS topic, every 5 minutes. [README](./ecs-ping-sns)

- ## ecs-static-website

    Containerized static website. [README](./ecs-static-website)

- ## ecs-worker

    Python application that polls the SQS queue for messages, and writes the message body to CloudWatch logs. [README](./ecs-worker)

- ## lambda-ping-sns

    Lambda function to send a random string and time to the shared SNS topic, whenever invoked by API Gateway HTTP API. [README](./lambda-ping-sns)

- ## lambda-worker

    Lambda function that writes the event, context object and SQS message to CloudWatch Logs. [README](./lambda-worker)

## Security

See [CONTRIBUTING](./CONTRIBUTING.md#security-issue-notifications) for more information.

## Code of Conduct

See [CODE OF CONDUCT](./CODE_OF_CONDUCT.md) for more information.

## License

This library is licensed under the MIT-0 License. See the [LICENSE](./LICENSE) file.

