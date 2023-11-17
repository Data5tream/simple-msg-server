# Simple MSG Server

Collect and display messages

## Running

*Docker image and instructions coming soon*

## Developing

Install typescript dependencies

```shell
nvm use
pnpm i
```

Run typescript watcher

```shell
pnpm watch
```

Prepare django

```shell
pip install -r requirements
python manage.py migrate
```

Run django

```shell
python manage.py runserver
```