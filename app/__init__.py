#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    __init__.py
    -----------------------------
    flask best practice
    :copyright: (c) 2018 by zcyuefan.
    :license: LICENSE_NAME, see LICENSE_FILE for more details.
"""
from config import config
from flask import Flask
from .extensions import (
    bootstrap,
    db,
    nav,
    security
)


def create_app(config_name):
    """
    create the app
    :return: Flask app
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Override configuration
    # Get config from envvar
    app.config.from_envvar("FBP_SETTINGS", silent=True)

    # Register blueprint
    configure_blueprints(app)

    # Load extensions
    configure_extensions(app)

    # Set logging
    configure_logging(app)

    return app


def configure_blueprints(app):
    """
    register blueprint
    :param app: flask app
    :return:
    """
    from .main.views import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/')


def configure_extensions(app):
    """
    init extensions
    :param app: flask app
    :return:
    """
    bootstrap.init_app(app)
    configure_bootstrap_cdns(app)

    db.init_app(app)

    configure_nav(app, nav)
    nav.init_app(app)

    # Setup Flask-Security
    from .user.models import user_datastore
    security.init_app(app, user_datastore)


def configure_logging(app):
    """
    init logging
    :param app: flask app
    :return:
    """
    from logging import config as logging_config
    if app.config.get("LOG_DEFAULT_CONF"):
        logging_config.dictConfig(app.config.get("LOG_DEFAULT_CONF"))

    if app.config.get("LOG_CONF_FILE"):
        logging_config.fileConfig(app.config.get("LOG_CONF_FILE"))

    # Other add on logger config
    pass


def configure_bootstrap_cdns(app):
    from flask_bootstrap import ConditionalCDN, WebCDN
    static = app.extensions['bootstrap']['cdns']['static']
    local = app.extensions['bootstrap']['cdns']['local']

    def get_cdn(key, primary=static):
        base_url = app.config.get('BOOTSTRAP_WEB_CDN_BASE_URLS').get(key)
        if base_url:
            web_cdn = WebCDN(base_url)
            return ConditionalCDN('BOOTSTRAP_SERVE_LOCAL', primary, web_cdn)
        else:
            return None

    for i in ['bootstrap', 'jquery']:
        cdn = get_cdn(i, local)
        if cdn:
            app.extensions['bootstrap']['cdns'].update(**{i: cdn})

    for i in ['html5shiv', 'respondjs', 'bootswatch', 'font-awesome']:
        cdn = get_cdn(i)
        if cdn:
            app.extensions['bootstrap']['cdns'].update(**{i: cdn})


def configure_nav(app, app_nav):
    from flask_security import current_user
    # from flask_nav import register_renderer
    from flask_navbar.elements import Navbar, View, Subgroup, Separator, Link, Text, RawTag, NavUl, Search

    def top_nav():
        search = Search('/search', navbar_right=False, icon='fa fa-search', btn_text=None,
                        input_placeholder='Search...', input_name='q', input_id='q', )

        if current_user.is_authenticated:
            right_nav = NavUl(
                View('Post', 'security.logout', icon='fa fa-edit'),
                Subgroup(
                    'Hi, ' + current_user.email,
                    View('Change Password', 'security.change_password'),
                    Separator(),
                    View('Help', 'security.logout'),
                    View('Feedback', 'security.logout'),
                    View('Logout', 'security.logout', icon='fa fa-sign-out'),
                ),
                RawTag('<li><a href="{url}">{text} <span class="badge">{count}</span></a></li>'.format(url='#',
                                                                                                       text='',
                                                                                                       count='10')),
                navbar_right=True
                )
        else:
            right_nav = NavUl(
                View('Login', 'security.login'),
                View('Register', 'security.register'),
                navbar_right=True
            )

        return Navbar(
            View(app.config.get('APP_NAME'), 'main.index'),
            NavUl(
                View('Home', 'main.index'),
                Link('Github', 'https://github.com/zcyuefan/flask-bestpractice'),
                navbar_right=False
            ),
            search,
            right_nav,
            # navbar_inverse=True,
            # navbar_fixed='top',
        )

    app_nav.register_element('top', top_nav)
    # register_renderer(app, 'ext_bootstrap', ExtBootstrapRenderer)
