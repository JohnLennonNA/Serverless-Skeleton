#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json, os, sys

if os.path.isdir(".libs/"):
    list(map(lambda x: sys.path.append(".libs/" + x ), os.listdir(".libs/")))

    import requests

def main(event, context):
    try:
        return gerenateJsonResponse(body={"status": "success", "data": "ok"})
    except Exception as e:
        db.close()
        return gerenateJsonResponse(body={"status": "error", "message": str(e)}, status=500)

def gerenateJsonResponse(body, status = 200):
    print("ERRO " + str(status) + " - " + str(json.dumps(body)))
    return { "statusCode": status, "body": json.dumps(body)}