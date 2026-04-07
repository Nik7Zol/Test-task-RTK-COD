FROM debian:bookworm-slim

RUN apt-get update && \
    apt-get install -y ansible openssh-client curl
WORKDIR /ansible
COPY ansible/ /ansible/

# Копируем приватный ключ
COPY ansible/ssh/id_rsa /root/.ssh/id_rsa
RUN chmod 600 /root/.ssh/id_rsa

ENV ANSIBLE_HOST_KEY_CHECKING=False

CMD ["/bin/bash"]
