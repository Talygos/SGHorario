from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.usuario_list),
    url(r'^menu/$', views.tela),
    url(r'^departamentos/$', views.departamentos),
    url(r'^departamento/(?P<pk>[0-9]+)/$', views.departamento_detail),
    url(r'^departamento/(?P<pk>[0-9]+)/morte/$', views.departamento_excluir),
    url(r'^professores/$', views.professores),
    url(r'^professor/(?P<pk>[0-9]+)/$', views.professor_detail),
    url(r'^professor/(?P<pk>[0-9]+)/morte/$', views.professor_excluir),
    url(r'^disciplinas/$', views.disciplinas),
    url(r'^disciplina/(?P<pk>[0-9]+)/$', views.disciplina_detail),
    url(r'^disciplina/(?P<pk>[0-9]+)/morte/$', views.disciplina_excluir),
    url(r'^cursos/$', views.cursos),
    url(r'^curso/(?P<pk>[0-9]+)/$', views.curso_detail),
    url(r'^curso/(?P<pk>[0-9]+)/morte/$', views.curso_excluir),
    url(r'^turmas/$', views.turmas),
    url(r'^turma/(?P<pk>[0-9]+)/$', views.turma_detail),
    url(r'^turma/(?P<pk>[0-9]+)/morte/$', views.turma_excluir),
    url(r'^matrizescurriculares/$', views.matrizescurriculares),
    url(r'^matrizescurriculares/(?P<pk>[0-9]+)/morte/$', views.matrizcurricular_excluir),
    url(r'^matrizescurriculares/(?P<pk>[0-9]+)/adicionar-periodo/$', views.adicionarperiodo),
    url(r'^matrizescurriculares/(?P<pk>[0-9]+)/excluir-periodo/$', views.excluirperiodo),
    url(r'^horarios/$', views.horarios),
    url(r'^horarios/novo-horario/$', views.adicionarHorario),
    url(r'^chat/$', views.chat),
    #url(r'^horario/novo-horario/$', views.horario),
    #url(r'^matrizcurricular/(?P<pk>[0-9]+)/$', views.matrizCurricular_detail),
    #url(r'^matrizcurricular/(?P<pk>[0-9]+)/morte/$', views.matrizCurricular_excluir),
    #url(r'^professores/filter/disciplina-by-departamento/$', 'filter', {'model_class': Professor, 'field_name': 'disciplina'},  name='state_filter')

]
