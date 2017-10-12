# VERSION:0.1
FROM yujinyu/fedora:mariadb

MAINTAINER yujinyu

COPY mark_loads /root/mark_loads
RUN chmod +x /root/mark_loads/*.sh && dnf install make gcc sysbench -y && dnf clean all
