# VERSION:0.1
FROM fedora:26
MAINTAINER yujinyu
# ENV HOSTNAME filebench
COPY filebench-workloads /root/filebench-workloads
COPY dbench-workloads /root/dbench-workloads
COPY microbenchmark /root/microbenchmark
RUN dnf makecache && dnf install -y filebench dbench exim gcc  && dnf clean all
RUN cd  /root/microbenchmark && make


