"""
Classes
Aluno
Curso
Instrutor

Associação
Aluno ↔ Curso (muitos para muitos)
Instrutor ↔ Curso
"""
class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.cursos = []

    def adicionar_curso(self, curso):
        if curso not in self.cursos:
            self.cursos.append(curso)

    def exibir_dados_aluno(self):
        print(f"Aluno: {self.nome}")
        if self.cursos:
            print("Cursos:")
            for curso in self.cursos:
                print(f"- {curso.nome}")
        else:
            print("Cursos: Nenhum")
        print("----------------")


class Curso:
    def __init__(self, nome, instrutor):
        self.nome = nome
        self.instrutor = instrutor

    def exibir_dados_curso(self):
        print(f"Curso: {self.nome}")
        print(f"Instrutor: {self.instrutor.nome}")
        print("----------------")


class Instrutor:
    def __init__(self, nome):
        self.nome = nome

    def exibir_instrutor(self):
        print(f"Instrutor: {self.nome}")
        print("----------------")


# Criando objetos
instrutor1 = Instrutor("Marcos Miguel")
curso1 = Curso("Matemática", instrutor1)
curso2 = Curso("História", instrutor1)

aluno1 = Aluno("Ana Maria")
aluno2 = Aluno("Rafael")

# Adicionando cursos aos alunos
aluno1.adicionar_curso(curso1)
aluno2.adicionar_curso(curso1)
aluno2.adicionar_curso(curso2)

# Exibindo informações
aluno1.exibir_dados_aluno()
aluno2.exibir_dados_aluno()

curso1.exibir_dados_curso()
curso2.exibir_dados_curso()

instrutor1.exibir_instrutor()