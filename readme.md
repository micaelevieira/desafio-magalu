<h1>Desafio DevOps</h1> 

### Tópicos 

:small_blue_diamond: [Descrição do projeto](#descricao-do-projeto)

:small_blue_diamond: [Funcionalidades](#funcionalidades)

:small_blue_diamond: [Pré-requisitos](#pre-requisitos)

:small_blue_diamond: [Execução](#execucao)

<div id='descricao-do-projeto'/>

## Descrição do projeto 

<p align="justify">
  Projeto desenvolvido como exercício para o processo seletivo de DevOps
</p>


<div id='funcionalidades'/>


## Funcionalidades

:heavy_check_mark: **Script para manusear usuários**  

script_users.py permite receber uma lista com usuários e criar ou deletar usuários. Permite ainda atualizar informações sobre os usuários.

:heavy_check_mark: **Script para conexão com banco de dados**

script_grants.sh permite realizar conexão com o banco de dados PostgresSQL e alterar permissões no banco para usuários.

:heavy_check_mark: **Script para conexão SSH com senha**

login_with_passwd.sh permite realizar uma conexão ssh com senha a uma máquina virtual linux.


:heavy_check_mark: **Script para conexão SSH sem senha**

login_without_passwd.sh permite realizar uma conexão ssh sem senha a uma máquina virtual linux.

:heavy_check_mark: **Script para monitorar processos do Linux**

monitor_process.sh monitora os logs do sistema linux e os armazena em um arquivo.

<div id='pre-requisitos'/>

## Pré-requisitos

:memo: Tarefa 1: [Python](https://www.python.org/downloads/)

:memo: Tarefa 2: [PostgresSQL](https://www.postgresql.org/download/)

:memo: Tarefa 3: [VirtualBox](https://www.virtualbox.org/wiki/Downloads) [OpenSSH](https://www.openssh.com/) 



<div id='execucao'/>

## Execução dos Scripts

Dê permissão de execução para cada script:

```
$ chmod +x <nome do script>
```

:memo: **Tarefa 1**

Execute o script:
```
$ ./script_users.py
```
Após a execução, escolha qual opção deseja


:memo: **Tarefa 2**

Altere a configuração do banco de dados para ser possível conectar sem senha. Abra o arquivo de configuração do PostresSQL /etc/postgresql/POSTGRES_VERSION/main/pg_hba.conf e substitua por: 

```
local  all  all                trust
host   all  all  127.0.0.1/32  trust
host   all  all  ::1/128       trust
```

Execute o script:
```
$ ./script_grants.sh <usuário> <banco> <-grant/-revoke> <"String de permissão">
```
Exemplo:
```
$ ./script_grants.sh maga auto_production -grant "SELECT ON candidates TO"
```

:memo: **Tarefa 3**


A máquina virtual é um ubuntu-server-22.04 criada no virtualbox. A .iso pode ser encontrada [aqui](https://ubuntu.com/download/server)

Nas configurações do virtualbox é importante alterar a placa de rede da máquina virtual para "placa em modo bridge", assim a máquina host se torna uma ponte para a máquina virtual.

Para o login_with_passwd.sh execute:

```
$ ./login_with_passwd.sh <usuário> <senha>
```

Para o login_without_passwd.sh devem ser configuradas as chaves públicas e privadas entre a máquina host e a máquina virtual. Para referência de configuração clique [aqui](https://www.digitalocean.com/community/tutorials/how-to-configure-ssh-key-based-authentication-on-a-linux-server-pt). Importante lembrar que as chaves são geradas no host hospedeiro e passadas para a máquina virtual. 

Após a configuração de chaves, execute:
```
$ ./login_without_passwd.sh <usuário>
```

Para o monitor_process.sh, execute:
```
$ ./monitor_process.sh <arquivo destino>
```
