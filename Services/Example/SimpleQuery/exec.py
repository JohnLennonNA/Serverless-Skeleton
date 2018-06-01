#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json, sys, os
map(lambda x: sys.path.append('.libs/' + x + '/'), os.listdir(".libs/"))

import MySQLdb

def main(event, context):

    try:
        db = MySQLdb.connect(
            host=os.environ['MYSQL_HOST'],
            user=os.environ['MYSQL_USER'],
            passwd=os.environ['MYSQL_PASS'],
            db=os.environ['MYSQL_DB']
        )

        ## CREATE A CURSOR TO WALK IN THE RESULT
        cur = db.cursor()

        ## EXECUTE THE QUERY ON DATABASE
        cur.execute("SELECT * FROM portal_cancelamento_item " \
                    "ORDER BY id DESC LIMIT 10")

        ## CREATE A EMPTY LIST TO ADD SOME DICTS AND CREATE A LIST OF DICTS
        response = []

        ## WALK IN THE RESULTS TO ADD THE DICT ON THE LIST
        for row in cur.fetchall():
            response.append({
                "field" : row[0],
                "field2": row[1]
            })

        return {
            "statusCode": 200,
            "body": json.dumps(response) ## CONVERT THE LIST OF DICTS TO JSON AND RETURN TO CLIENT
        }
    except ValueError:
        return {
            "statusCode": 500,
            "body": json.dumps(ValueError)  ## CONVERT THE LIST OF DICTS TO JSON AND RETURN TO CLIENT
        }