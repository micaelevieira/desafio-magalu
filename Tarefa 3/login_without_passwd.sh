#!/bin/bash
#ssh maga@192.168.100.103 -p 22
# Modo de uso:
# chmod +x login_without_passwd.sh
# login_without_passwd.sh <usuário>

user="$1"

ssh "$1"@192.168.100.103 -p 22 

