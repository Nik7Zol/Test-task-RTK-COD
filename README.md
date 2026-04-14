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
Для них создаются докер тома grafana-data и victoria-data, которых хранятся данные.

В конце же отправил всё выполненное задание на github.


## Установка тестового задания

Для работы с тестовым заданием на свою ОС нужно скачать git, ansible, docker.
Для Unix-систем поможет команда:
```sh
apt update && apt install ansible docker git
```

Далее нужно скопировать репозиторий данного проекта:
```sh
git clone https://github.com/Nik7Zol/Test-task-RTK-COD.git
```

После нужно перейти в клонированный католог:
```sh
cd Test-task-RTK-COD/
```

## Запуск 7 контейнеров

Создаём и запускаем контейнеры, после проверяем, что их статус "up"

```sh
 docker-compose up -d --build
 docker-compose ps
```
![Launching containers](https://github.com/Nik7Zol/Test-task-RTK-COD/blob/main/images/Launching_containers.png)

## Запуск ansible-playbooks

Сначала заходим в контейнер "ansible". Через который производим донастройку всех остальных контейнеров с помощью плейбуков.

```sh
 docker exec -it ansible bash

 ansible-playbook -i hosts.yml playbooks/playbook_lb.yml
 ansible-playbook -i hosts.yml playbooks/playbook_cluster.yml
 ansible-playbook -i hosts.yml playbooks/playbook_backend.yml
 ansible-playbook -i hosts.yml playbooks/playbook_extra.yml
 ansible-playbook -i hosts.yml playbooks/playbook_monitoring.yml
```
![Start_ansible-playbooks](https://github.com/Nik7Zol/Test-task-RTK-COD/blob/main/images/Start_ansible-playbooks.png)

Устанавливаем на контейнер ansible утилиту 'curl'.
После проверяем работоспособность бекэндов.

```sh
 apt update && apt install curl
 curl http://192.168.100.100:80
```

![Curl_test](https://github.com/Nik7Zol/Test-task-RTK-COD/blob/main/images/Curl_test.png)

Выходим из контейнера ansible и проверяем через какой контейнер балансировщик (lb1 или lb2) проходит трафик.

```sh
exit
```
```sh
 docker exec lb1 ip addr show | grep 192.168.100.100
 docker exec lb2 ip addr show | grep 192.168.100.100
```
![Worker_balancer_container](https://github.com/Nik7Zol/Test-task-RTK-COD/blob/main/images/Worker_balancer_container.png)

Выключаем балансировщик, через который проходит трафик. В моём случае это lb1.

```sh
 docker stop lb1 # Если в прошлой команде Vip показался у 'lb1', иначе 'lb1' нужно заменить на 'lb2'
```
![Stop_worker_balancer_container](https://github.com/Nik7Zol/Test-task-RTK-COD/blob/main/images/Stop_worker_balancer_container.png)

Повторная проверка доступности через утилиту 'curl'.

![Curl_test_after_stop_balancer_container](https://github.com/Nik7Zol/Test-task-RTK-COD/blob/main/images/Curl_test_after_stop_balancer_container.png)

## Проверка Grafana и VictoriaMetrics

Для начала зайду на VictoriaMetrics и проверю, что все со всех нужных контейнеров собираются метрики. Для этого нужно перейти по ссылке.

http://localhost:8428/targets

![VictoriaMetrics_after_stop_container](https://github.com/Nik7Zol/Test-task-RTK-COD/blob/main/images/VictoriaMetrics_after_stop_container.png)

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
![VictoriaMetrics_active_all_containers](https://github.com/Nik7Zol/Test-task-RTK-COD/blob/main/images/VictoriaMetrics_active_all_containers.png)

Далее заходим на Grafana по ссылке: http://localhost:3000
 login: admin
 password: admin

Далее нужно зайти во вкладку Dashboard. В данной части у меня не получилось выполнить полностью задачу. Не получилось найти и подключить нужные метрики.

![Grafana_main_dashboard](https://github.com/Nik7Zol/Test-task-RTK-COD/blob/main/images/Grafana_main_dashboard.png)

