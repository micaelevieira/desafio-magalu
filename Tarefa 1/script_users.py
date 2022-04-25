#!/usr/bin/env python3
#
# Modo de uso:
# chmod +x script_users.py
# ./script_users.py
#
import sys 
import os
import pwd

print("Escolha uma opção para prosseguir: ")
print("1 - Criar usuários")
print("2 - Atualizar usuários")
print("3 - Excluir usuários")
op = input()

#Ler arquivo
def read_file(users_file):
	print("Lendo arquivo")
	with open(users_file) as f:
		users = f.readlines()
	print(f"Arquivo carregado com sucesso, {len(users)} usuários foram carregados")
	print("Deseja criar usuários? 1- Sim 2- Não")
	op2 = input()
	if op2 =="1":
		create_users(users)
		print(f"{len(users)} usuários criados com sucesso")

	else:
		print("Obrigada")

#Criar usuários
def create_users(users):
	for user in users:
		os.system(f"useradd {user}")

#Deletar usuários
def delete_users(users_file):
	with open(users_file) as f:
		users = f.readlines()
		for user in users:
			os.system(f"userdel {user}")
	print(f"{len(users)} usuários deletados com sucesso")

#Localizar usuários
def locate_user(user):
	username = user
	usernames = [x[0] for x in pwd.getpwall()]
	if username in usernames:
		print("Usuário encontrado")


if op == "1":
	print("Informe o nome do arquivo")
	file = input()
	read_file(file)

elif op == "2":
	print("1 - Adicionar a grupo")
	print("2 - Alterar login e senha")
	op3 = input()
	if op3 == "1":
		print("Deseja carregar arquivo com usuários? s- Sim n- Não")
		op4 = input()
		if op4 == "s":
			print("Informe o arquivo")
			users_update = input()
			print("Informe o grupo")
			group = input()
			with open(users_update) as f:
				users = f.readlines()
			for user in users:
				os.system(f"usermod -a -G {group} {user}")
		else:
			print("Informe qual usuário deseja inserir ao grupo")
			user_update_group = input()
			print("Informe o grupo")
			group = input()
			os.system(f"usermod -a -G {group} {user_update_group}")

	else:
		print("Informe qual usuário deseja atualizar")
		user_update = input()
		print ("Informe novo login")
		new_name = input()
		os.system(f"usermod -l {new_name} {user_update}")
		os.system(f"passwd {new_name}")


elif op == "3":
	print("Deseja informar arquivo ou nome de usuário 1-arquivo 2- usuário")
	op5 = input()
	if op5 == "1":
		print("Informe o arquivo")
		file = input()
		delete_users(file)
	else:
		print("Digite o nome do usuário que deseja escluir")
		user_del = input()
		locate_user(user_del)
		print("Deseja excluir? S-Sim N-Não")
		op6 = input()
		if op6 == "S":
			os.system(f"userdel {user_del}")
			print("usuário deletado com sucesso")
			



    
