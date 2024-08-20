
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-x+n*1(5)o)#uhrh0gi4$%@zp+rb*ot(9u(j8q6$!6q85hn9(+z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',   
    'ce2024',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',  # Substitua pelo nome do seu banco de dados
        'USER': 'postgres.hykxrdvswwazjqtjjtxu',            # Substitua pelo nome do usuário do banco de dados
        'PASSWORD': 'Wceninha@090928',       # Substitua pela senha do usuário do banco de dados
        'HOST': 'aws-0-sa-east-1.pooler.supabase.com',   # Substitua pelo host do Supabase
        'PORT': '6543',   # A porta padrão do Postgres
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR/"static"]


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


JAZZMIN_SETTINGS = {
 "site_title"  : "DENCIO TRINDADE",
 "site_header" : "DT - 47700",
 "site_brand"  : "DT 47700 - ADMIN",
 "site_logo"   : "dt_foto.jpeg",
 "login_logo"  : "logo_270.jpg",

 'icons': {
    'auth': 'fas fa-users-cog',
    'auth.user': 'fas fa-user',
    'auth.Group': 'fas fa-users',
    #'popets.usuario': 'fas fa-copyright',
    #'popets.usuariotipo': 'fas fa-object-group',
 },


 'welcome_sign': 'Bem-vindo(a)',
 'copyright': 'DB SERVICOS TECNOLOGICOS',
 #'search_model': ['popets.usuario','popets.petperfil',],
 #'show_ui_builder': True,
 "user_avatar": None,

 # Links to put along the top menu
    "topmenu_links": [

        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},        
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},        
        {"model": "auth.User"},        
        {"app": "books"},
    ],

 "show_sidebar": True,
 "navigation_expanded": False,
 "hide_apps": [],
 "hide_models": ['auth.Group'],
 "order_with_respect_to": [],




    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

     #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,

    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to link font from fonts.googleapis.com (use custom_css to supply font otherwise)
    "use_google_fonts_cdn": True,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,

 

     ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    # Add a language dropdown into the admin
    "language_chooser": False,

}
