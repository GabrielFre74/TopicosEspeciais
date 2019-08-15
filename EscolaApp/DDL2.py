import sqlite3

conn = sqlite3.connect('EscolaApp_versao2.db')

cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE tb_escola(
        id_escola INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(45) NOT NULL
    );
""")
print("Tabela escola criada com sucesso!")

cursor.execute("""
    CREATE TABLE tb_aluno(
        id_aluno INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(45) NOT NULL,
        matricula VARCHAR(12) NOT NULL,
        cpf VARCHAR(11) NOT NULL,
        nascimento DATE NOT NULL
    );
""")
print("Tabela aluno criada com sucesso!")

cursor.execute("""
    CREATE TABLE tb_curso(
        id_curso INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(45) NOT NULL,
        turno VARCHAR(10) NOT NULL
    );
""")
print("Tabela curso criada com sucesso!")

cursor.execute("""
    CREATE TABLE tb_turma(
        id_turma INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(45) NOT NULL
    );
""")
print("Tabela turma criada com sucesso!")

cursor.execute("""
    CREATE TABLE tb_disciplina(
        id_disciplina INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(45)
    );
""")
print("Tabela disciplina criada com sucesso!")

cursor.execute("""
    CREATE TABLE tb_turno(
        id_turno INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(45)
    );
""")
print("Tabela turno criada com sucesso!")

cursor.execute("""
    CREATE TABLE tb_campus(
        id_campus INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        sigla VARCHAR(10),
        cidade VARCHAR(45)
    );
""")
print("Tabela campus criada com sucesso!")

cursor.execute("""
    CREATE TABLE tb_professor(
        id_professor INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(45)
    );
""")
print("Tabela professor criada com sucesso!")

cursor.execute("""
    CREATE TABLE tb_endereco(
        id_endereco INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        logradouro VARCHAR(65),
        complemento VARCHAR(45),
        bairro VARCHAR(45),
        cep VARCHAR(8),
        numero INTEGER
    );
""")
print("Tabela endereco criada com sucesso!")

conn.close()
