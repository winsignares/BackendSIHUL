from django.urls import path
from . import views

urlpatterns = [
    path('', views.crud, name='crud'),

    # Rol
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('create_rol/', views.create_rol, name='create_rol'),
    path('update_rol/', views.update_rol, name='update_rol'),
    path('delete_rol/', views.delete_rol, name='delete_rol'),
    path('get_rol/<int:id>/', views.get_rol, name='get_rol'),
    path('get_rol/', views.list_roles, name='list_roles'),

    # Sede
    path('create_sede/', views.create_sede, name='create_sede'),
    path('update_sede/', views.update_sede, name='update_sede'),
    path('delete_sede/', views.delete_sede, name='delete_sede'),
    path('get_sede/<int:id>/', views.get_sede, name='get_sede'),
    path('get_sede/', views.list_sedes, name='list_sedes'),

    # Facultad
    path('create_facultad/', views.create_facultad, name='create_facultad'),
    path('update_facultad/', views.update_facultad, name='update_facultad'),
    path('delete_facultad/', views.delete_facultad, name='delete_facultad'),
    path('get_facultad/<int:id>/', views.get_facultad, name='get_facultad'),
    path('get_facultad/', views.list_facultades, name='list_facultades'),

    # Programa
    path('create_programa/', views.create_programa, name='create_programa'),
    path('update_programa/', views.update_programa, name='update_programa'),
    path('delete_programa/', views.delete_programa, name='delete_programa'),
    path('get_programa/<int:id>/', views.get_programa, name='get_programa'),
    path('get_programa/', views.list_programas, name='list_programas'),

    # PeriodoAcademico
    path('create_periodo/', views.create_periodo, name='create_periodo'),
    path('update_periodo/', views.update_periodo, name='update_periodo'),
    path('delete_periodo/', views.delete_periodo, name='delete_periodo'),
    path('get_periodo/<int:id>/', views.get_periodo, name='get_periodo'),
    path('get_periodo/', views.list_periodos, name='list_periodos'),

    # Grupo
    path('create_grupo/', views.create_grupo, name='create_grupo'),
    path('update_grupo/', views.update_grupo, name='update_grupo'),
    path('delete_grupo/', views.delete_grupo, name='delete_grupo'),
    path('get_grupo/<int:id>/', views.get_grupo, name='get_grupo'),
    path('get_grupo/', views.list_grupos, name='list_grupos'),

    # Asignatura
    path('create_asignatura/', views.create_asignatura, name='create_asignatura'),
    path('update_asignatura/', views.update_asignatura, name='update_asignatura'),
    path('delete_asignatura/', views.delete_asignatura, name='delete_asignatura'),
    path('get_asignatura/<int:id>/', views.get_asignatura, name='get_asignatura'),
    path('get_asignatura/', views.list_asignaturas, name='list_asignaturas'),

    # EspacioFisico
    path('create_espacio/', views.create_espacio, name='create_espacio'),
    path('update_espacio/', views.update_espacio, name='update_espacio'),
    path('delete_espacio/', views.delete_espacio, name='delete_espacio'),
    path('get_espacio/<int:id>/', views.get_espacio, name='get_espacio'),
    path('get_espacio/', views.list_espacios, name='list_espacios'),

    # Recurso
    path('create_recurso/', views.create_recurso, name='create_recurso'),
    path('update_recurso/', views.update_recurso, name='update_recurso'),
    path('delete_recurso/', views.delete_recurso, name='delete_recurso'),
    path('get_recurso/<int:id>/', views.get_recurso, name='get_recurso'),
    path('get_recurso/', views.list_recursos, name='list_recursos'),

    # EspacioRecurso
    path('create_espacio_recurso/', views.create_espacio_recurso, name='create_espacio_recurso'),
    path('update_espacio_recurso/', views.update_espacio_recurso, name='update_espacio_recurso'),
    path('delete_espacio_recurso/', views.delete_espacio_recurso, name='delete_espacio_recurso'),
    path('get_espacio_recurso/<int:espacio_id>/<int:recurso_id>/', views.get_espacio_recurso, name='get_espacio_recurso'),
    path('get_espacio_recurso/', views.list_espacio_recursos, name='list_espacio_recursos'),

    # Usuario
    path('create_usuario/', views.create_usuario, name='create_usuario'),
    path('update_usuario/', views.update_usuario, name='update_usuario'),
    path('delete_usuario/', views.delete_usuario, name='delete_usuario'),
    path('get_usuario/<int:id>/', views.get_usuario, name='get_usuario'),
    path('get_usuario/', views.list_usuarios, name='list_usuarios'),

    # Horario
    path('create_horario/', views.create_horario, name='create_horario'),
    path('update_horario/', views.update_horario, name='update_horario'),
    path('delete_horario/', views.delete_horario, name='delete_horario'),
    path('get_horario/<int:id>/', views.get_horario, name='get_horario'),
    path('get_horario/', views.list_horarios, name='list_horarios'),

    # HorarioFusionado
    path('create_horario_fusionado/', views.create_horario_fusionado, name='create_horario_fusionado'),
    path('update_horario_fusionado/', views.update_horario_fusionado, name='update_horario_fusionado'),
    path('delete_horario_fusionado/', views.delete_horario_fusionado, name='delete_horario_fusionado'),
    path('get_horario_fusionado/<int:id>/', views.get_horario_fusionado, name='get_horario_fusionado'),
    path('get_horario_fusionado/', views.list_horarios_fusionados, name='list_horarios_fusionados'),

    # PrestamoEspacio
    path('create_prestamo/', views.create_prestamo, name='create_prestamo'),
    path('update_prestamo/', views.update_prestamo, name='update_prestamo'),
    path('delete_prestamo/', views.delete_prestamo, name='delete_prestamo'),
    path('get_prestamo/<int:id>/', views.get_prestamo, name='get_prestamo'),
    path('get_prestamo/', views.list_prestamos, name='list_prestamos'),
]
