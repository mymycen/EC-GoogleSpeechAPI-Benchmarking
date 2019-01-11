#! usr/bin/env python

import argparse
import os
import sys
import Transcribe as t
import json


def start():
    parse = argparse.ArgumentParser()
    parse.add_argument("-bucket", help="Location of bucket")
    parse.add_argument("-files", help="File containing the list of file names")
    parse.add_argument("-ref", help="Reference.json file")
    parse.add_argument("-out", help="Path of output file")

    args = parse.parse_args()

    if args.bucket is not None:
        bucket_loc = args.bucket
    if args.files is not None:
        files = args.files
    if args.ref is not None:
        reference = args.ref
    if args.out is not None:
        out = args.out

    # print("bucket: ", bucket_loc)
    # print("files: ", files)
    # print("reference :", reference)

    if os.path.exists(files):
        with open(files,'r') as f:
            for line in f:
                for currentline in line.split(","):
                    uri = bucket_loc+"/"+currentline

    # with open("api-key.json") as f:
    #     str = f.read()
    # os.environ["GOOGLE_CLOUD_SPEECH_CREDENTIALS"]="/home/ananya/Downloads/google-cloud-sdk/My First Project-4b1b3700378d.json"

    # print(os.environ.get('GOOGLE_APPLICATION_CREDENTIALS'))

    t.transcribe_gcs(uri)


if __name__ == '__main__':
    start()