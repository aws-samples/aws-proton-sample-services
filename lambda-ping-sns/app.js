/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

// 1. Receive event from API Gateway HTTP API.
// 2. Log event and context object to CloudWatch Logs.
// 3. Send SNS message and log results to CloudWatch Logs. 
// 3. Return a response with event information and SNS message to the caller.

const AWS = require('aws-sdk')
AWS.config.region = process.env.AWS_REGION 
const sns = new AWS.SNS({apiVersion: '2012-11-05'})

exports.handler = async (event, context) => {
  try {
    // Log event and context object to CloudWatch Logs
    console.log("Event: ", JSON.stringify(event, null, 2));
    console.log("Context: ", JSON.stringify(context, null, 2));
    sns_message = (Math.random()+1).toString(36).slice(2);
    date = Date();

    // Create event object to return to caller
    const eventObj = {
      functionName: context.functionName,
      SNS_Message: `Message ${sns_message} sent at ${date}`,
      SNS_Subject: 'New message from publisher',
    };

    // Params object for SNS
    const params = {
      Message: `Message ${sns_message} sent at ${date}`,
      Subject: 'New message from publisher',
      TopicArn: process.env.SNSTopicArn
    };
    
    // Send to SNS
    const result = await sns.publish(params).promise();
    console.log(result);

    const response = {
      statusCode: 200,
      body: JSON.stringify(eventObj, null, 2),
    };
    return response;
  } catch (error) {
    console.error(error);
    throw new Error(error);
  }
};