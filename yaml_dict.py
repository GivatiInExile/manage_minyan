#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 14:43:27 2019

@author: daniellandesman
"""
import quickstart
from config import *
from collections import defaultdict
import yaml

path = r'%s' % YAML_ADDR

def store_yaml(id_dict):
        with open(path, 'w') as file:
                documents = yaml.dump(id_dict, file)


def load_yaml():
    with open(path, 'w') as file:
        documents = yaml.full_load(file)

    return documents
    for item, doc in documents.items():
            print(item, ":", doc)