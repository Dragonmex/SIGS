# **SIGS - Backend**

Sistema Integrado de Gestão de Serviços Públicos (SIGS). Este repositório contém o back-end do projeto desenvolvido em **Python 3.10.11** com **Django** e **PostgreSQL 15**.

---

## **Pré-requisitos**

Certifique-se de ter os seguintes itens disponíveis:

- [python-3.10.11](https://github.com/Dragonmex/SIGS/tree/master/instaladores)
- [postgresql-15-x64](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
- [Git](https://git-scm.com/downloads)
- Microsoft Visual C++ Build Tools (veja o passo 5).

---

Pré-requisitos

Certifique-se de ter os seguintes itens disponíveis:

    Diretório instaladores/ contendo:
        python-3.10.11-amd64.exe (instalador do Python)
    PostgreSQL 15 (baixe e instale manualmente).
    Git instalado no sistema.
    Microsoft Visual C++ Build Tools (veja o passo 5).



## **Passo a Passo para Configuração**

### **1. Clone o Repositório**

Abra o terminal ou o Git Bash e execute os comandos abaixo:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio/backend
```

### **2. Instale o Python 3.10.11**

1. Navegue até o diretório `instaladores/`.
2. Execute o arquivo `python-3.10.11-amd64.exe`.
3. Durante a instalação:
    - Habilite a opção **"Add Python to PATH"**.
    - Escolha **"Instalação personalizada"** e ative todas as opções recomendadas.
4. Teste a instalação:

```bash
python --version
```

### **3. Instale o PostgreSQL 15**

1. No diretório `instaladores/`, execute o arquivo `postgresql-15-x64.exe`.
2. Durante a instalação:
    - Configure a senha do usuário padrão `postgres`.
    - Habilite a instalação do **pgAdmin4** (opcional).
3. Teste a instalação:
    - Abra o terminal e execute:

```bash
psql -U postgres
```

- Digite a senha configurada e pressione **Enter**.
- Crie o banco de dados:

```bash
CREATE DATABASE app;
```

- Saia do PostgreSQL:

```bash
\q
```

### **4. Crie o Ambiente Virtual**

No diretório do repositório, execute:

```bash
python -m venv venv
venv\Scripts\activate
```

Se tudo estiver correto, você verá o nome do ambiente virtual `(venv)` no início do terminal.

### **5. Instale o Microsoft Visual C++ Build Tools**

O **psycopg2**, biblioteca usada para conectar ao PostgreSQL, requer o Microsoft Visual C++ para compilar corretamente. Siga os passos abaixo:

1. Baixe o instalador do Visual C++ Build Tools em [https://visualstudio.microsoft.com/visual-cpp-build-tools/](https://visualstudio.microsoft.com/visual-cpp-build-tools/).
2. Execute o instalador e selecione:
    - **Desktop development with C++**
3. Conclua a instalação e reinicie o terminal.


### **6. Instale as Dependências**

Com o ambiente virtual ativado, execute:

```bash
pip install -r requirements.txt
```

### **7. Configure o Banco de Dados**

No arquivo `backend/settings.py`, atualize as configurações do banco de dados:


```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'app',
        'USER': 'postgres',
        'PASSWORD': 'sua_senha',  # Substitua pela senha configurada
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

```

### **8. Execute as Migrações**

Crie as tabelas do banco de dados com os comandos:

```python
python manage.py makemigrations
python manage.py migrate

```


### **9. Popule o Banco de Dados**

Rode o comando para preencher o banco de dados com dados iniciais:

```python
python manage.py populate_db
```

### **10. Inicie o Servidor**

Por fim, inicie o servidor de desenvolvimento:

```python
python manage.py runserver
```

# Comandos Úteis

**Criar superusuário**:

```python
python manage.py createsuperuser
```

**Ativar ambiente virtual**:

```python
venv\Scripts\activate
```

**Desativar ambiente virtual**:

```python
deactivate
```
