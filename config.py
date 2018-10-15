#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    config.py
    -----------------------------
    Flask Configuration Classes
    :copyright: (c) 2018 by zcyuefan.
    :license: LICENSE_NAME, see LICENSE_FILE for more details.
"""

import os

# Get the app root path
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # App Settings
    APP_NAME = 'Flask Blog'

    # Flask Settings
    # See http://flask.pocoo.org/docs/1.0/config/#builtin-configuration-values
    DEBUG = False
    TESTING = False

    # Auth, mail, form
    # Flask-Security, Flask-Login, Flask-Mail, Flask-WTF
    # generate a random string:
    # from base64 import b64encode
    # from os import urandom
    # print(b64encode(urandom(64)).decode('utf-8'))
    SECRET_KEY = 'Ot6hv8TsudpUvG+tTEmNikfFK05a4HM1gTx9W1PEfxtCtEpz3jbg2ODgESzllJo4fXpdvzBpj/n9fGCG1XtSDQ=='
    # login activities
    SECURITY_TRACKABLE = True
    # password
    SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
    SECURITY_PASSWORD_SALT = 'YaHIpdai23Im'
    # register
    SECURITY_REGISTERABLE = True
    SECURITY_CHANGEABLE = True
    SECURITY_SEND_REGISTER_EMAIL = False

    # Third-party security
    # Flask-OAuthlib

    # Databases
    # Flask-SQLAlchemy
    # For SQLite:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + basedir + '/' + \
                              'fbp.sqlite'

    # This option will be removed as soon as Flask-SQLAlchemy removes it.
    # At the moment it is just used to suppress the super annoying warning
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # This will print all SQL statements
    SQLALCHEMY_ECHO = False

    # i18n
    # Flask-Babel

    # Flask-Admin

    # Flask-Bootstrap
    BOOTSTRAP_WEB_CDN_BASE_URLS = {
        'bootstrap': '//cdn.bootcss.com/bootstrap/3.3.7/',
        'jquery': '//cdn.bootcss.com/jquery/1.12.4/',
        'html5shiv': '//cdn.bootcss.com/html5shiv/3.7.3/',
        'respond': '//cdn.bootcss.com/respond.js/1.4.2/',
        'bootswatch': '//cdn.bootcss.com/bootswatch/3.3.7/cerulean/',
        'font-awesome': '//cdn.bootcss.com/font-awesome/4.7.0/',
    }

    # Logging
    # If set to a file path, this should be an absolute file path
    LOG_CONF_FILE = None

    # If set to a file path, this should be an absolute path
    LOG_PATH = os.path.join(basedir, 'logs')

    LOG_DEFAULT_CONF = {
        'version': 1,
        'disable_existing_loggers': False,

        'formatters': {
            'standard': {
                'format': '%(asctime)s [%(levelname)s] [%(threadName)s:%(thread)d] [%(name)s] '
                          '[%(module)s:%(funcName)s] [Line:%(lineno)d]- %(message)s'
            },
        },

        'handlers': {
            'console': {
                'level': 'DEBUG',
                'formatter': 'standard',
                'class': 'logging.StreamHandler',
            },
            'debuglog': {
                'level': 'DEBUG',
                'formatter': 'standard',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(LOG_PATH, 'debug.log'),
                'mode': 'a',
                'maxBytes': 10485760,  # 10MB
                'backupCount': 5,
            },
            'infolog': {
                'level': 'INFO',
                'formatter': 'standard',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(LOG_PATH, 'info.log'),
                'mode': 'a',
                'maxBytes': 10485760,  # 10MB
                'backupCount': 5,
            },
            'errorlog': {
                'level': 'ERROR',
                'formatter': 'standard',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(LOG_PATH, 'error.log'),
                'mode': 'a',
                'maxBytes': 10485760,  # 10MB
                'backupCount': 5,
            }
        },

        'loggers': {
            'flask.app': {
                'handlers': ['console', 'infolog', 'errorlog'],
                'level': 'DEBUG',
                'propagate': True
            },
            'anotherlogger': {
                'handlers': ['debuglog'],
                'level': 'DEBUG',
                'propagate': True
            },
        }
    }

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    # ASSETS_DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'dev.sqlite')

    @classmethod
    def init_app(cls, app):
        print('THIS APP IS IN DEBUG MODE. \
                YOU SHOULD NOT SEE THIS IN PRODUCTION.')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'test.sqlite')
    # WTF_CSRF_ENABLED = False

    @classmethod
    def init_app(cls, app):
        print('THIS APP IS IN TESTING MODE.  \
                YOU SHOULD NOT SEE THIS IN PRODUCTION.')


class ProductionConfig(Config):
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}
