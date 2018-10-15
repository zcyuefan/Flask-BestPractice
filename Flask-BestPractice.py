#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Flask-BestPractice.py
    -----------------------------
    extended command line
    run `export FLASK_APP=Flask-BestPractice.py` first, `set FLASK_APP=Flask-BestPractice.py` on windows instead
    use `flask db [command]` to manage your app database. see Flask-Migrate doc for more info.
    :copyright: (c) 2018 by zcyuefan.
    :license: LICENSE_NAME, see LICENSE_FILE for more details.
"""

import os
import click
from flask_migrate import Migrate
from app import create_app, db

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


@app.cli.command()
def create_user():
    """Create a user to test."""
    from app.user.models import user_datastore
    user_datastore.create_user(email='123@abc.com', password='password')
    user_datastore.commit()
