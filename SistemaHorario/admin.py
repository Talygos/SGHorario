from django.contrib import admin
from .models import Departamento
from .models import Professor
from .models import Disciplina
from .models import MatrizCurricular
from .models import Curso
from .models import Turma
from .models import Login
from .models import Periodo

admin.site.register(Departamento)
admin.site.register(Professor)
admin.site.register(Disciplina)
admin.site.register(MatrizCurricular)
admin.site.register(Curso)
admin.site.register(Turma)
admin.site.register(Periodo)
admin.site.register(Login)

