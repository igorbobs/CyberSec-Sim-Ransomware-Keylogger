# Projeto de Simulação em Cibersegurança: Ransomware e Keylogger

## ⚠️ Aviso Legal e Ético

Este projeto foi desenvolvido para **fins estritamente educacionais**. O objetivo é demonstrar, em um ambiente controlado, o funcionamento de ameaças digitais como ransomware e keyloggers para que possamos entender melhor como nos proteger delas.

**NÃO utilize este código em sistemas ou contra pessoas sem permissão explícita.** O uso indevido de ferramentas de cibersegurança é ilegal e antiético. O autor não se responsabiliza pelo mau uso deste projeto.

---

## 🎯 Sobre o Projeto

Este repositório contém a implementação de duas simulações de malware em Python:

1.  **Ransomware Simulado:** Um conjunto de scripts que criptografa arquivos em um diretório específico e exige uma "chave" para descriptografá-los.
2.  **Keylogger Simulado:** Um script que captura as teclas digitadas e as salva em um arquivo de log, com a funcionalidade de enviar esse log por e-mail.

O foco principal é o aprendizado sobre os vetores de ataque e, mais importante, sobre as **estratégias de defesa e mitigação**.

## 📂 Estrutura do Projeto

O projeto está organizado da seguinte forma:

-   `/ransomware_simulado`: Contém os scripts para gerar chaves, criptografar e descriptografar arquivos.
-   `/keylogger_simulado`: Contém o script do keylogger e o módulo de envio de e-mail.
-   `/docs`: Contém a documentação detalhada sobre as medidas de defesa e prevenção.
-   `requirements.txt`: Lista as dependências Python necessárias.

## 🛠️ Como Usar

### Pré-requisitos

-   Python 3.x
-   Pip (gerenciador de pacotes Python)

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/seu-usuario/projeto-ciberseguranca.git
    cd projeto-ciberseguranca
    ```

2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

### Executando a Simulação de Ransomware

1.  **Navegue até a pasta do ransomware:**
    ```bash
    cd ransomware_simulado
    ```

2.  **Crie arquivos de teste:**
    A pasta `arquivos_teste/` já contém alguns exemplos. Sinta-se à vontade para adicionar outros.

3.  **Execute o script de criptografia:**
    ```bash
    python encrypt.py
    ```
    Isso irá criptografar todos os arquivos na pasta `arquivos_teste/` e criar um arquivo `LEIA_ME.txt` com a mensagem de resgate. Uma chave `secret.key` será gerada.

4.  **Para recuperar os arquivos, execute o script de descriptografia:**
    ```bash
    python decrypt.py
    ```
    Este script usará a `secret.key` para restaurar os arquivos ao seu estado original.

### Executando a Simulação de Keylogger

1.  **Navegue até a pasta do keylogger:**
    ```bash
    cd keylogger_simulado
    ```

2.  **(Opcional) Configure o envio de e-mail:**
    Abra o arquivo `email_sender.py` e preencha as variáveis `email_remetente`, `senha_remetente` e `email_destinatario`. **Use uma "Senha de App" se seu provedor for o Gmail.**

3.  **Execute o script do keylogger:**
    ```bash
    python keylogger.py
    ```
    O terminal ficará "travado" enquanto o script estiver rodando. Comece a digitar em qualquer janela (bloco de notas, navegador, etc.).

4.  **Pare o keylogger:**
    Pressione a tecla `Esc` para parar a captura. O script salvará os registros em `key_log.txt` e, se configurado, enviará o log por e-mail antes de finalizar.

## 🛡️ Reflexão sobre Defesa

A parte mais importante deste projeto é a análise das contramedidas. Um resumo detalhado das técnicas de prevenção, detecção e mitigação para ransomware e keyloggers pode ser encontrado em:

[**📄 Documento de Reflexão sobre Defesa (`docs/reflexao_defesa.md`)**](./docs/reflexao_defesa.md)
