# Change Log

## [1.0.5] 2024-11-27
### Changes

> Update RM Links

- 👉 [Django Tabler](https://app-generator.dev/product/tabler/django/) - `Product Page`
- 👉 [Django Tabler Documentation](https://app-generator.dev/docs/products/django/tabler/index.html) - `Complete Information` and Support Links
  - [Getting Started with Django](https://app-generator.dev/docs/technologies/django/index.html) - a `comprehensive tutorial`
  - `Configuration`: Install Dependencies, Prepare Environment, Setting up the Database 
  - `Start with Docker`
  - `Manual Build`
  - `Start the project`
  - `Deploy on Render`

## [1.0.4] 2024-03-09
### Changes

- Deprecate `distutils`
  - use `str2bool`
- Update Deps 
  - `requirements.txt`  
- Update README: [PRO Version](https://appseed.us/product/volt-dashboard-pro/django/), List features
  - `API`, **Charts** 
  - **DataTables** (Filters, Export)
  - **Celery**
  - **Media Files Manager**
  - **Extended User Profiles**
- Update [Custom Development](https://appseed.us/custom-development/) Section
  - New Pricing: `$3,999`

## [1.0.3] 2023-05-30
### Changes

- Update DEMO: [Django Tabler](https://django-tabler.onrender.com/)
  - Deployed on `Render`

## [1.0.2] 2023-05-29
### Changes

- Move to theme-based pattern
  - [Django Tabler Admin](https://github.com/app-generator/django-admin-tabler)
- 🚀 `Deployment` 
  - `CI/CD` flow via `Render`

## [1.0.1] 2021-01-20
### Changes

- Bump Django Codebase to [v2stable.0.1](https://github.com/app-generator/boilerplate-code-django-dashboard/releases)
- Dependencies update (all packages) 
  - Django==4.0.1
- Settings update for Django 4.x
  - `New Parameter`: CSRF_TRUSTED_ORIGINS
    - [Origin header checking isn`t performed in older versions](https://docs.djangoproject.com/en/4.0/ref/settings/#csrf-trusted-origins)  

## Unreleased
### Changes

- Patch [#1 - Whitenoise Fix](https://github.com/app-generator/django-dashboard-tabler/issues/1)
    - WhiteNoiseMiddleware must be positioned right after SecurityMiddleware
    - Impacted file: [core/settings.py](https://github.com/app-generator/django-dashboard-tabler/blob/master/core/settings.py) / MIDDLEWARE section

## [1.0.0] 2020-01-14
### Changes
