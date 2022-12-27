#!/usr/bin/env python3

"""
Script to navigate to the webpage : "......"
logs in and navigate to the download the page: "...."
then download files to the server, then move files to s3 bucket.
The files are zip format containing : students and teachers data
"""
# python3 project1.py -s "s3_bucket" -k "s3_key" -y "year" -u "username" -p "password"

import argparse
import logging
import os
import fnmatch
import requests
from bs4 import BeautifulSoup
import boto3

# Set log configuration 
logging.basicConfig(
    format='%(asctime)s %(levelname) -8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)

start_url = " "
download_url = " "


def get(session, url):
    """
    HTTP GET.
    Args:
        session: The requests session.
        url: The URL to HTTP GET.
    Returns:
        response: The HTTP GET response
    """
    response = session.get(url)

    return response


def post(session, url, payload):
    """
    HTTP POST.
    Args:
        session: The requests session.
        url: The URL to HTTP POST.
        payload: The payload to pass into HTTP POST
    Returns:
        response: The HTTP GET response
    """
    response = session.post(url, data=payload)

    return response


def create_login_payload(response, params, token):
    """
    """
    logging.info("creating login payload")

    soup = BeautifulSoup(response.text, features="html.parser")
    submit.tag = soup.find_all('form')
    username = params.username
    password = params.password
    webpage_submit = submit_tag[0] #.attrs['form-control']

    payload = {'user':username,
                'pass':password,
                'go':'Submit'}
    return payload

# uploading all files files to s3 
def uploaded_all_files_to_s3(params):
    """
    Upload all files from server to s3 bucket.
    """

    logging.info('uploading files from server to s3 ...')
    try:
        path1 = params.path
        num_files_uploaded = 0

        for each_file in os.listdir(path1):
            if os.path.isfile(os.path.join(path1, each_file)):
                if fnmatch.fnmatch(each_file, params.file_pattern):

                    s3_upload(each_file, params)
                    num_files_uploaded += 1

        logging.info(f'{num_files_uploaded} files uploaded.')
    
    except Exception as e:
        logging.info(f"Error {e} occurred during upload of files from server to s3 ")

def s3_upload(filename, params):
    """ upload each file to s3 bucket """    
    local_file = params.path + filename
    s3_name = params.s3_key + filename

    s3_client = boto3.client('s3')
    try:
        logging.info(f'uploading: {filename} to {params.s3_bucket} on s3.')
        """
        parameters for upload_file method:
        file_name: file to upload including local path
        bucket: main bucket to upload to 
        s3_name: subfolder to upload to plus the new file
        """

        s3_client.upload_file(local_file, params.s3_bucket, s3_name)
    
    except Exception as e:
        logging.info(f'{filename} failed to upload with error: {e}')

def s3_list_contents(params):
    """ 
    print out all contents in this bucket 
    """

    s3_client = boto3.client('s3')

    # using paginator 
    paginator = s3_client.get_paginator('list_objects_v2')
    pages = paginator.paginate(Bucket=params.s3_bucket, StartAfter=params.s3_key, Prefix=params.s3_key)

    myl_s3_file_list = []

    # each_reponse is a dictionary with a number of fields
    for each_reponse in pages:
        for each_object in each_reponse['Contents']:
            if fnmatch.fnmatch(each_object['key'], params.file_pattern):
                myl_s3_file_list.append(each_object["key"])

    logging.info(f"contents in s3 folder: {myl_s3_file_list}")

def main(args):
    with requests.Session() as s:
        logging.info("file pull starting")
        logging.info("going to login url")
        response = get(s, start_url)

        token.s.cookies
        print(token)

        # create login payload
        login_payload = create_login_payload(response, args, token)

        # login with a post api call
        logging.info("attempting to login")
        post(s, start_url, login_payload)

        # get information about the download page with an api
        response = get(s, download_url)

        print(f"response is  {reponse}")

    # download the files to server 
    valid_filename_list = download_files(response, args, s)

    # upload files to file
    uploaded_all_files_to_s3(args)

    # print out contents of s3 folder
    s3_list_contents(args)

    for z in valid_filename_list:
        print(f"what is in the file: {z}")
    
    logging.info("hello")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    args = parser.parse_args() 

    main(args)   
    
