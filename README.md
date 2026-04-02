# Тестовое задание от РТК-ЦОД



## Запуск 7 контейнеров
```sh
 docker-compose up -d
 docker-compose ps
```
![Launching containers](https://github.com/Nik7Zol/Test-task-RTK-COD/blob/main/images/Launching_containers.png)

## Запуск ansible-playbooks
```sh
 docker exec -it ansible bash

 ansible-playbook -i hosts.yml playbooks/playbook_lb.yml
 ansible-playbook -i hosts.yml playbooks/playbook_cluster.yml
 ansible-playbook -i hosts.yml playbooks/playbook_backend.yml
 ansible-playbook -i hosts.yml playbooks/playbook_extra.yml
 ansible-playbook -i hosts.yml playbooks/playbook_monitoring.yml
```
![Launching containers](https://github.com/Nik7Zol/Test-task-RTK-COD/blob/main/images/Start_ansible-playbooks.png)
```sh
 apt update && apt install curl
 curl http://192.168.100.100:80
```
![Launching containers](https://github.com/Nik7Zol/Test-task-RTK-COD/blob/main/images/Curl_test.png)
