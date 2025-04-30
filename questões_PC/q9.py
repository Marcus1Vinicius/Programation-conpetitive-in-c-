# Na biblioteca digital, alguns materiais como artigos acadêmicos e revistas especializadas são restritos a usuários com assinaturas premium. Escreva um programa que receba o tipo de assinatura de um usuário ("básica" ou "premium") e o tipo de material que ele deseja acessar ("ebook", "artigo", ou "revista"). O programa deve verificar e exibir uma mensagem informando se o usuário tem permissão para acessar o material desejado. Usuários com assinatura "premium" podem acessar todos os tipos de materiais, enquanto usuários com assinatura "básica" só podem acessar "ebooks".

# Digite o tipo de assinatura (básica ou premium): premium
# Digite o tipo de material que deseja acessar (ebook, artigo ou revista): ebook
# Acesso permitido.

tipo_assinatura = input("Digite o tipo de assinatura (básica ou premium): ")
tipo_material = input("Digite o tipo de material que deseja acessar (ebook, artigo ou revista): ")

if(tipo_assinatura == "básica" and tipo_material == "ebook"):
    print("Acesso permitido.")

elif(tipo_assinatura == "premium"):
    print("Acesso permitido.")

else:
    print("Acesso negado!")