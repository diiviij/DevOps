FROM ubuntu:20.04

RUN apt-get update && apt-get install -y fortune-mod cowsay

COPY wisecow.sh /app/wisecow.sh
WORKDIR /app

EXPOSE 4499
CMD ["./wisecow.sh"]
