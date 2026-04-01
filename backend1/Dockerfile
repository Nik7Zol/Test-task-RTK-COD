FROM debian:bookworm-slim

RUN apt-get update && \
    apt-get install -y openssh-server sudo python3 python3-pip 

RUN useradd -m -s /bin/bash ansible && \
    echo "ansible ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

RUN mkdir /var/run/sshd && \
    mkdir -p /home/ansible/.ssh && \
    chmod 700 /home/ansible/.ssh

# Копируем публичный ключ (владельцем будет root)
COPY ansible/ssh/id_rsa.pub /home/ansible/.ssh/authorized_keys

# Меняем владельца на ansible и выставляем правильные права
RUN chown -R ansible:ansible /home/ansible/.ssh && \
    chmod 600 /home/ansible/.ssh/authorized_keys


CMD ["/usr/sbin/sshd", "-D"]
