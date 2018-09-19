#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import unittest
import json

sys.path.append("../src/")

from main import gerenateJsonResponse

class gerenateJsonResponseTest(unittest.TestCase):
    def test(self):

        response = gerenateJsonResponse(body={"status": "error", "message": "Message Test"}, status=500)
        self.assertTrue(("statusCode" in response))
        self.assertEqual(response['statusCode'], 500)
        self.assertTrue( ("status" in response['body'] ) )
        self.assertTrue( ("message" in response['body'] ) )

        values = json.loads(response['body'])
        self.assertEqual(values['status'], "error")
        self.assertEqual(values['message'], "Message Test")

        line = []
        line.append({123456: {"qtd": float(1)}})

        response = gerenateJsonResponse(body={
            "status": "success",
            "data": {
                "invoiceKey": 41180410490181000216550010009969571002185112,
                "products": line}}
        )

        self.assertTrue(("statusCode" in response))
        self.assertEqual(response['statusCode'], 200)
        self.assertTrue( ("status" in response['body'] ) )
        self.assertTrue( ("data" in response['body'] ) )

        values = json.loads(response['body'])
        self.assertEqual(values['status'], "success")
        self.assertEqual(len(values['data']['products']), 1)
        self.assertEqual( values['data']['products'][0]['123456']['qtd'] , 1.0)