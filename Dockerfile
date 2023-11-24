FROM node:21 as nodebuilder

WORKDIR /app
RUN corepack enable
COPY ["typescript/package.json", "typescript/pnpm-lock.yaml", "./"]
RUN pnpm i

COPY typescript/tsconfig.json ./
COPY typescript/ts_src ts_src
RUN pnpm run compile --outDir compiled
RUN ls -l

FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apk add nginx && \
    pip install --upgrade pip

COPY nginx.conf /etc/nginx/
COPY entrypoint.sh /app

COPY app/requirements.txt /app
RUN pip install -r requirements.txt

COPY app /app
COPY --from=nodebuilder /app/compiled/* /app/simple_msg_server/static/simple_msg_server/js

RUN python manage.py collectstatic

EXPOSE 8000
ENTRYPOINT ["sh", "/app/entrypoint.sh"]
