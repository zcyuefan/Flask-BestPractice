#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    main.views
    -----------------------------
    DESCRIPTION  
    :copyright: (c) 2018 by zcyuefan.
    :license: LICENSE_NAME, see LICENSE_FILE for more details.
"""
from . import main
from flask import render_template, flash, url_for
from markupsafe import Markup
from flask_security import login_required


class CarouselItem:
    def __init__(self, caption, a_href, img_src, active=False):
        self.caption = caption
        self.a_href = a_href
        self.img_src = img_src
        self.active = active


@main.route('/')
def index():
    flash('Hi welcome')
    flash(Markup(
        '<strong>Oh snap!</strong> <a href="#" class="alert-link"> Change a few things up</a> and try submitting again.'),
          'danger')
    carousel_items = [
        CarouselItem(caption='First', a_href='http://www.baidu.com', img_src=url_for('static', filename='timg.jpg'),
                     active=True),
        CarouselItem(caption='Second', a_href='http://www.baidu.com', img_src=url_for('static', filename='timg.jpg')),
        CarouselItem(caption='Third', a_href='http://www.baidu.com', img_src=url_for('static', filename='timg.jpg'))]
    return render_template('index.html', carousel_items=carousel_items)


@main.route('/products')
@login_required
def products():
    return 'Haha'
    # return render_template('index.html')


@main.route('/about')
def about():
    return 'TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT'
    # return render_template('index.html')
