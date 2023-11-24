# Simple MSG Server

Collect and display messages. Either via `formdata` or `json`.

## Environment / configuration variables

| Env name               | default value           |
|------------------------|-------------------------|
| `DB_HOST`              | `localhost`             |
| `DB_NAME`              | `postgres`              |
| `DB_USER`              | `postgres`              |
| `DB_PASS`              |                         |
| `DB_PORT`              | `5432`                  |
| `SECRET_KEY`           |                         |
| `DJANGO_DEBUG`         | `False`                 |
| `DJANGO_ALLOWED_HOSTS` | `127.0.0.1,localhost`   |
| `CSRF_TRUSTED_ORIGINS` | `http://127.0.0.1:8000` |


## Running

### Prebuild image

Pull the image from GitHub

```shell
podman pull ghcr.io/data5tream/simple-msg-server:latest
```

### Local build

Build the container

```shell
podman build -t simple-msg-server .
```

Run the container (you need a running `postgres` database)

```shell
podman run -p 8000:8000 \
  -e DB_HOST=host.containers.internal \
  -e DB_PASS=password \
  simple-msg-server
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