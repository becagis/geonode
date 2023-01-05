ARG GEOSERVER_VERSION=2.19.6
FROM geonode/geoserver:${GEOSERVER_VERSION}
MAINTAINER GeoNode Development Team

RUN apt update && apt install -y vim

# COPY set_geoserver_auth.sh /usr/local/tomcat/tmp

# RUN apt-get update \
#     && apt-get -y upgrade \
#     && chmod +x /usr/local/tomcat/tmp/set_geoserver_auth.sh