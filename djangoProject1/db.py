# To use Neon with Django, you have to create a Project on Neon and specify the project connection settings in your settings.py in the same way as for standalone Postgres.

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'neondb',
    'USER': 'AndrejWiseman',
    'PASSWORD': 'tq0QxBuD3cbs',
    'HOST': 'ep-autumn-silence-59904924.eu-central-1.aws.neon.tech',
    'PORT': '5432',
  }
}