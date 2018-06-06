#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json, os, sys

list(map(lambda x: sys.path.append('.libs/' + x ), os.listdir(".libs/")))

import requests

def main(event, context):

    try:
        payload = {
                "query": {
                    "match": {
                        "context.id": {
                            "query": event["pathParameters"]["idOrder"],
                            "type": "phrase"
                        }
                    }
                }
            }

        headers = {'content-type': 'application/json'}
        r = requests.post(os.environ['URL_ELASTIC'], data=json.dumps(payload), headers=headers )

        return {
            "statusCode": 200,
            "body": r.content
        }
    except Exception as e:
        e = sys.exc_info()[0]
        print e