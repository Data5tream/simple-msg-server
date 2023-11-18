# Simple MSG Server

Collect and display messages. Either via `formdata` or `json`.

## Environment variables

Following environment variables need to be set

- `DB_HOST`
- `DB_NAME`
- `DB_USER`
- `DB_PASS`

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
pip install -r requirements.txt
python manage.py migrate
```

Run django

```shell
python manage.py runserver
```