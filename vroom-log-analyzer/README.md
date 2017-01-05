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

Here how LogRecordReader works. [The source is here](log_record_reader.py)

1. the public method is `get_records`. 
2. The `get_records` takes lines from `get_lines`, filter them by regexp and returns using python generators (yield)
3. The `get_lines` takes decoded chunks from `get_decoded_chunks`, split them by lines and returns using generator.
4. The `get_decoded_chunks` gets chunks from `get_chunks`, decodes them using `zlib` library and returns using generator.
5. `get_chunks` reads chunks of data from S3 file.

## Class Diagram
![Class Diagram](LogAnalyser.png)
