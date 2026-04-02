# Тестовое задание от РТК-ЦОД

Данное задание было выполнено на виртуальной машине в VirtualBox на ОС Ubuntu 24.04. После установки ОС, установил ansible и docker. 

```sh
apt update && apt install ansible docker
```

И приступил к созданию docker-compose, после Dockerfile для каждого контейнера, кроме контейнеров для мониторинга. Далее создал playbooks и hosts.ini для настройки каждого контейнера. Также создал ssh ключи для подключения к контейнерам.

```sh
ssh-keygen
```

После написал оставшиеся файлы конфигурации для nginx, grafana и victoriametrics.

В конце же отправил всё выполненное задание на github.


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

```sh
 docker exec lb1 ip addr show | grep 192.168.100.100
 docker exec lb2 ip addr show | grep 192.168.100.100
```
![Launching containers](https://github.com/Nik7Zol/Test-task-RTK-COD/blob/main/images/Worker_balancer_container.png)

```sh
 docker stop lb1 # Если в прошлой команде Vip показался у 'lb1', иначе 'lb1' нужно заменить на 'lb2'
```
![Launching containers](https://github.com/Nik7Zol/Test-task-RTK-COD/blob/main/images/Stop_worker_balancer_container.png)

Проверка доступности через утилиту 'curl'.

![Launching containers](https://github.com/Nik7Zol/Test-task-RTK-COD/blob/main/images/Curl_test_after_stop_balancer_container.png)

## Проверка Grafana и VictoriaMetrics

Для начала зайду на VictoriaMetrics и проверю, что все со всех нужных контейнеров собираются метрики. Для этого нужно перейти по ссылке.

http://localhost:8428/targets

![Launching containers](https://github.com/Nik7Zol/Test-task-RTK-COD/blob/main/images/VictoriaMetrics_after_stop_container.png)

Увидел, что не работает один контейнер, нужно включить его обратно. И запустить playbook для настройки.

```sh
 docker start lb1
```
```sh
 docker exec -it ansible bash
 ansible-playbook -i hosts.yml playbooks/playbook_lb.yml
 ansible-playbook -i hosts.yml playbooks/playbook_cluster.yml
 ansible-playbook -i hosts.yml playbooks/playbook_extra.yml
```
![Launching containers](https://github.com/Nik7Zol/Test-task-RTK-COD/blob/main/images/VictoriaMetrics_active_all_containers.png)

Далее заходим на Grafana по ссылке: http://localhost:3000
 login: admin
 password: admin

Далее нужно зайти во вкладку Dashboard. В данной части у меня не получилось выполнить полностью задачу. Не получилось найти и подключить нужные метрики.

![Launching containers](https://github.com/Nik7Zol/Test-task-RTK-COD/blob/main/images/Grafana_main_dashboard.png)

