# Network Security Toolkit (Basic)

Este projeto é um conjunto de ferramentas básicas em Python para estudo de
redes e fundamentos de segurança.

O objetivo é aprendizado prático de:
- DNS
- Reverse DNS
- Validação de endereços IP
- Scan de portas TCP
- Organização de código e GitHub

## Ferramentas

### DNS Resolver
Resolve um hostname para um endereço IP e realiza reverse DNS.

### IPv4 Validator
Valida se uma string representa um endereço IPv4 válido.

### Port Scanner
Realiza um scan TCP simples em portas comuns usando sockets.

## Estrutura do Projeto

- `dns_resolver.py` — resolução DNS e reverse DNS
- `ip_validator.py` — validação de endereços IPv4
- `port_scanner.py` — scan de portas TCP
- `main.py` — reservado para uso futuro
- `.gitignore`

## Como executar

Cada ferramenta pode ser executada individualmente:

```bash
python dns_resolver.py
python ip_validator.py
python port_scanner.py