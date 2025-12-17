FROM ubuntu:latest
LABEL authors="people"

ENTRYPOINT ["top", "-b"]