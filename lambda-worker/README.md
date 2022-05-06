# Expected output

INFO	Event:  
{
    "Records": [
        {
            "messageId": "7effcc2b-d4ba-4941-a586-ee40e8b41c83",
            "receiptHandle": "AQEB2epQxsixNphT1pJ6W2a7ptvtqJDYXtqG2G1SCDZhGQT51GuU77u/2ya68nIOCUjZBlk/Am002E8x2zW0i5RcFi/6c1BXOIpOAZComPkFXZMD56HxDkwTmW8AA7/7xER7oVvxM9/B9nfr52p3PiofmngpMR+FAYNj5R96UflB24KNdefSy/7BVvIk45/LzhQbTySkVAo/D5wwxWPAqwBK6N0wm43CWlm6ILk9lirRbORrZPUyX5tRQyMeN6aSGdJiEm1Wl+0CxgWCvwTuUkoQaTGiEkEsbPGHR/J/iHbwHlKS7vPfxldZHZ5AjY08dzighu7qpbuRxLMBRiwKNwG4KOfArHR0YjaGEJVCRxWrEcLQBSnXo1EBHSR62UuEL6BW6Pige1jN6yjSp4fmGliaew8Y+n/7HXjCsvkDL53qPVcGQU7vA3Na5t1j3p8a6TSrMKu02amINpvfeSXB2tlRqA5Y7GqO1X504VtG4uFezIU=",
            "body": "{\n  \"Type\" : \"Notification\",\n  \"MessageId\" : \"76f49e3f-97eb-5e9f-8645-c4d758c3d592\",\n  \"TopicArn\" : \"arn:aws:sns:us-east-2:XXXXXXXXXXXX:AWSProton-vpc-env-prod-cloudformation--QYWPQLSESXEMRBY-ping\",\n  \"Subject\" : \"New message from publisher\",\n  \"Message\" : \"Message 3x3txhl9i2 sent at Sun May 01 2022 18:09:44 GMT+0000 (Coordinated Universal Time)\",\n  \"Timestamp\" : \"2022-05-01T18:09:44.076Z\",\n  \"SignatureVersion\" : \"1\",\n  \"Signature\" : \"G6ef1WJyfFGgHS8dh1sHCjruxIs0A1D0dbpb67rFvUOWYiR8K5oWk4HgMTQ4UrGVUKLtRhwFF9UNVSYINePm9M/KmYhKLldDtg0VzBTJ90uu98XunFFeeSuS/Jw6zilBhIOKV+Bveq+s0FrmJDmrXx9N7yOkruD/azVUd/o1k+QSqlpkRqT5pDW2eVIHFnjn2uKEaZjDR71sCAuhlzXmlNOuFMMvc6OSVqvHfGnhnQJVOfYSJwNKCpXR6Y1F0+i2ubDIEjQHGi6qvYsRFlkpRdS2jJA0xsad6nwecH8bWPgQ+O0l0z63HJDw+ghGyl7kM+3RfRPpSwNsZhLMeL/frA==\",\n  \"SigningCertURL\" : \"https://sns.us-east-2.amazonaws.com/SimpleNotificationService-7ff5318490ec183fbaddaa2a969abfda.pem\",\n  \"UnsubscribeURL\" : \"https://sns.us-east-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-2:XXXXXXXXXXXX:AWSProton-vpc-env-prod-cloudformation--QYWPQLSESXEMRBY-ping:dc8974a0-3710-4b29-a078-7d0d5f53c844\"\n}",
            "attributes": {
                "ApproximateReceiveCount": "1",
                "SentTimestamp": "1651428584109",
                "SenderId": "AIDAJQR6QDGQ7PATMSYEY",
                "ApproximateFirstReceiveTimestamp": "1651428584110"
            },
            "messageAttributes": {},
            "md5OfBody": "20d9c6741a7b6f8858309bb6e78dd5aa",
            "eventSource": "aws:sqs",
            "eventSourceARN": "arn:aws:sqs:us-east-2:XXXXXXXXXXXX:AWSProton-worker-lambda-s-worker-lambda-s-cloudformation-MySqsQueue-U5YMDp8VFYEJ",
            "awsRegion": "us-east-2"
        }
    ]
}

INFO	Context:  
{
    "callbackWaitsForEmptyEventLoop": true,
    "functionVersion": "$LATEST",
    "functionName": "worker-lambda-svc-prod-function",
    "memoryLimitInMB": "512",
    "logGroupName": "/aws/lambda/worker-lambda-svc-prod-function",
    "logStreamName": "2022/05/01/[$LATEST]6d56308e4e9344168158554db14e720e",
    "invokedFunctionArn": "arn:aws:lambda:us-east-2:XXXXXXXXXXXX:function:worker-lambda-svc-prod-function",
    "awsRequestId": "06831dc6-8bfd-5d2a-9f9a-472e44e198a5"
}

INFO	
{
    "Type": "Notification",
    "MessageId": "76f49e3f-97eb-5e9f-8645-c4d758c3d592",
    "TopicArn": "arn:aws:sns:us-east-2:XXXXXXXXXXXX:AWSProton-vpc-env-prod-cloudformation--QYWPQLSESXEMRBY-ping",
    "Subject": "New message from publisher",
    "Message": "Message 3x3txhl9i2 sent at Sun May 01 2022 18:09:44 GMT+0000 (Coordinated Universal Time)",
    "Timestamp": "2022-05-01T18:09:44.076Z",
    "SignatureVersion": "1",
    "Signature": "G6ef1WJyfFGgHS8dh1sHCjruxIs0A1D0dbpb67rFvUOWYiR8K5oWk4HgMTQ4UrGVUKLtRhwFF9UNVSYINePm9M/KmYhKLldDtg0VzBTJ90uu98XunFFeeSuS/Jw6zilBhIOKV+Bveq+s0FrmJDmrXx9N7yOkruD/azVUd/o1k+QSqlpkRqT5pDW2eVIHFnjn2uKEaZjDR71sCAuhlzXmlNOuFMMvc6OSVqvHfGnhnQJVOfYSJwNKCpXR6Y1F0+i2ubDIEjQHGi6qvYsRFlkpRdS2jJA0xsad6nwecH8bWPgQ+O0l0z63HJDw+ghGyl7kM+3RfRPpSwNsZhLMeL/frA==",
    "SigningCertURL": "https://sns.us-east-2.amazonaws.com/SimpleNotificationService-7ff5318490ec183fbaddaa2a969abfda.pem",
    "UnsubscribeURL": "https://sns.us-east-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-2:XXXXXXXXXXXX:AWSProton-vpc-env-prod-cloudformation--QYWPQLSESXEMRBY-ping:dc8974a0-3710-4b29-a078-7d0d5f53c844"
}