# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

from . import themeConfig


class PyScadaThemeConfig(AppConfig):
    name = 'pyscada.'  + themeConfig.name
    verbose_name = _("PyScada "  + themeConfig.nameCamel)
    path = os.path.dirname(os.path.realpath(__file__))
    default_auto_field = 'django.db.models.AutoField'
