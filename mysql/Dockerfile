FROM mysql:5.7

COPY create_database.sql /etc/mysql/create_database.sql
ENV MYSQL_DATABASE="audino"
ENV MYSQL_ROOT_PASSWORD="root"
ENV MYSQL_USER="audino"
ENV MYSQL_PASSWORD="audino"

CMD [ "--init-file=/etc/mysql/create_database.sql", "--character-set-server=utf8mb4", "--collation-server=utf8mb4_bin" ]
