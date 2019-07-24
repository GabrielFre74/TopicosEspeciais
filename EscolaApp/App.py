from flask import Flask, request, jsonify
import logging
import sqlite3

app = Flask(__name__)

formater = logging.Formatter("%(asctime)S - %(levelname)s - %(message)s")
handler = logging.FileHandler("escolaapp.log")
handler.setFormatter(formatter)

logger = app.logger
logger.addHandler(handler)
logger.setLevel(logging.INFO)

@app.route("/escolas", methods= ['GET'])
def getEscolas():
    try:
        loger.info("Listando escolas.")

        conn = sqlite3.connect('escola.db')

        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM tb_escola;
        """)
        for linha in cursor.fetchall():
            escola = {
                "id_escola": linha[0],
                "nome": linha[1],
                "logradouro": linha[2],
                "cidade": linha[3]
                }
            escolas.append(escola)

            conn.close()
    except(sqlite3.Error):
        looger.error("Aconteceu um erro.")

    return jsonify(escolas)

@app.route("/escolas/<int:id>", methods=['GET'])
def getEscolasByID(id):
    try:
        logger.info("Listando escola por id: %s" %(id))
        conn = sqlite3.connect('escola.db')

        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM tb_escola where id = ?;
        """, (id, ))

        linha = cursor.fetchone()
        escola = {
            "id_escola": linha[0],
            "nome": linha[1],
            "logradouro": linha[2],
            "cidade": linha[3]
        }

        conn.close()

    except(sqlite3.Error):
        looger.error("Aconteceu um erro.")

    return jsonify(escola)

@app.route("/escola", methods=['POST'])
def setEscola():
    try:
        logger.info("Inserindo escolas.")

        escola = request.get_json()
        nome = escola['nome']
        logradouro = escola['logradouro']
        cidade = escola['cidade']

        conn = sqlite3.connect('escola.db')

        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO tb_escola(nome, logradouro, cidade)
            VALUES(?,?,?);
        """, (nome, logradouro, cidade))

        conn.commit()
        conn.close()

        id = cursor.lastrowid
        escola["id_escola"] = id

    except(sqlite3.Error):
        looger.error("Aconteceu um erro.")

    return jsonify(escola)


@app.route("/alunos", methods=['GET'])
def getAlunos():
    try:
        logger.info("Listando alunos.")

        conn = sqlite3.connect('escola.db')

        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM tb_aluno;
        """)

        for linha in cursor.fetchall():
            aluno = {
    		      "id_aluno": linha[0],
                  "nome": linha[1],
                  "matricula": linha[2],
                  "cpf": linha[3],
                  "nascimento": linha[4]
            }
            alunos.append(aluno)
        conn.close()
    except(sqlite3.Error):
        looger.error("Aconteceu um erro.")
    return jsonify(alunos)

@app.route("/alunos/<int:id>", methods=['GET'])
def getAlunosByID(id):
    try:
        logger.info("Listando alunos por id: %s" %(id))

        conn = sqlite3.connect('escola.db')
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM tb_aluno where id_aluno=?;
        """, (id, ))

        linha = cursor.fetchone()
        aluno = {
              "id_aluno": linha[0],
              "nome": linha[1],
              "matricula": linha[2],
              "cpf": linha[3],
              "nascimento": linha[4]
        }

        conn.close()
    except(sqlite3.Error):
        looger.error("Aconteceu um erro.")
    return jsonify(aluno)

@app.route("/aluno", methods=['POST'])
def setAluno():
    try:
        logger.info("Inserindo alunos.")
        aluno = request.get_json()
        nome = aluno['nome']
        matricula = aluno['matricula']
        cpf = aluno['cpf']
        nascimento = aluno['nascimento']

        conn = sqlite3.connect('escola.db')

        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO tb_aluno(nome, matricula, cpf, nascimento)
            VALUES(?,?,?,?);
        """, (nome, matricula, cpf, nascimento))

        conn.commit()
        conn.close()

        id = cursor.lastrowid
        aluno["id_aluno"] = id

    except(sqlite3.Error):
        looger.error("Aconteceu um erro.")
    return jsonify(aluno)


@app.route("/cursos", methods=['GET'])
def getCursos():
    try:
        logger.info("Listando cursos.")
        conn = sqlite3.connect('escola.db')

        cursor = conn.cursor()

        cursor.execute("""
            SELECT* FROM tb_curso;
        """)
        for linha in cursor.fetchall():
            curso = {
                "id_curso": linha[0],
                "nome": linha[1],
                "turno": linha[2]
            }
            cursos.append(curso)

        conn.close()
    except(sqlite3.Error):
        looger.error("Aconteceu um erro.")
    return jsonify(cursos)

