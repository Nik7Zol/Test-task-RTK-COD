ansible-playbook -i hosts.yml playbooks/playbook_lb.yml
ansible-playbook -i hosts.yml playbooks/playbook_cluster.yml
ansible-playbook -i hosts.yml playbooks/playbook_backend.yml
ansible-playbook -i hosts.yml playbooks/playbook_extra.yml
ansible-playbook -i hosts.yml playbooks/playbook_monitoring.yml
