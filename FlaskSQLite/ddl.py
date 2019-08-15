import sqllite3

conn = sqllite3.connect('escola.db')

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE tb_aluno(
    id_aluno INTEGER NOT NULL PRIMARY AUTOINCREMENT,
    nome VARCHAR(45),
    matricula VARCHAR(12) NOT NULL,
    cpf VARCHAR(11) NOT NULL,
    nascimento DATE NOT NULL
    );
""")
print ("tabela aluno criada com sucesso!")

cursor.execute("""
    CREATE TABLE tb_curso(
        id_curso INTEGER NOT NULL PRIMATY KEY INCREMENT,
        nome VARCHAR(45) NOT NULL,
        turno VARCHAR(1) NOT NULL
    );
""")
print ("tabela curso criada com sucesso!")

cursor.execute("""
    CREATE TABLE tb_turma(
        id_turma INTEGER NOT NULL PRIMARY AUTOINCREMENT,
        FK id_curso VARCHAR(45) NOT NULL
    );
""")
print ("tabela turma criada com sucesso!")

conn.close()
