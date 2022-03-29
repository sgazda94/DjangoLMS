# dj_schulx

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

Dj_schulx is a Learning Managment System (LMS) project for educational purposes.

📎 Main features:

- organisation of courses
- making lessons plans in Markdown
- organization student groups, presence checking
- lesson planning (date, time) for specific groups


🛠️ Stack:

- [Django](https://www.djangoproject.com/) (Backend)
- [Bulma](https://bulma.io/) (CSS Framework)
- [HTMX](https://htmx.org/) (simple AJAX requests)

📄 Tasks to do:

- [ ] Add HTMX requests
- [ ] Add persmision based on role
- [ ] Write tests
- [ ] Many more 👋

---

🍪 Text below automatically created by Cookiecutter Django

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create an **superuser account**, use this command:

      $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy dj_schulx

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html).

## Deployment

The following details how to deploy this application.
