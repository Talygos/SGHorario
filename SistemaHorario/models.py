from django.db import models
from django.utils import timezone

CargaHoraria_Choices = (
    ('20','20 horas'),
    ('40','40 horas'),
)

CargaHorariaD_Choices = (
    ('40', '40 horas'),
    ('80', '80 horas'),
)

DiaSemana_Choices = (
    ('Segunda', 'Segunda-feira'),
    ('Terca', 'Terca-feira'),
    ('Quarta', 'Quarta-feira'),
    ('Quinta', 'Quinta-feira'),
    ('Sexta', 'Sexta-feira'),   
)

class Login(models.Model):
    usuario = models.CharField(max_length=20)
    senha = models.IntegerField(default=1234)
    tipoUsuario = models.IntegerField(default=0)

class Departamento(models.Model):
    nome = models.CharField(max_length=75, unique=True, blank=False)
    sigla = models.CharField(max_length=5, unique=True, blank=False)

    def __unicode__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=50,  blank=False)
    cargaHoraria = models.CharField(max_length=2, choices=CargaHorariaD_Choices, default=20,  blank=False)
    departamento = models.ForeignKey(Departamento, null=True,  blank=False)

    def __unicode__(self):
        return self.nome

class Professor(models.Model):
    nome = models.CharField(max_length=50,  blank=False)
    cargaHoraria = models.CharField(max_length=2, choices=CargaHoraria_Choices, default=20,  blank=False)
    telefone = models.CharField(max_length=25, null=True)
    email = models.EmailField(max_length=50, null=True,  blank=False)
    departamento = models.ForeignKey(Departamento)
    chefe =  models.BooleanField(default=False)
    disciplina = models.ManyToManyField(Disciplina)

    def __unicode__(self):
        return self.nome
    
class Curso(models.Model):
    nome = models.CharField(max_length=25,  blank=False)
    coordenador = models.ForeignKey(Professor, null=True)

    def __unicode__(self):
        return self.nome
    
class MatrizCurricular(models.Model):
   nomeMatriz = models.CharField(max_length=100,  blank=False)
   curso = models.OneToOneField(Curso, on_delete=models.CASCADE)
   
   def __unicode__(self):
       return unicode(self.nomeMatriz) or u''

class Periodo(models.Model):
    numeroPeriodo = models.IntegerField(default = 1,  blank=False)
    matriz = models.ForeignKey(MatrizCurricular)
    disciplina = models.ManyToManyField(Disciplina)

    def __unicode__(self):
       return unicode(self.matriz) or u''
    
class Turma(models.Model):
    numero = models.CharField(max_length=5,  blank=False)
    semestre =  models.CharField(max_length=10,  blank=False)
    curso = models.ForeignKey(Curso)

    def __unicode__(self):
        return self.numero

class Horario(models.Model):
    turma = models.ForeignKey(Turma)
    semestre =  models.CharField(max_length=10,  blank=False)

class DiaSemana(models.Model):
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    nome =  models.CharField(max_length=20, choices=DiaSemana_Choices, default='Segunda',  blank=False)
    disciplina = models.ManyToManyField(Disciplina)

class Menssagem(models.Model):
    #de = models.ForeignKey(Professor)
    para = models.ForeignKey(Professor)
    assunto = models.CharField(max_length = 50, blank=False)
    menssagem = models.CharField(max_length = 100, blank=False)
    data = models.DateTimeField(blank=True, null=True)
    


    
