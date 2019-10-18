#!/bin/python3
# encoding: utf-8
import smtplib
import time
import getpass
import sys
print("será necessario a permissão de aplicativos desconhecidos nas configurações do seu email.\nentre neste link para fazer o processo: myaccount.google.com/lesssecureapps ")
time.sleep(4)
try:
    print("""

   _____ ____  ___    __  _____  _____________       __  ______    ______ 
  / ___// __ \/   |  /  |/  /  |/  / ____/ __ \     /  |/  /   |  /  _/ / 
  \__ \/ /_/ / /| | / /|_/ / /|_/ / __/ / /_/ /    / /|_/ / /| |  / // /  
 ___/ / ____/ ___ |/ /  / / /  / / /___/ _, _/    / /  / / ___ |_/ // /___
/____/_/   /_/  |_/_/  /_/_/  /_/_____/_/ |_|    /_/  /_/_/  |_/___/_____/
                                                                                                                                                           
                                                                                      """)
    print("spammer Mail V.1.0\n© B4")
    time.sleep(3)
    print("será necessario a entrada de seu email e senha para autenticação")
    time.sleep(2)
    remetente= input('seu email: ')
    senha = getpass.getpass('sua senha: ')

    destinatario = input('email alvo: ')
    texto = input("digite sua mensagem: ")
    repeticoes=int(input("digite a quantidade de mensagens a serem enviadas: "))
    espera = int(input("quantos segundos de espera a cada mensagem: "))
    assunto = ''
###########
    msg = '\r\n'.join([
      'From: %s' % remetente,
      'To: %s' % destinatario,
      'Subject: %s' % assunto,
      '',
      '%s' % texto
      ])
    # Enviando o email
    server = smtplib.SMTP_SSL('smtp.gmail.com:465')
    server.login(remetente,senha)
    while repeticoes > 0:
        server.sendmail(remetente, destinatario, msg)
        print("\nenviado com sucesso - ",repeticoes)
        time.sleep(espera)
        repeticoes = repeticoes - 1
    print("\nfim do programa!!")
    time.sleep(5)
    server.quit()
except Exception as erro:
    print("ocorreu um erro:",erro)
    time.sleep(10)
except KeyboardInterrupt:
    print("\nfim do programa...")
    sys.exit()
