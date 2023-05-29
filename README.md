# [Django Dashboard Tabler](https://appseed.us/product/tabler/django/)

Open-source **[Django Dashboard](https://appseed.us/admin-dashboards/django)** generated by AppSeed op top of an iconic design. **Tabler** is a open-source admin template crafted by Codecalm agency. It comes with the basic components and set of pre-built pages required to lay the foundation for any application - Design provided by Codecalm.

- 👉 [Django Tabler](https://appseed.us/product/tabler/django/) - product page
- 👉 [Django tabler](https://django-dashboard-tabler.appseed.us/) - LIVE App

<br />

> Features

- ✅ `Up-to-date Dependencies`
- ✅ `Design`: [Django Theme Tabler](https://github.com/app-generator/django-admin-tabler), UI Version `v1.0.0-beta19`
- ✅ `Sections` covered by the design:
  - ✅ **Admin section** (reserved for superusers)
  - ✅ **Authentication**: `Django.contrib.AUTH`, Registration
  - ✅ **All Pages** available in for ordinary users 
- ✅ `Docker`
- 🚀 `Deployment` 
  - `CI/CD` flow via `Render`

<br />

![Django Tabler - Open-Source Starter crafted by AppSeed.](https://github.com/app-generator/dummy/assets/51070104/8e56d253-5196-4a8d-961c-bd6c2a01a6a7)

<br />

## Start with `Docker`

> 👉 **Step 1** - Download the code from the GH repository (using `GIT`) 

```bash
$ git clone https://github.com/app-generator/django-tabler.git
$ cd django-tabler
```

<br />

> 👉 **Step 2** - Start the APP in `Docker`

```bash
$ docker-compose up --build 
```

Visit `http://localhost:5085` in your browser. The app should be up & running.

<br />

## Environment

Create a new `.env` file using sample `env.sample`. The meaning of each variable can be found below: 

- `DEBUG`: if `True` the app runs in develoment mode
  - For production value `False` should be used
- For `MySql` persistence
  - Install the DB Driver: `pip install mysqlclient` 
  - Create DB and assign a new user (full rights) 
  - Edit `.env` to match the DB, user, password ..  

<br />

## Manual Build

> Download the code 

```bash
$ git clone https://github.com/app-generator/django-tabler.git
$ cd django-tabler
```

<br />

### 👉 Set Up for `Unix`, `MacOS` 

> Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```

<br />

> Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> Start the APP

```bash
$ python manage.py createsuperuser # create the admin
$ python manage.py runserver       # start the project
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

### 👉 Set Up for `Windows` 

> Install modules via `VENV` (windows) 

```
$ virtualenv env
$ .\env\Scripts\activate
$ pip3 install -r requirements.txt
```

<br />

> Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> Start the APP

```bash
$ python manage.py createsuperuser # create the admin
$ python manage.py runserver       # start the project
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

## Codebase Structure

The project is coded using a simple and intuitive structure presented below:

```bash
< PROJECT ROOT >
   |
   |-- core/                            
   |    |-- settings.py                   # Project Configuration  
   |    |-- urls.py                       # Project Routing
   |
   |-- home/
   |    |-- views.py                      # APP Views 
   |    |-- urls.py                       # APP Routing
   |    |-- models.py                     # APP Models 
   |    |-- tests.py                      # Tests  
   |
   |-- requirements.txt                   # Project Dependencies
   |
   |-- env.sample                         # ENV Configuration (default values)
   |-- manage.py                          # Start the app - Django default start script
   |
   |-- ************************************************************************
```

<br />

## Deploy on [Render](https://render.com/)

- Create a Blueprint instance
  - Go to https://dashboard.render.com/blueprints this link.
- Click `New Blueprint Instance` button.
- Connect your `repo` which you want to deploy.
- Fill the `Service Group Name` and click on `Update Existing Resources` button.
- After that your deployment will start automatically.

At this point, the product should be LIVE.

<br />

## [PRO Version](https://appseed.us/product/volt-dashboard-pro/django/)   

This design is a pixel-perfect [Bootstrap 5](https://www.admin-dashboards.com/bootstrap-5-templates/) Dashboard with a fresh, new design. `Volt Dashboard PRO` is built with over 300 frontend individual elements, like buttons, inputs, navbars, nav tabs, cards, or alerts, giving you the freedom of choosing and combining.

> Features: 

- `Up-to-date Dependencies`
- `Design`: [Django Theme Volt](https://github.com/app-generator/django-volt-dashboard-pro) - `PRO Version`
- `Sections` covered by the design:
  - **Admin section** (reserved for superusers)
  - **Authentication**: `Django.contrib.AUTH`, Registration
  - **All Pages** available in for ordinary users 
- `Docker`, `Deployment`:
  - `CI/CD` flow via `Render`

![Volt Dashboard PRO - Starter generated by AppSeed.](https://user-images.githubusercontent.com/51070104/172672843-8c40a801-3438-4e9c-86db-38a34191fbdf.png)

<br />

---
[Django Dashboard Tabler](https://appseed.us/product/tabler/django/) - Open-source starter generated by **[AppSeed Generator](https://appseed.us/generator/)**.
