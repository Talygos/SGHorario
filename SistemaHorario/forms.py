from django import forms

from .models import Departamento
from .models import Disciplina
from .models import Professor
from .models import Curso
from .models import Turma
from .models import MatrizCurricular
from .models import Periodo
from .models import Horario
from .models import Menssagem

import os

class DepartamentoForm(forms.ModelForm):

    class Meta:
        model = Departamento
        fields = ('nome', 'sigla',)


class DisciplinaForm(forms.ModelForm):

    class Meta:
        model = Disciplina
        fields = ('nome', 'cargaHoraria', 'departamento',)

class ProfessorForm(forms.ModelForm):

    class Meta:
        model = Professor
        fields = ('nome', 'telefone', 'email', 'cargaHoraria', 'departamento', 'chefe', 'disciplina',)
        
class CursoForm(forms.ModelForm):

    class Meta:
        model = Curso
        fields = ('nome', 'coordenador',)

class MatrizCurricularForm(forms.ModelForm):

    class Meta:
        model = MatrizCurricular
        fields = ('nomeMatriz','curso',)
        
class TurmaForm(forms.ModelForm):

    class Meta:
        model = Turma
        fields = ('numero', 'semestre', 'curso',)

class PeriodoForm(forms.ModelForm):

    class Meta:
        model = Periodo
        fields = ('numeroPeriodo','matriz','disciplina',)

class HorarioForm(forms.ModelForm):

    class Meta:
        model = Horario
        fields = ('turma','semestre',)

class MenssagemForm(forms.ModelForm):

    class Meta:
        model = Menssagem
        fields = ('para', 'assunto', 'menssagem','data',)








