FROM nginx:1.23.0-alpine

RUN apk add --no-cache openssl inotify-tools

WORKDIR /etc/nginx/

# @becagis
ENV HTTP_HOST localhost
ENV HTTP_PORT 80
ENV HTTPS_PORT 443
ENV JENKINS_HTTP_PORT 9080
ENV GEOSERVER_UPSTREAM_HOST geoserver
ENV CELERY_MONITOR_UPSTREAM_HOST celerymonitor
ENV JENKINS_UPSTREAM_HOST jenkins
ENV DJANGO_UPSTREAM_HOST django
ENV RESOLVER 127.0.0.11
ENV LETSENCRYPT_MODE disabled

ADD nginx.conf.envsubst nginx.https.available.conf.envsubst ./
ADD geonode.conf.envsubst ./sites-enabled/

ADD docker-autoreload.sh docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
RUN chmod +x /docker-autoreload.sh
RUN chmod +x /docker-entrypoint.sh

CMD ["nginx", "-g", "daemon off;"]
