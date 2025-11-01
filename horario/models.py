from django.db import models
from django.db.models import F, CheckConstraint, ExpressionWrapper, BooleanField, Index
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Q

# Create your models here.

class Sede(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=150, blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Facultad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Programa(models.Model):
    id = models.AutoField(primary_key=True)
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE, related_name='programas')
    nombre = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class PeriodoAcademico(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Grupo(models.Model):
    id = models.AutoField(primary_key=True)
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE, related_name='grupos')
    periodo = models.ForeignKey(PeriodoAcademico, on_delete=models.CASCADE, related_name='grupos')
    nombre = models.CharField(max_length=50)
    semestre = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    activo = models.BooleanField(default=True)

    class Meta:
        indexes = [
            Index(fields=['periodo'], name='idx_grupo_periodo'),
        ]

    def __str__(self):
        return self.nombre

class Asignatura(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)
    creditos = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

class EspacioFisico(models.Model):
    id = models.AutoField(primary_key=True)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE, related_name='espacios')
    tipo = models.CharField(max_length=50)
    capacidad = models.PositiveIntegerField()
    ubicacion = models.CharField(max_length=100, blank=True, null=True)
    recursos = models.TextField(blank=True, null=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.tipo} ({self.ubicacion or 'sin ubicación'})"

class Recurso(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre or str(self.id)

class EspacioRecurso(models.Model):
    espacio = models.ForeignKey(EspacioFisico, on_delete=models.CASCADE, related_name='espacio_recursos')
    recurso = models.ForeignKey(Recurso, on_delete=models.CASCADE, related_name='recurso_espacios')
    disponible = models.BooleanField(default=True)

    class Meta:
        unique_together = (('espacio', 'recurso'),)

    def __str__(self):
        return f"{self.espacio} - {self.recurso}"

class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100, unique=True)
    contrasena_hash = models.CharField(max_length=255)
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True, blank=True, related_name='usuarios')
    activo = models.BooleanField(default=True)

    class Meta:
        indexes = [
            Index(fields=['rol'], name='idx_usuario_rol'),
        ]

    def __str__(self):
        return self.nombre

class Horario(models.Model):
    id = models.AutoField(primary_key=True)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='horarios')
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE, related_name='horarios')
    docente = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name='horarios_docente')
    espacio = models.ForeignKey(EspacioFisico, on_delete=models.CASCADE, related_name='horarios')
    dia_semana = models.CharField(max_length=15)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    cantidad_estudiantes = models.IntegerField(null=True, blank=True)

    class Meta:
        constraints = [
            CheckConstraint(
                check=Q(hora_fin__gt=F('hora_inicio')),
                name='chk_horario_horas',
            ),
        ]
        indexes = [
            Index(fields=['espacio'], name='idx_horario_espacio'),
            Index(fields=['docente'], name='idx_horario_docente'),
        ]


    def __str__(self):
        return f"{self.dia_semana} {self.hora_inicio}-{self.hora_fin}"

class HorarioFusionado(models.Model):
    id = models.AutoField(primary_key=True)
    grupo1 = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='horarios_fusionados_1')
    grupo2 = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='horarios_fusionados_2')
    grupo3 = models.ForeignKey(Grupo, on_delete=models.CASCADE, null=True, blank=True, related_name='horarios_fusionados_3')
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE, related_name='horarios_fusionados')
    docente = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name='horarios_fusionados')
    espacio = models.ForeignKey(EspacioFisico, on_delete=models.CASCADE, related_name='horarios_fusionados')
    dia_semana = models.CharField(max_length=15)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    cantidad_estudiantes = models.IntegerField(null=True, blank=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        constraints = [
            CheckConstraint(
                check=Q(hora_fin__gt=F('hora_inicio')),
                name='chk_horario_fusionado_horas',
            ),
        ]


    def __str__(self):
        return f"Fusionado {self.asignatura} {self.dia_semana}"

class PrestamoEspacio(models.Model):
    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('Aprobado', 'Aprobado'),
        ('Rechazado', 'Rechazado'),
        ('Vencido', 'Vencido'),
    ]

    id = models.AutoField(primary_key=True)
    espacio = models.ForeignKey(EspacioFisico, on_delete=models.CASCADE, related_name='prestamos')
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name='prestamos_solicitados')
    administrador = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name='prestamos_admin')
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    motivo = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Pendiente')

    class Meta:
        constraints = [
            CheckConstraint(
                check=Q(hora_fin__gt=F('hora_inicio')),
                name='chk_prestamo_horas',
            ),
        ]
        indexes = [
            Index(fields=['espacio', 'fecha'], name='idx_prestamo_espacio_fecha'),
        ]


    def __str__(self):
        return f"{self.espacio} - {self.fecha}"
