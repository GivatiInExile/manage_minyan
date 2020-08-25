#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 14:43:27 2019

@author: daniellandesman
"""
import quickstart
import config
from collections import defaultdict
import yaml


def store_yaml(id_dict):
    #with open(r'E:\data\store_file.yaml', 'w') as file:
    with open(r'/Users/daniellandesman/minyan_poetry/manage_minyan/email_id.yaml', 'w') as file:
        documents = yaml.dump(id_dict, file)

def load_yaml():
    #with open(r'E:\data\store_file.yaml') as file:
    with open(r'/Users/daniellandesman/minyan_poetry/manage_minyan/email_id.yaml') as file:
        documents = yaml.full_load(file)

    return documents
    for item, doc in documents.items():
            print(item, ":", doc)