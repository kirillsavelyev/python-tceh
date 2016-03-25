# -*- coding: utf-8 -*-

import json
import jsonschema
from datetime import datetime
from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/api/<ver_api>/order', methods=['POST'])
def api(ver_api):
    try:
        with open('schems' + ver_api + '.json', mode='r') as val_schem:
