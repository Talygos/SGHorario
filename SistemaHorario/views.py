from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponseBadRequest, HttpResponse
from .models import Login
from .models import Departamento
from .models import Professor
from .models import Disciplina
from .models import Curso
from .models import Turma
from .models import MatrizCurricular
from .models import Periodo
from .forms  import DepartamentoForm
from .forms  import ProfessorForm
from .forms  import DisciplinaForm
from .forms  import CursoForm
from .forms  import TurmaForm
from .forms  import MatrizCurricularForm
from .forms  import PeriodoForm
from .forms  import HorarioForm
from .forms  import MenssagemForm

def usuario_list(request):
    usuario = Login.objects.all().order_by('usuario')
    return render(request, 'SistemaHorario/Index.html', {'usuario': usuario})

def tela(request):
    usuario = Login.objects.all().order_by('usuario')
    return render(request, 'SistemaHorario/TelaInicial.html', {'usuario': usuario})

def departamentos(request):
    departamentos = Departamento.objects.all().order_by('nome')
    if request.method == "POST":
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            Departamento.author = request.user
            form.save()
            return redirect('SistemaHorario.views.departamentos')
        else:
            return HttpResponseBadRequest('ERROR!')
    else:
        form = DepartamentoForm()
    return render(request, 'SistemaHorario/Departamentos.html', {'form': form, 'departamentos': departamentos})

def departamento_detail(request, pk):
    departamento = get_object_or_404(Departamento, pk=pk)
    if request.method == "POST":
        form = DepartamentoForm(request.POST, instance=departamento)
        if form.is_valid():
            Departamento.author = request.user
            form.save()
            return redirect('SistemaHorario.views.departamentos')
    else:
        form = DepartamentoForm(instance=departamento)
    return render(request, 'SistemaHorario/Departamento.html', {'form': form})
    
def departamento_excluir(request, pk):
    departamento = get_object_or_404(Departamento, pk=pk)
    departamento.delete()
    return redirect('SistemaHorario.views.departamentos')

def disciplinas(request):
    disciplinas = Disciplina.objects.all().order_by('nome')
    departamentos = Departamento.objects.all()
    if request.method == "POST":
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            Disciplina.author = request.user
            Departamento.author = request.user
            form.save()
            return redirect('SistemaHorario.views.disciplinas')
    else:
        form = DisciplinaForm()
    return render(request, 'SistemaHorario/Disciplinas.html', {'form': form, 'disciplinas':disciplinas, 'departamentos': departamentos})

def disciplina_detail(request, pk):
    disciplina = get_object_or_404(Disciplina, pk=pk)
    if request.method == "POST":
        form = DisciplinaForm(request.POST, instance=disciplina)
        if form.is_valid():
            Disciplina.author = request.user
            form.save()
            return redirect('SistemaHorario.views.disciplinas')
    else:
        form = DisciplinaForm(instance=disciplina)
    return render(request, 'SistemaHorario/Disciplina.html', {'form': form})

def disciplina_excluir(request, pk):
    disciplina = get_object_or_404(Disciplina, pk=pk)
    disciplina.delete()
    return redirect('SistemaHorario.views.disciplinas')

def professores(request):
    departamentos = Departamento.objects.all()
    disciplinas = Disciplina.objects.all()
    professores = Professor.objects.all().order_by('nome')
    if request.method == "POST":
        form = ProfessorForm(request.POST)
        if form.is_valid():
            Professor.author = request.user
            Disciplina.author = request.user
            Departamento.author = request.user
            form.save()
            return redirect('SistemaHorario.views.professores')
    else:
        form = ProfessorForm()
    return render(request, 'SistemaHorario/Professores.html', {'form': form, 'professores':professores, 'departamentos': departamentos, 'disciplinas':disciplinas})

def professor_detail(request, pk):
    professor = get_object_or_404(Professor, pk=pk)
    if request.method == "POST":
        form = ProfessorForm(request.POST, instance=professor)
        if form.is_valid():
            Professor.author = request.user
            form.save()
            return redirect('SistemaHorario.views.professores')
    else:
        form = ProfessorForm(instance=professor)
    return render(request, 'SistemaHorario/Professor.html', {'form': form})

def professor_excluir(request, pk):
    professor = get_object_or_404(Professor, pk=pk)
    professor.delete()
    return redirect('SistemaHorario.views.professores')


def cursos(request):
    cursos = Curso.objects.all()
    professores = Professor.objects.all().order_by('nome')
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            Curso.author = request.user
            professores.author = request.user
            form.save()
            return redirect('SistemaHorario.views.cursos')
    else:
        form = CursoForm()
    return render(request, 'SistemaHorario/Cursos.html', {'form': form, 'cursos': cursos, 'professores':professores})

