from django.contrib import admin
from .models import Sede, Facultad, Programa, PeriodoAcademico
from .models import Grupo, Asignatura, Horario, EspacioFisico
from .models import Recurso, EspacioRecurso, Rol, Usuario, HorarioFusionado
from .models import PrestamoEspacio

# Register your models here.
admin.site.register(Sede)
admin.site.register(Facultad)
admin.site.register(Programa)
admin.site.register(PeriodoAcademico)
admin.site.register(Grupo)
admin.site.register(Asignatura)
admin.site.register(EspacioFisico)
admin.site.register(Recurso)
admin.site.register(EspacioRecurso)
admin.site.register(Rol)
admin.site.register(Usuario)
admin.site.register(Horario)
admin.site.register(HorarioFusionado)
admin.site.register(PrestamoEspacio)


