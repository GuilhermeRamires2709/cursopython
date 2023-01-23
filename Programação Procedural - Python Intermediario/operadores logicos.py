#Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira valida
# toda a expressão como verdadeira
# Se qualquer valor for considerado verdadeiro
# a expressão inteira será avaliada naquele valor
# São considerados falsos (que você já viu)
# 0 0.0 '' False
# Também existe o tipo None que é usado para representar um não valor
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('senha: ')
senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# Avaliação de curto circuito

senha = input('senha: ') or "Sem senha"
print(senha)