/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

// 1. Receive event from SQS Queue.
// 2. Log event and context object to CloudWatch Logs.
// 3. Log SQS message to CloudWatch Logs. 
// 3. Return a null response.

const AWS = require('aws-sdk')
AWS.config.region = process.env.AWS_REGION 

exports.handler = async (event, context) => {
  try {
    // Log event and context object to CloudWatch Logs
    console.log("Event: ", JSON.stringify(event, null, 2));
    console.log("Context: ", JSON.stringify(context, null, 2));
    event.Records.forEach(record => {
      const { body } = record;
      console.log(body);
    });
    return {};
  } catch (error) {
    console.error(error);
    throw new Error(error);
  }
};