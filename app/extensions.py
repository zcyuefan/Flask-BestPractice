#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    app.extensions
    -----------------------------
    The flask extensions used by app
    :copyright: (c) 2018 by zcyuefan.
    :license: LICENSE_NAME, see LICENSE_FILE for more details.
"""
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security
from flask_navbar import Nav
from flask_wtf import Form


# Style
bootstrap = Bootstrap()

# Database
db = SQLAlchemy()

# User management
security = Security()

# Nav bar
nav = Nav()
