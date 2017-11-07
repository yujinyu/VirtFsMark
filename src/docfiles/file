FROM yujinyu/fedora:26
MAINTAINER yujinyu

COPY fio.sh /
RUN chmod +x /fio.sh
RUN dnf install fio libaio-devel -y && dnf clean all
RUN mkdir -p /test && touch /test/file