def curso_detail(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == "POST":
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            Curso.author = request.user
            form.save()
            return redirect('SistemaHorario.views.cursos')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'SistemaHorario/Curso.html', {'form': form})

def curso_excluir(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    curso.delete()
    return redirect('SistemaHorario.views.cursos')

def turmas(request):
    turmas = Turma.objects.all()
    curso = Curso.objects.all()
    if request.method == "POST":
        form = TurmaForm(request.POST)
        if form.is_valid():
            Turma.author = request.user
            curso.author = request.user
            form.save()
            return redirect('SistemaHorario.views.turmas')
    else:
        form = TurmaForm()
    return render(request, 'SistemaHorario/Turmas.html', {'form': form, 'turmas': turmas, 'curso':curso})

def turma_detail(request, pk):
    turma = get_object_or_404(Turma, pk=pk)
    if request.method == "POST":
        form = TurmaForm(request.POST, instance=turma)
        if form.is_valid():
            Turma.author = request.user
            form.save()
            return redirect('SistemaHorario.views.turmas')
    else:
        form = TurmaForm(instance=turma)
    return render(request, 'SistemaHorario/Turma.html', {'form': form})

def turma_excluir(request, pk):
    turma = get_object_or_404(Turma, pk=pk)
    turma.delete()
    return redirect('SistemaHorario.views.turmas')

def matrizescurriculares(request):
    matrizescurriculares = MatrizCurricular.objects.all()
    cursos = Curso.objects.all()
    if request.method == "POST":
        form = MatrizCurricularForm(request.POST)
        if form.is_valid():
            MatrizCurricular.author = request.user
            Disciplina.author = request.user
            Curso.author = request.user
            form.save()
            return redirect('SistemaHorario.views.matrizescurriculares')
    else:
        form = MatrizCurricularForm()
    return render(request, 'SistemaHorario/MatrizCurriculares.html', {'form': form, 'matrizescurriculares': matrizescurriculares, 'cursos':cursos})

def matrizcurricular_excluir(request, pk):
    matrizcurricular = get_object_or_404(MatrizCurricular, pk=pk)
    matrizcurricular.delete()
    return redirect('SistemaHorario.views.matrizescurriculares')

def adicionarperiodo(request, pk):
    matrizPeriodo = get_object_or_404(MatrizCurricular, pk=pk)
    periodos = Periodo.objects.all().filter(matriz = pk).order_by('numeroPeriodo')
    disciplinas = Disciplina.objects.all()
    if request.method == "POST":
        form = PeriodoForm(request.POST)
        if form.is_valid():
            Periodo.author = request.user
            form.save()
            return redirect('SistemaHorario.views.matrizescurriculares')
    else:
        form = PeriodoForm()
    return render(request, 'SistemaHorario/MatrizCurricular.html', {'form': form, 'disciplinas':disciplinas,'periodos': periodos, 'matrizPeriodo': matrizPeriodo})

def excluirperiodo(request, pk):
    periodo = get_object_or_404(Periodo, pk=pk)
    periodo.delete()
    return redirect('SistemaHorario.views.matrizescurriculares')
    
def horarios(request):
    return render(request, 'SistemaHorario/Horarios.html', {})

def chat(request):
    if request.method == "POST":
        form = MenssagemForm(request.POST)
        if form.is_valid():
            menssagem = form.save(commit=False)
            menssagem.author = request.user
            menssagem.data = timezone.now()
            menssagem.save()
            return redirect('SistemaHorario.views.chat')
    else:
        form = MenssagemForm()
    return render(request, 'SistemaHorario/CaixaEntrada.html', {'form':form})
                  #, {'form':form})

def adicionarHorario(request):
    turmas = Turma.objects.all()
    if request.method == "POST":
        form = HorarioForm(request.POST)
        if form.is_valid():
            Horario.author = request.user
            form.save()
            return redirect('SistemaHorario.views.horarios')
    else:
        form = PeriodoForm()
    return render(request, 'SistemaHorario/Horario.html', {'form': form, 'turmas':turmas})

def horario(request):
    horario = Horario.objects.all()
    turma = Turma.objects.all()
    if request.method == "POST":
       form = HorarioForm(request.POST)
       if form.is_valid():
            horario.author = request.user
            turma.author = request.user
            form.save()
            return redirect('SistemaHorario.views.horario')
    else:
        form = HorarioForm()
    return render(request, 'SistemaHorario/Horario.html', {'form': form, 'horario': horario, 'turma':turma})
       
