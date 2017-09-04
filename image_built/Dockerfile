# VERSION:0.1
FROM fedora:26
MAINTAINER yujinyu
# ENV HOSTNAME filebench
COPY mark_loads /root/mark_loads
RUN dnf install -y filebench dbench make gcc  && dnf clean all
RUN cd /root/mark_loads/microbenchmark && make && make clean


