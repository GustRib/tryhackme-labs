# Room: Pickle Rick

**Plataforma:** TryHackMe  
**Room:** https://tryhackme.com/room/picklerick  
**Dificuldade:** Easy  
**Categoria:** Linux / Web  

## Objetivo
Laboratório introdutório focado em enumeração web e exploração básica
em ambiente Linux, com o objetivo de obter acesso inicial ao sistema e explorar falhas simples de configuração.

## Enumeração
Durante a fase de enumeração, foram realizadas:
- Varredura de portas para identificação de serviços expostos
- Enumeração de diretórios e arquivos web
- Análise manual das funcionalidades disponíveis na aplicação

Durante essa fase, foi possível identificar pontos de entrada
que indicaram possível execução de comandos.

## Exploração
Com base nos resultados da enumeração:
- Foi identificada uma funcionalidade web vulnerável
- A vulnerabilidade permitiu execução de comandos no sistema alvo
- O acesso inicial foi obtido de forma controlada, sem uso de exploits públicos

A abordagem foi escolhida com base nos resultados da enumeração,
evitando uso de exploits prontos.

## Pós-Exploração
Após o acesso inicial:
- Foi realizada enumeração local do sistema
- Análise de permissões e comandos disponíveis
- Exploração de falhas simples de configuração para avançar privilégios

Essa fase reforçou conceitos básicos de privilege escalation em Linux.

## Aprendizados
- Importância da enumeração antes de qualquer tentativa de exploração
- Como pequenas falhas web podem levar a execução de comandos
- Conceitos iniciais de pós-exploração e privilege escalation
- Valor de uma abordagem metodológica em pentest

## Observações Éticas
Este write-up não contém flags, credenciais, exploits completos
ou qualquer informação sensível.

Todo o conteúdo refere-se exclusivamente a ambientes controlados
da plataforma TryHackMe, respeitando princípios éticos e de escopo.
