from django.db import models

NIVEL_CHOICES = (
    ('estagiario', 'Estagiário'),
    ('trainee', 'Trainee'),
    ('junior', 'Júnior'),
    ('pleno', 'Pleno'),
    ('senior', 'Sênior'),
    ('especialista', 'Especialista'),
)

CARGO_CHOICES = (
    ('engenheiro_de_dados', 'Engenheiro de Dados'),
    ('cientista_de_dados', 'Cientista de Dados'),
    ('engenheiro_de_machine_learning', 'Engenheiro de Machine Learning'),
    ('mlops', 'MLOps'),
    ('analista_de_dados', 'Analista de Dados'),
    ('lider_de_equipe', 'Líder de Equipe'),
    ('gerente_de_projetos', 'Gerente de Projetos'),
    ('gerente_de_ciencia_de_dados', 'Gerente de Ciência de Dados'),
    ('diretor_de_ciencia_de_dados', 'Diretor de Ciência de Dados'),
)

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50, choices=CARGO_CHOICES)
    nivel = models.CharField(max_length=15, choices=NIVEL_CHOICES)
    salario = models.DecimalField(max_digits=8, decimal_places=2)
    data_contratacao = models.DateField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    def aumentar_salario(self, percentual):
        aumento = self.salario * percentual / 100
        self.salario += aumento
        self.save()

    def demitir(self):
        self.ativo = False
        self.save()

