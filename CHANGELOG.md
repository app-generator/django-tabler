# Change Log

## [1.0.1] 2021-01-20
### Improvements

- Bump Django Codebase to [v2stable.0.1](https://github.com/app-generator/boilerplate-code-django-dashboard/releases)
- Dependencies update (all packages) 
  - Django==4.0.1
- Settings update for Django 4.x
  - `New Parameter`: CSRF_TRUSTED_ORIGINS
    - [Origin header checking isn`t performed in older versions](https://docs.djangoproject.com/en/4.0/ref/settings/#csrf-trusted-origins)  

## Unreleased
### Bug fixes

- Patch [#1 - Whitenoise Fix](https://github.com/app-generator/django-dashboard-tabler/issues/1)
    - WhiteNoiseMiddleware must be positioned right after SecurityMiddleware
    - Impacted file: [core/settings.py](https://github.com/app-generator/django-dashboard-tabler/blob/master/core/settings.py) / MIDDLEWARE section

## [1.0.0] 2020-01-14
### Initial Release
