#!/bin/bash
# Modo de uso:
# chmod +x monitor_process.sh
# monitor_process.sh <arquivo destino>


arquivo="$1"

while [[ true ]]; do
	ps -aux >> "$1"
	echo "Log extraído no arquivo setado"
	sleep 900
done
