# Reflexão sobre Medidas de Prevenção e Defesa

Este documento detalha as estratégias e ferramentas para se proteger contra as ameaças simuladas neste projeto: Ransomware e Keyloggers.

## 🛡️ Defesa Contra Ransomware

Ransomware é uma ameaça destrutiva. A defesa eficaz se baseia em uma estratégia de múltiplas camadas (defesa em profundidade).

### 1. Prevenção (A Primeira Linha de Defesa)

-   **Conscientização do Usuário:** A maioria dos ataques de ransomware começa com phishing. Treinar usuários para não clicar em links suspeitos, não abrir anexos inesperados e verificar a identidade do remetente é a defesa mais eficaz e barata.
-   **Filtros de E-mail e Web:** Soluções que bloqueiam e-mails de spam/phishing e sites maliciosos antes que cheguem ao usuário.
-   **Firewall e Sistemas de Prevenção de Intrusão (IPS):** Bloqueiam o acesso a servidores de Comando e Controle (C2) conhecidos e podem detectar padrões de tráfego anômalos associados à atividade de ransomware.
-   **Patch Management:** Manter sistemas operacionais e softwares (navegadores, Office, etc.) sempre atualizados para corrigir vulnerabilidades que o ransomware poderia explorar para se propagar.

### 2. Detecção e Mitigação (Durante o Ataque)

-   **Antivírus e EDR (Endpoint Detection and Response):** Soluções modernas não dependem apenas de assinaturas. Elas usam análise comportamental para detectar atividades suspeitas, como a criptografia rápida e em massa de arquivos. Um EDR pode isolar o host infectado da rede para impedir a propagação.
-   **Sandboxing:** Executar arquivos suspeitos em um ambiente isolado (sandbox) para analisar seu comportamento antes de permitir que sejam executados no sistema real.
-   **Monitoramento de Integridade de Arquivos:** Ferramentas que alertam quando arquivos críticos sofrem alterações inesperadas.

### 3. Recuperação (Após o Ataque)

-   **Backups, Backups e Mais Backups:** A única garantia de recuperação contra um ransomware. A **regra 3-2-1** é fundamental:
    -   **3** cópias dos seus dados.
    -   **2** tipos de mídia diferentes (ex: HD externo e nuvem).
    -   **1** cópia offline/imutável (desconectada da rede, para que o ransomware não possa criptografá-la também).
-   **Plano de Resposta a Incidentes:** Ter um plano claro de quem contatar, como isolar sistemas e como restaurar a partir de backups economiza tempo e dinheiro. **Pagar o resgate não é uma garantia de recuperação** e financia o crime.

---

## 🕵️ Defesa Contra Keyloggers

Keyloggers são furtivos e focados no roubo de informações. A defesa se concentra em impedir a instalação e detectar a exfiltração de dados.

### 1. Prevenção

-   **Cuidado com Downloads:** A principal via de infecção é através de software pirata, "cracks" ou programas de fontes não confiáveis. Baixe software apenas de sites oficiais.
-   **Antivírus/Anti-Malware:** Soluções de segurança de endpoint são eficazes na detecção de keyloggers conhecidos antes que sejam instalados.
-   **Firewall de Host:** Um firewall bem configurado pode bloquear a comunicação de saída do keylogger quando ele tenta enviar os logs para o atacante.

### 2. Detecção e Mitigação

-   **Análise de Processos e Rede:** Monitorar processos em execução (Gerenciador de Tarefas no Windows) e o tráfego de rede pode revelar atividades suspeitas. Um processo desconhecido consumindo recursos ou fazendo conexões de rede inesperadas é um sinal de alerta.
-   **Teclados Virtuais:** Para inserir informações extremamente sensíveis (como senhas de banco), usar o teclado virtual na tela pode frustrar keyloggers baseados em software, pois eles monitoram o teclado físico.
-   **Autenticação de Múltiplos Fatores (MFA):** A medida mais importante contra o roubo de credenciais. Mesmo que um atacante capture sua senha com um keylogger, ele não conseguirá acessar a conta sem o segundo fator (código do app, token físico, etc.).

### 3. Conscientização

-   **Gerenciadores de Senhas:** Usar um gerenciador de senhas com preenchimento automático pode mitigar o risco, pois você não está digitando a senha fisicamente.
-   **Revisão Periódica:** Verificar periodicamente os aplicativos instalados e as extensões do navegador para remover qualquer item suspeito ou não utilizado.
