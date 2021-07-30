# Nutdevs.org opensource License Updater

[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/NutDevs-org/NutDevs.org-Licence/badges/quality-score.png?b=main)](https://scrutinizer-ci.com/g/NutDevs-org/NutDevs.org-Licence/?branch=main)
![GitHub repo size](https://img.shields.io/github/repo-size/NutDevs-org/NutDevs.org-Licence)
![GitHub file size in bytes](https://img.shields.io/github/size/NutDevs-org/NutDevs.org-Licence)
![Lines of code](https://img.shields.io/tokei/lines/github/NutDevs-org/NutDevs.org-Licence)
[![.github/workflows/main.yml](https://github.com/NutDevs-org/NutDevs.org-Licence/actions/workflows/main.yml/badge.svg)](https://github.com/NutDevs-org/NutDevs.org-Licence/actions/workflows/main.yml)

A small python script to automatically update License files

## Install for manual utilisation

1. Download the files from the repository
```bash
git clone https://github.com/NutDevs-org/NutDevs.org-Licence
```

2. Install the required python packages
```bash
python -m pip install requirements.txt
```


3. Create a file named `.env` in project root as the `.env.example` template.


4. Run the script
```bash
python -m main.py
```

## Install as github Action

1. Copy the `github_action.yml.example` into `.github/workflows.main.yml`


2. Go to your repository setting and add a value `TOKEN` with your account token in the `secrets` section.

*The workflows should update every day but you can run it manually*


## Get a github token

Go in your account setting, developers settings, personal access token and create a new token

***DO NOT SHARE IT WITH ANYONE !***