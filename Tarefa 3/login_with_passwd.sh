#!/bin/bash
# Modo de uso:
# chmod +x login_with_passwd.sh
# login_with_passwd.sh <usuário> <senha>
user="$1"
passwd="$2"

sshpass -p "$2" ssh "$1"@192.168.100.103 -p 22 

#fazer uma verificação se o usuário digitou todos os comandos.