@app.route("/cursos/<int:id>", methods=['GET'])
def getCursosByID(id):
    try:
        logger.info("Listando cursos por id: %s" %(id))
        conn = sqlite3.connect('escola.db')
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM tb_curso where id=?;
        """, (id, ))

        linha = cursor.fetchone()
        curso = {
            "id_curso": linha[0],
            "nome": linha[1],
            "turno": linha[2]
        }

        conn.close()
    except(sqlite3.Error):
        looger.error("Aconteceu um erro.")
    return jsonify(curso)

@app.route("/curso", methods=['POST'])
def setCurso():
    try:
        logger.info("Inserindo curso.")

        curso = request.get_json()
        nome = curso['nome']
        turno = curso['turno']

        conn = sqlite3.connect('escola.db')
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO tb_curso (nome, turno) values(?,?);
        """, (nome, turno, ))

        conn.commit()
        conn.close()

        id = cursor.lastrowid
        curso["id_curso"] = id

    except(sqlite3.Error):
        looger.error("Aconteceu um erro.")
    return jsonify(curso)


@app.route("/turmas", methods=['GET'])
def getTurmas():
    try:
        logger.info("Listando turmas.")
        conn = sqlite3.connect('escola.db')

        cursor = conn.cursor()

        cursor.execute("""
            SELECT* FROM tb_turma;
        """)
        for linha in cursor.fetchall():
            turma = {
                "id_turma": linha[0],
                "nome": linha[1],
                "curso": linha[2]
            }
            turmas.append(turma)

        conn.close()
    except(sqlite3.Error):
        looger.error("Aconteceu um erro.")
    return jsonify(turmas)


@app.route("/turmas/<int:id>", methods=['GET'])
def getTurmasByID(id):
    try:
        logger.info("Listando turma por id: %s" %(id))
        conn = sqlite3.connect('escola.db')
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM tb_turma where id=?;
        """, (id, ))

        linha = cursor.fetchone()
        turma = {
            "id_turma": linha[0],
            "nome": linha[1],
            "curso": linha[2]
        }

        conn.close()
    except(sqlite3.Error):
        looger.error("Aconteceu um erro.")
    return jsonify(turma)


@app.route("/turma", methods=['POST'])
def setTurma():
    try:
        logger.info("Inserindo turma.")

        turma = request.get_json()
        nome = turma['nome']
        curso = turma['curso']

        conn = sqlite3.connect('escola.db')
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO tb_turma (nome, curso) VALUES (?,?);
        """, (nome, curso, ))

        conn.commit()
        conn.close()

        id = cursor.lastrowid
        turma["id_turma"] = id

    except(sqlite3.Error):
        looger.error("Aconteceu um erro.")
    return jsonify(turma)

@app.route("/disciplinas", methods=['GET'])
def getDisciplinas():
    try:
        logger.info("Listando disciplinas.")
        conn = sqlite3.connect('escola.db')

        cursor = conn.cursor()

        cursor.execute("""
            SELECT* FROM tb_disciplina;
        """)
        for linha in cursor.fetchall():
            disciplina = {
                "id_disciplina": linha[0],
                "nome": linha[1]
            }
            disciplinas.append(disciplina)

        conn.close()
    except(sqlite3.Error):
        looger.error("Aconteceu um erro.")
    return jsonify(disciplinas)

@app.route("/disciplinas/<int:id>", methods=['GET'])
def getDisciplinasByID(id):
    try:
        logger.info("Listando disciplina por id: %s" %(id))
        conn = sqlite3.connect('escola.db')
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM tb_disciplina where id=?;
        """, (id, ))

        linha = cursor.fetchone()
        disciplina = {
            "id_disciplina": linha[0],
            "nome": linha[1]
        }

        conn.close()
    except(sqlite3.Error):
        looger.error("Aconteceu um erro.")
    return jsonify(disciplina)


@app.route("/disciplina", methods=['POST'])
def setDisciplina():
    try:
        logger.info("Inserindo disciplina.")

        disciplina = request.get_json()
        nome = disciplina['nome']

        conn = sqlite3.connect('escola.db')
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO tb_disciplina (nome) VALUES (?);
        """, (nome, ))

        conn.commit()
        conn.close()

        id = cursor.lastrowid
        disciplina["id_disciplina"] = id

    except(sqlite3.Error):
        looger.error("Aconteceu um erro.")
    return jsonify(disciplina)


if(__name__ == '__main__'):
    app.run(host='0.0.0.0', debug=True, use_reloader=True)
