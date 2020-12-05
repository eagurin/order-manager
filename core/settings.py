import os
from django.db import connections
import multidb

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'l(h8q13ckxly)09oj6!94*sbpklxz#b1c=)!+(o55-^46(-lmt'

DEBUG = True

ALLOWED_HOSTS = ['*', 'localhost', '127.0.0.1']

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rangefilter',
    'djmoney',
    'main',
]

MIDDLEWARE = [
    'multidb.middleware.PinningRouterMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

MULTIDB_PINNING_SECONDS = 5
MULTIDB_PINNING_COOKIE = 'multidb_pin_writes'

ROOT_URLCONF = 'core.urls'

TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
}

# DATABASES = {
#     'default': {
# 	    'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'mysql',
	    # 'USER': 'goldme6j_testdj',
	    # 'PASSWORD': 'Ju%k9DBc',
	    # 'HOST': 'localhost',
	    # 'OPTIONS': {
        #     'init_command': "SET sql_mode='STRICT_TRANS_TABLES', innodb_strict_mode=1",
        #     'charset': 'utf8mb4',
        #     "autocommit": True,
        # },
    # },
    # 'postgresql': {
    #     'NAME': 'postgresql',
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'USER': 'postgres_user',
    #     'PASSWORD': 'password'
    # },
    # 'mssql': {
    #     'NAME': 'mssql',
    #     'ENGINE': 'sql_server.pyodbc',
    #     'USER': 'mssql_user',
    #     'PASSWORD': 'password'
    # },
    # 'mysql_gis': {
    #     'NAME': 'mysql_gis',
    #     'ENGINE': 'django.contrib.gis.db.backends.mysql',
    #     'USER': 'mysql_gis_user',
    #     'PASSWORD': 'password'
    # },
    # 'spatialite': {
    #     'NAME': 'spatialite',
    #     'ENGINE': 'django.contrib.gis.db.backends.spatialite',
    #     'USER': 'spatialite_user',
    #     'PASSWORD': 'password'
    # },
    # 'oracle': {
    #     'NAME': 'oracle',
    #     'ENGINE': 'django.db.backends.oracle',
    #     'USER': 'oracle_user',
    #     'PASSWORD': 'password'
    # },
    # 'oracle_gis': {
    #     'NAME': 'oracle_gis',
    #     'ENGINE': 'django.contrib.gis.db.backends.oracle',
    #     'USER': 'oracle_gis_user',
    #     'PASSWORD': 'password'
    # },
    # 'redshift': {
    #     'NAME': 'redshift',
    #     'ENGINE': 'django_redshift_backend',
    #     'USER': 'redshift_user',
    #     'PASSWORD': 'password'
    # }
# }

# REPLICA_DATABASES = ['mysql', 'postgresql', 'mssql', 'mysql_gis', 'spatialite', 'oracle', 'oracle_gis', 'redshift']
# DATABASE_ROUTERS = ('multidb.ReplicaRouter',)
# connection = connections[multidb.get_replica()]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

CURRENCIES = ('USD', 'RUB', 'EUR')
LANGUAGE = "en"
LANGUAGE_CODE = "en"
TIME_ZONE = "Europe/London"
DATETIME_FORMAT = 'd-m-Y'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

JAZZMIN_SETTINGS = {
    "site_logo": "vendor/adminlte/img/AdminLTELogo.png",
    "welcome_sign": "Welcome",
    "copyright": "",
    "search_model": None,
    "user_avatar": "avatar",
    "topmenu_links": [],
    "usermenu_links": [],
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": [],
    "custom_links": {},
        "icons": {"auth": "fas fa-users-cog", "auth.user": "fas fa-user", "auth.Group": "fas fa-users", "main": "fas fa-money-check-alt", "main.Order": "fas fa-check-square", "main.Agent": "fas fa-building"},
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    "related_modal_active": False,
    "custom_css": None,
    "custom_js": None,
    "show_ui_builder": False,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {},
    "language_chooser": False,
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": True,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "dark_mode_theme": None,
    "actions_sticky_top": True,
}
