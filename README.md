#Тестовое задание от РТК-ЦОД



#Запуск 7 контейнеров

docker exec -it ansible bash

![Launching containers](https://github.com/Nik7Zol/Test-task-RTK-COD/images/Launching containers.png)

ansible-playbook -i hosts.yml playbooks/playbook_lb.yml

ansible-playbook -i hosts.yml playbooks/playbook_cluster.yml

ansible-playbook -i hosts.yml playbooks/playbook_backend.yml

ansible-playbook -i hosts.yml playbooks/playbook_extra.yml

ansible-playbook -i hosts.yml playbooks/playbook_monitoring.yml
