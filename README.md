# Simple MSG Server

Collect and display messages. Either via `formdata` or `json`.

## Environment variables

Following environment variables need to be set

- `DB_HOST`
- `DB_NAME`
- `DB_USER`
- `DB_PASS`

## Running

Build the container

```shell
podman build -t simple_msg_server .
```

Run the container (you need a running `postgres` database)

```shell
podman run -p 8000:8000 \
  -e DB_NAME=postgres \
  -e DB_HOST=host.containers.internal \
  -e DB_USER=postgres \
  -e DB_PASS=password \
  simple_msg_server
```

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