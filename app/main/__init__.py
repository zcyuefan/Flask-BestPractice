#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    __init__.py
    -----------------------------
    $DESCRIPTION$ $END$ 
    :copyright: (c) 2018 by zcyuefan.
    :license: LICENSE_NAME, see LICENSE_FILE for more details.
"""
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views
