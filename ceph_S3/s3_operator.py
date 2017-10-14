#!/usr/local/bin/python2.7
#coding:ut  f-8
#Authon:jethrolin 20171014


#creat connection
import boto
import boto.s3.connection
import os

#ceph info
access_key = 'X6A4AY2AV69VR2V4MH1C'
secret_key = 'Zq1QzpKBtUqxemChlnBugieJvCX9sy58nDolDByL'
rgw_host = '100.115.147.205'

conn = boto.connect_s3(
    aws_access_key_id = access_key,
    aws_secret_access_key = secret_key,
    host = rgw_host,
    #is_secure=False,               # uncomment if you are not using ssl
    calling_format = boto.s3.connection.OrdinaryCallingFormat(),
)

#show all buckets,example:
# mahbuckat1   2011-04-21T18:05:39.000Z
# mahbuckat2   2011-04-21T18:05:48.000Z

for bucket in conn.get_all_buckets():
    print "{name}\t{created}".format(
        name = bucket.name,
        created = bucket.creation_date,
    )

#create a new bucket
bucket = conn.create_bucket('test-bucket')

i = 0
for i in range(1,10):
    bucket = conn.create_bucket("aiautopilot-i"),



#show objects in buckert,examples :
#myphoto1.jpg 251262  2011-08-08T21:35:48.000Z
#myphoto2.jpg 262518  2011-08-08T21:38:01.000Z

for key in bucket.list():
    print "{name}\t{size}\t{modified}".format(
        name = key.name,
        size = key.size,
        modified = key.last_modified,
    )

#delete bucket,can not delete an un-null bucket
conn.delete_bucket(bucket.name)


#create a new object

key = bucket.new_key('hello.txt')
key.set_contents_from_string('Hello World!')

#download an object

key = bucket.get_key('perl_poetry.pdf')
key.get_contents_to_filename('/home/larry/documents/perl_poetry.pdf')

#delete an ohject
bucket.delete_key('goodbye.txt')