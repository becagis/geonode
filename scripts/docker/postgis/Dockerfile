FROM postgis/postgis:13-3.1
LABEL BecaGIS Team

RUN apt update -y && apt install vim telnet -y

# COPY ./start-container.sh /docker-entrypoint-initdb.d/0_start_container.sh
COPY ./initdb-geonode.sh /docker-entrypoint-initdb.d/geonode.sh
# COPY ./pgbouncer.ini /etc/pgbouncer/pgbouncer.ini

# RUN chmod +x /docker-entrypoint-initdb.d/0_start_container.sh
RUN chmod +x /docker-entrypoint-initdb.d/geonode.sh
# RUN chmod +x /etc/pgbouncer/pgbouncer.ini

# RUN sed -i "s/listen_port = 6431/listen_port = 6432/" /etc/pgbouncer/pgbouncer.ini

# FROM kartoza/postgis:13-3.1


# RUN apt update -y && apt install telnet supervisor pgbouncer -y

# COPY ./initdb-geonode.sh /docker-entrypoint-initdb.d/geonode.sh
# # COPY ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf
# # COPY ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf
# COPY start-container /usr/local/bin/start-container

# RUN chmod +x /docker-entrypoint-initdb.d/geonode.sh
# RUN chmod +x /usr/local/bin/start-container

# # CMD /etc/init.d/pgbouncer start

# # CMD ["start-container"]

# # ENTRYPOINT [ "/opt/bitnami/scripts/pgbouncer/entrypoint.sh" ]
# # CMD [ "/etc/init.d/pgbouncer", "start" ]