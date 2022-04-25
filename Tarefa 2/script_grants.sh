#!/bin/bash
# Banco utilizado: Postgres 
# Importante: configurar o banco para conectar sem senha
# Modo de uso:
# chmod +x script_grants.sh
# ./script_grants.sh <usuário> <banco> <-grant/-revoke> <String>

GRANT SELECT ON candidates TO magalu

user="$1"
database="$2"
string="$4"
STR1="GRANT"
SRT2="REVOKE"
principal1="$STR1 $4 $user"
principal2="$SRT2 $4 $user"

case "$3" in
	-grant) echo "Conectando ao banco..."
	psql -U postgres -d "$database" -h localhost -c "$principal1"
	echo "Script executado com sucesso!!"
	;;
	-revoke) echo "Conectando ao banco..."
	psql -U postgres -d "$database" -c "$principal2"
	echo "Script executado com sucesso!!"
	;;
esac