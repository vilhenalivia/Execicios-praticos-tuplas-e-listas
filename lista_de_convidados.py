lista_atual = ['Ana', 'Pedro', 'Carlos']
nome = input('Digite o nome do novo convidado: ')
posicao = int(input('Digite a posição na qual deseja inserir o convidado: '))
lista_atual.insert(posicao -1, nome)
print(f"Lista atualizada de convidados: {lista_atual}")

