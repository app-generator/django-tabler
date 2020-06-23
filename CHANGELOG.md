# Change Log

## Unreleased
### Bug fixes

- Patch [#1 - Whitenoise Fix](https://github.com/app-generator/django-dashboard-tabler/issues/1)
    - WhiteNoiseMiddleware must be positioned right after SecurityMiddleware
    - Impacted file: [core/settings.py](https://github.com/app-generator/django-dashboard-tabler/blob/master/core/settings.py) / MIDDLEWARE section

## [1.0.0] 2020-01-14
### Initial Release
