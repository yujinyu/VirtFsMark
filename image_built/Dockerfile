# VERSION:0.1
FROM fedora:26
MAINTAINER yujinyu
COPY mark_loads /root/mark_loads
RUN chmod +x /root/mark_loads/run.sh
RUN dnf install -y filebench dbench make gcc  && dnf clean all
RUN cd /root/mark_loads/microbenchmark && make && make clean


