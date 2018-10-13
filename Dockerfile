FROM nginx:latest

RUN apt-get update \
    && apt-get install --assume-yes --fix-missing \
        sudo \
        supervisor \
        vim \
        less \
        pyenv \
        mysql

RUN cp /usr/src/app/deployment
RUN pyenv install 3.6.6 \
    pipenv install

RUN mkdir -p /var/tmp/supervisor \
    && cp /usr/src/app/deployment/supervisord.conf /etc/supervisor/supervisord.conf \
    && cp /usr/src/app/deployment/gunicorn.conf /etc/supervisor/conf.d/gunicorn.conf \
    && cp /usr/src/app/deployment/nginx-conf.conf /etc/nginx/nginx.conf

RUN chmod +x /usr/src/app/entrypoint.sh

CMD ["bash", "/usr/src/app/entrypoint.sh"]
