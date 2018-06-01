#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json, sys, os, urllib
map(lambda x: sys.path.append('.libs/' + x + '/'), os.listdir(".libs/"))

from PyPDF2 import PdfFileMerger, PdfFileWriter, PdfFileReader
from StringIO import StringIO

import glob
import zipfile

def main(event, context):

    try:
        memoryFile = StringIO(urllib.urlopen('URL OF THE FILE').read())
        unzipFile(memoryFile, "/tmp/")
        memoryFile.close()

        print "File unziped"

        output = PdfFileWriter()
        totalFiles = len(glob.glob("/tmp/*.pdf"))

        flag = 0
        files = []

        for x in glob.glob("/tmp/*.pdf"):
            files.append(PdfFileReader(file(x, 'rb')))

            print x

            if len(files) == 2:
                page = files[0].getPage(0)
                page.mergeTranslatedPage(files[1].getPage(0), 0,150, True)
                output.addPage(page)
                files = []

            flag += 1

            if  ( totalFiles % 2 ) != 0 & flag == ( len(glob.glob("/tmp/*.pdf")) - 1):
                page = files[0].getPage(0)
                output.addPage(page)

        outputStream = file("/tmp/document-output.pdf", "wb")
        output.write(outputStream)
        outputStream.close()

        print "End process"

        return {
            "statusCode": 200,
            "body": json.dumps({"message":"sucess"}) ## CONVERT THE LIST OF DICTS TO JSON AND RETURN TO CLIENT
        }
    except ValueError:

        print ValueError

        return {
            "statusCode": 500,
            "body": json.dumps(ValueError)  ## CONVERT THE LIST OF DICTS TO JSON AND RETURN TO CLIENT
        }

def unzipFile(pathFile, pathToStore):
    zip_ref = zipfile.ZipFile(pathFile, 'r')
    zip_ref.extractall(pathToStore)
    zip_ref.close()