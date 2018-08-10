## Project setup

This project uses `pyenv` and `pyenv-virtualenv` to create an isolated Python environment.

Review [Getting started: Python dep mgmt with pyenv](https://github.com/CenturyLinkCloud/pl-cloud-infrastructure/wiki/Getting-started:-Python-dep-mgmt-with-pyenv). 

Once `pyenv` and `pyenv-virtualenv` are installed, create your environment

```bash
ᐅ pyenv install 3.6.5
python-build: use openssl from homebrew
python-build: use readline from homebrew
Installing Python-3.6.5...
# ...

ᐅ pyenv virtualenv 3.6.5 ms-ref-python-django-3.6.5
Requirement already satisfied: setuptools in /Users/starver/.pyenv/versions/3.6.5/envs/ms-ref-python-django-3.6.5/lib/python3.6/site-packages
Requirement already satisfied: pip in /Users/starver/.pyenv/versions/3.6.5/envs/ms-ref-python-django-3.6.5/lib/python3.6/site-packages
```

Now, install all dependencies:

```bash
pip install -r requirements-dv.txt
```
