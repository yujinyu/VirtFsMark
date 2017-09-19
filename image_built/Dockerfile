# VERSION:0.1
FROM yujinyu/fedora:mariadb

MAINTAINER yujinyu

COPY mark_loads /root/mark_loads
RUN chmod +x /root/mark_loads/run.sh
RUN dnf install make gcc sysbench -y && dnf clean all
RUN cd /root/mark_loads/microbenchmark && make && make clean
# Expose the default port for mariadb(mysql) database
EXPOSE 3306
