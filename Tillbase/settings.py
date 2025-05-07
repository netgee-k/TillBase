STATIC_URL = '/static/'
INSTALLED_APPS = [
    'bootstrap4',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # your custom app
    'main',
]


DEBUG = True
LOGIN_REDIRECT_URL = '/dashboard/'  # This is the URL to redirect to after login
ROOT_URLCONF = 'Tillbase.urls'
SECRET_KEY = 'k*oz=3!08d!bb14z-&6i!6yl9*^+^+@!75vx2@iv-v7m*i7fy&'
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  
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


DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'tillbase',
        'ENFORCE_SCHEMA': True,
        'CLIENT': {
            'host': 'mongodb+srv://jesse:kimani@tillbase.zg83hlp.mongodb.net/?retryWrites=true&w=majority&appName=tillbase'
        }
    }
}
