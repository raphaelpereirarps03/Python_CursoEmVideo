import datetime

print("""A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
=> Até 9 anos: MIRIM;
=> Até 14 anos: INFANTIL;
=> Até 19 anos: JUNIOR;
=> Até 20 anos: SÊNIOR;
=> Acima: MASTER. 
""")

anoNasc = int(input("Entre com o ano de nascimento do atleta: "))
idade = (datetime.date.today().year - anoNasc)

if idade <= 9:
    print("Sua categoria é: \033[34mMIRIM\033[m")
elif idade <= 14:
    print("Sua categoria é: \033[31mINFANTIL\033[m")
elif idade <= 19:
    print("Sua categoria é: \033[32mJUNIOR\033[m")
elif idade <= 20:
    print("Sua categoria é: \033[33mSÊNIOR\033[m")
else:
    print("Sua categoria é: \033[7mMASTER\033[m")
