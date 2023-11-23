# Simple MSG Server

Collect and display messages. Either via `formdata` or `json`.

## Environment / configuration variables

| Env name  | default value |
|-----------|---------------|
| `DB_HOST` | `localhost`   |
| `DB_NAME` | `postgres`    |
| `DB_USER` | `postgres`    |
| `DB_PASS` |               |
| `DB_PORT` | `6543`        |

## Running

Build the container

```shell
podman build -t simple_msg_server .
```

Run the container (you need a running `postgres` database)

```shell
podman run -p 8000:8000 \
  -e DB_HOST=host.containers.internal \
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