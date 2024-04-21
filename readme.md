# Utilitário de rede :computer:
### Um utilitário de rede básico, escrito em python, para auxiliar em problemas de conectividade no adaptador de rede do computador

### Através deste utilitário, são executados alguns comandos para:
### - liberar a configuração DHCP atual e descartar a configuração de endereço IP para todos os adaptadores de rede (ipconfig/release)
### - Renovar a configuração do DHCP para todos os adaptadores de rede (ipconfig/renew)
### - Liberar e redefinir o conteúdo do cache do resolvedor de cliente DNS. (ipconfig/flushdns)
### - Realizar o registro dinâmico manual para os nomes DNS e endereços IP configurados em um computador (ipconfig/registerdns).
### -  Limpa e recarrega o cache de nomes NetBIOS no computador local (nbtstat -rr)
### - Redefinição das configurações do TCP/IP do adaptador de rede (netsh int ip reset all) 
### - Redefinição do winsock (netsh winsock reset)

## Obs: Pode ser que seja necessário reiniciar o computador para que as redefinições do adaptador de rede e o winsock sejam concluídas.
