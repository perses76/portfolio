# Vroom Log Analyzer

 - **Date:** October, 2016
 - **Organization:** Vroom

Take all new files or files that have been changed from last check from S3 bucket, Unzip them, Parse by line 
and Save records matched to regexp filter into Google Store.

## Technologies
Google App Engine, Google Storage, Python, AWS, S3

## Challenges

As log file have avarage size about 40-50 mb and Google has limit 10 min for background request processing, 
we need to find the fastest way to process files.

To accomplish it, we use stream reading by chunk and python generators to return data on each level of processing.

## Class Diagram
![Class Diagram](LogAnalyser.png)
