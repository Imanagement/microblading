
"""
Django settings for conf project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_8y5zm4d+(chr3gan22-u@0$kzzavu14xilffa)!$6dy^2)3*5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'djangocms_admin_style',
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # applications
    'appointments',
    'blog',
    'conf',
    'core',
    'portfolio',
    'services',
    'shop',
    'testimonials',
    # third-app applications
    'cms',
    'djangocms_icon',
    'djangocms_link',
    'djangocms_text_ckeditor',
    'django.contrib.sites',
    'easy_thumbnails',
    'filer',
    'menus',
    'mptt',
    'pipeline',
    'sekizai',
    'silk',
    "translation_manager",
    'treebeard',

]

MIDDLEWARE = [
    'silk.middleware.SilkyMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
]

ROOT_URLCONF = 'conf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sekizai.context_processors.sekizai',
            ],
        },
    },
]

WSGI_APPLICATION = 'conf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres_db_4',
        'HOST': 'db',
        'USER': 'postgres_user',
        'PASSWORD': 'postgres_pass',
    }
}

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
#         'LOCATION': 'my_cache_table',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

gettext = lambda s: s
# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/
CMS_LANGUAGES = {
    ## Customize this
    1: [
        {
            'code': 'en',
            'name': gettext('en'),
            'redirect_on_fallback': True,
            'public': True,
            'hide_untranslated': False,
        },
        {
            'code': 'es',
            'name': gettext('es'),
            'redirect_on_fallback': True,
            'public': True,
            'hide_untranslated': False,
        },
    ],
    'default': {
        'redirect_on_fallback': True,
        'public': True,
        'hide_untranslated': False,
    },
}
LANGUAGE_CODE = 'en'
LANGUAGES = [
    ('en', gettext('en')),
    ('es', gettext('es')),
    ('ru', gettext('ru'))
]

MODELTRANSLATION_LANGUAGES = ('en', 'es')

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

TRANSLATIONS_PROJECT_BASE_DIR = BASE_DIR
TRANSLATIONS_ALLOW_NO_OCCURRENCES = True
TRANSLATIONS_AUTO_CREATE_LANGUAGE_DIRS = False
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATICFILES_STORAGE = 'pipeline.storage.PipelineManifestStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

PIPELINE = {
    'STYLESHEETS': {
        'main': {
            'source_filenames': (
                'core/css/animate.min.css',
                'core/css/font-awesome.min.css',
                'core/css/photo_modules.css',
                'core/css/theme.css',
                'core/css/swipebox.min.css',
                'core/css/responsive.css',
                'core/css/extra.css'
            ),
            'output_filename': 'core/css/main.min.css',
            'variant': 'datauri'
        },
    },
    'JAVASCRIPT': {
        'main': {
            'source_filenames': (
                'core/js/vc_carousel.js',
                'core/js/images-loaded.js',
                'core/js/vc_transition.js',
                'core/js/jquery.isotope.min.js',
                'core/js/jquery.swipebox.min.js',
                'core/js/jquery.mousewheel.js',
                'core/js/sorting_gallery.js',
                'core/js/theme.js',
                'core/js/extra.js',
                'core/js/jquery.cookie.js',
                'core/js/slick.min.js',
                'core/js/waypoint.js',
                'core/js/circles_gallery.js',
                'core/js/flow_gallery.js',
                'core/js/fs_gallery.js',
                'core/js/gt3_promo_block.js',
                'core/js/jquery.event.swipe.js',
                'core/js/kenburns.js',
                'core/js/nivo.js',
                'core/js/ribbon_gallery.js',
                'core/js/shift_gallery.js',
                'core/js/stripe_gallery.js',
            ),
            'output_filename': 'core/js/main.min.js',
        }
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CKEDITOR_UPLOAD_PATH = "uploads/"
SITE_ID = 1
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)
THUMBNAIL_HIGH_RESOLUTION = True
X_FRAME_OPTIONS = 'SAMEORIGIN'

CMS_TEMPLATES = [
    ('base.html', 'Home page template'),
]

DJANGOCMS_LINK_TEMPLATES = [
    ('accent', 'Accent'),
    ('social', 'Social'),
]

CKEDITOR_SETTINGS = {
    'language': '{{ language }}',
    'toolbar_CMS': [
        # {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
        # {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll', '-', 'Scayt']},
        # ['cmsplugins', 'cmswidget'],
        # ['Maximize', ''],
        # ['Source', '-', 'ShowBlocks'],
        # '/',
        # {'name': 'basicstyles',
        #  'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'CopyFormatting',
        #            'RemoveFormat']},
        # {'name': 'paragraph',
        #  'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
        #            'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock']},
        # {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
        # {'name': 'insert', 'items': ['Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak']},
        # '/',
        # {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize', 'lineheight']},
        # {'name': 'colors', 'items': ['TextColor', 'BGColor']},
        { 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ], 'items': [ 'Source', '-', 'Save', 'NewPage', 'ExportPdf', 'Preview', 'Print', '-', 'Templates' ] },
        { 'name': 'clipboard', 'groups': [ 'clipboard', 'undo' ], 'items': [ 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo' ] },
        { 'name': 'editing', 'groups': [ 'find', 'selection', 'spellchecker' ], 'items': [ 'Find', 'Replace', '-', 'SelectAll', '-', 'Scayt' ] },
        { 'name': 'forms', 'items': [ 'Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton', 'HiddenField' ] },
        '/',
        { 'name': 'basicstyles', 'groups': [ 'basicstyles', 'cleanup' ], 'items': [ 'Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'CopyFormatting', 'RemoveFormat' ] },
        { 'name': 'paragraph', 'groups': [ 'list', 'indent', 'blocks', 'align', 'bidi' ], 'items': [ 'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl', 'Language' ] },
        { 'name': 'links', 'items': [ 'Link', 'Unlink', 'Anchor' ] },
        { 'name': 'insert', 'items': [ 'Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe' ] },
        '/',
        { 'name': 'styles', 'items': [ 'Styles', 'Format', 'Font', 'lineheight', 'FontSize' ] },
        { 'name': 'colors', 'items': [ 'TextColor', 'BGColor' ] },
        { 'name': 'tools', 'items': [ 'Maximize', 'ShowBlocks' ] },
        { 'name': 'others', 'items': [ '-' ] },
        { 'name': 'about', 'items': [ 'About' ] },
        {'name': 'cms', 'items': [ 'cmsplugins'] }
        ],
    'toolbar_HTMLField': [
        # {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
        # {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll', '-', 'Scayt']},
        # ['cmsplugins', 'cmswidget'],
        # ['Maximize', ''],
        # ['Source', '-', 'ShowBlocks'],
        # '/',
        # {'name': 'basicstyles',
        #  'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'CopyFormatting',
        #            'RemoveFormat']},
        # {'name': 'paragraph',
        #  'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
        #            'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock']},
        # {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
        # {'name': 'insert', 'items': ['Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak']},
        # '/',
        # {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize', 'lineheight']},
        # {'name': 'colors', 'items': ['TextColor', 'BGColor']},
        {'name': 'document', 'groups': ['mode', 'document', 'doctools'],
         'items': ['Source', '-', 'Save', 'NewPage', 'ExportPdf', 'Preview', 'Print', '-', 'Templates']},
        {'name': 'clipboard', 'groups': ['clipboard', 'undo'],
         'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
        {'name': 'editing', 'groups': ['find', 'selection', 'spellchecker'],
         'items': ['Find', 'Replace', '-', 'SelectAll', '-', 'Scayt']},
        {'name': 'forms',
         'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                   'HiddenField']},
        '/',
        {'name': 'basicstyles', 'groups': ['basicstyles', 'cleanup'],
         'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'CopyFormatting',
                   'RemoveFormat']},
        {'name': 'paragraph', 'groups': ['list', 'indent', 'blocks', 'align', 'bidi'],
         'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                   'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                   'Language']},
        {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
        {'name': 'insert',
         'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
        '/',
        {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'lineheight', 'FontSize']},
        {'name': 'colors', 'items': ['TextColor', 'BGColor']},
        {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
        {'name': 'others', 'items': ['-']},
        {'name': 'about', 'items': ['About']},
        {'name': 'cms', 'items': [ 'cmsplugins'] }
    ],
    'font_names': 'Open Sans, sans-serif;Poppins, sans-serif;',
    'extraPlugins': 'font, lineheight',
    'skin': 'moono-lisa',
    'line_height': '1px;5px;10px;15px;20px;25px;30px;35px;40px;45px;50px;55px;60px;70px;80px;90px;',
    'stylesSet': [
        {'name': 'Заголовки для слайдера', 'element': 'h1', 'attributes': {'class': 'heading font-weight-700'}},
        {'name': 'Заголовок', 'element': 'h2', 'attributes': {'class': 'heading'}},
        {'name': 'Галочки', 'element': 'ul', 'attributes': {'class': 'fa-check-list'}},
        {'name': 'Квадраты', 'element': 'ul', 'attributes': {'class': 'square-list'}},
        {'name': 'Галочки в квадратах', 'element': 'ul', 'attributes': {'class': 'square-check-list'}},
    ],
    'fontSize_sizes': '2/2px;4/4px;6/6px;8/8px;10/10px;12/12px;14/14px;16/16px;18/18px;20/20px;22/22px;24/24px;26/26px;28/28px;30/30px;32/32px;34/34px;36/36px;38/38px;40/40px;42/42px;44/44px;46/46px;48/48px;50/50px;51/51px;52/52px;53/53px;54/54px;55/55px;56/56px;57/57px;58/58px;59/59px;60/60px;70/70px;72/72px;',
}