from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
import datetime

def crud(request):
    return render(request, 'CRUD.html')

@csrf_exempt
def create_rol(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nombre = data.get('nombre')
            descripcion = data.get('descripcion')
            if not nombre or not descripcion:
                return JsonResponse({"error": "El nombre y la descripción son requeridos"}, status=400)
            nuevo_rol = Rol(nombre=nombre, descripcion=descripcion)
            nuevo_rol.save()
            return JsonResponse({"message": "Rol creado", "id": nuevo_rol.id}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "El cuerpo de la solicitud no es un JSON válido."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
        
@csrf_exempt
def update_rol(request):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            id = data.get('id')
            nombre = data.get('nombre')
            descripcion = data.get('descripcion')
            if not id or not nombre or not descripcion:
                return JsonResponse({"error": "ID, nombre y descripción son requeridos"}, status=400)
            rol_existente = Rol.objects.get(id=id)
            rol_existente.nombre = nombre
            rol_existente.descripcion = descripcion
            rol_existente.save()
            return JsonResponse({"message": "Rol actualizado", "id": rol_existente.id}, status=200)
        
        except Rol.DoesNotExist:
            return JsonResponse({"error": "El rol con el ID proporcionado no existe."}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "El cuerpo de la solicitud no es un JSON válido."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
def delete_rol(request):
    if request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            id = data.get('id')
            if not id:
                return JsonResponse({"error": "El ID es requerido"}, status=400)
            rol_existente = Rol.objects.get(id=id)
            rol_existente.delete()
            return JsonResponse({"message": "Rol eliminado"}, status=200)
        except Rol.DoesNotExist:
            return JsonResponse({"error": "El rol con el ID proporcionado no existe."}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "El cuerpo de la solicitud no es un JSON válido."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
def get_rol(request, id=None):
    if id is None:
        return JsonResponse({"error": "El ID es requerido en la URL"}, status=400)
    try:
        rol_existente = Rol.objects.get(id=id)
        return JsonResponse({"id": rol_existente.id, "nombre": rol_existente.nombre, "descripcion": rol_existente.descripcion}, status=200)
    except Rol.DoesNotExist:
        return JsonResponse({"error": "El rol con el ID proporcionado no existe."}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
def list_roles(request):
    if request.method == 'GET':
        roles = Rol.objects.all()
        roles_list = [{"id": rol.id, "nombre": rol.nombre, "descripcion": rol.descripcion} for rol in roles]
        return JsonResponse({"roles": roles_list}, status=200)

# ---------- Sede CRUD ----------
@csrf_exempt
def create_sede(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nombre = data.get('nombre')
            direccion = data.get('direccion')
            ciudad = data.get('ciudad')
            activa = data.get('activa', True)
            if not nombre:
                return JsonResponse({"error": "El nombre es requerido"}, status=400)
            s = Sede(nombre=nombre, direccion=direccion, ciudad=ciudad, activa=bool(activa))
            s.save()
            return JsonResponse({"message": "Sede creada", "id": s.id}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
def update_sede(request):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            id = data.get('id')
            if not id:
                return JsonResponse({"error": "ID es requerido"}, status=400)
            sede = Sede.objects.get(id=id)
            sede.nombre = data.get('nombre', sede.nombre)
            sede.direccion = data.get('direccion', sede.direccion)
            sede.ciudad = data.get('ciudad', sede.ciudad)
            if 'activa' in data:
                sede.activa = bool(data.get('activa'))
            sede.save()
            return JsonResponse({"message": "Sede actualizada", "id": sede.id}, status=200)
        except Sede.DoesNotExist:
            return JsonResponse({"error": "Sede no encontrada."}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
def delete_sede(request):
    if request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            id = data.get('id')
            if not id:
                return JsonResponse({"error": "ID es requerido"}, status=400)
            sede = Sede.objects.get(id=id)
            sede.delete()
            return JsonResponse({"message": "Sede eliminada"}, status=200)
        except Sede.DoesNotExist:
            return JsonResponse({"error": "Sede no encontrada."}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
def get_sede(request, id=None):
    if id is None:
        return JsonResponse({"error": "El ID es requerido en la URL"}, status=400)
    try:
        sede = Sede.objects.get(id=id)
        return JsonResponse({"id": sede.id, "nombre": sede.nombre, "direccion": sede.direccion, "ciudad": sede.ciudad, "activa": sede.activa}, status=200)
    except Sede.DoesNotExist:
        return JsonResponse({"error": "Sede no encontrada."}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
def list_sedes(request):
    if request.method == 'GET':
        sedes = Sede.objects.all()
        lst = [{"id": s.id, "nombre": s.nombre, "direccion": s.direccion, "ciudad": s.ciudad, "activa": s.activa} for s in sedes]
        return JsonResponse({"sedes": lst}, status=200)


# ---------- Facultad CRUD ----------
@csrf_exempt
def create_facultad(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nombre = data.get('nombre')
            activa = data.get('activa', True)
            if not nombre:
                return JsonResponse({"error": "El nombre es requerido"}, status=400)
            f = Facultad(nombre=nombre, activa=bool(activa))
            f.save()
            return JsonResponse({"message": "Facultad creada", "id": f.id}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
def update_facultad(request):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            id = data.get('id')
            if not id:
                return JsonResponse({"error": "ID es requerido"}, status=400)
            f = Facultad.objects.get(id=id)
            f.nombre = data.get('nombre', f.nombre)
            if 'activa' in data:
                f.activa = bool(data.get('activa'))
            f.save()
            return JsonResponse({"message": "Facultad actualizada", "id": f.id}, status=200)
        except Facultad.DoesNotExist:
            return JsonResponse({"error": "Facultad no encontrada."}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
def delete_facultad(request):
    if request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            id = data.get('id')
            if not id:
                return JsonResponse({"error": "ID es requerido"}, status=400)
            f = Facultad.objects.get(id=id)
            f.delete()
            return JsonResponse({"message": "Facultad eliminada"}, status=200)
        except Facultad.DoesNotExist:
            return JsonResponse({"error": "Facultad no encontrada."}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
def get_facultad(request, id=None):
    if id is None:
        return JsonResponse({"error": "El ID es requerido en la URL"}, status=400)
    try:
        f = Facultad.objects.get(id=id)
        return JsonResponse({"id": f.id, "nombre": f.nombre, "activa": f.activa}, status=200)
    except Facultad.DoesNotExist:
        return JsonResponse({"error": "Facultad no encontrada."}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
def list_facultades(request):
    if request.method == 'GET':
        items = Facultad.objects.all()
        lst = [{"id": i.id, "nombre": i.nombre, "activa": i.activa} for i in items]
        return JsonResponse({"facultades": lst}, status=200)


# ---------- Programa CRUD ----------
@csrf_exempt
def create_programa(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nombre = data.get('nombre')
            facultad_id = data.get('facultad_id')
            activo = data.get('activo', True)
            if not nombre or not facultad_id:
                return JsonResponse({"error": "nombre y facultad_id son requeridos"}, status=400)
            facultad = Facultad.objects.get(id=facultad_id)
            p = Programa(nombre=nombre, facultad=facultad, activo=bool(activo))
            p.save()
            return JsonResponse({"message": "Programa creado", "id": p.id}, status=201)
        except Facultad.DoesNotExist:
            return JsonResponse({"error": "Facultad no encontrada."}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
def update_programa(request):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            id = data.get('id')
            if not id:
                return JsonResponse({"error": "ID es requerido"}, status=400)
            p = Programa.objects.get(id=id)
            if 'nombre' in data:
                p.nombre = data.get('nombre')
            if 'facultad_id' in data:
                p.facultad = Facultad.objects.get(id=data.get('facultad_id'))
            if 'activo' in data:
                p.activo = bool(data.get('activo'))
            p.save()
            return JsonResponse({"message": "Programa actualizado", "id": p.id}, status=200)
        except Programa.DoesNotExist:
            return JsonResponse({"error": "Programa no encontrado."}, status=404)
        except Facultad.DoesNotExist:
            return JsonResponse({"error": "Facultad no encontrada."}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
def delete_programa(request):
    if request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            id = data.get('id')
            if not id:
                return JsonResponse({"error": "ID es requerido"}, status=400)
            p = Programa.objects.get(id=id)
            p.delete()
            return JsonResponse({"message": "Programa eliminado"}, status=200)
        except Programa.DoesNotExist:
            return JsonResponse({"error": "Programa no encontrado."}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
def get_programa(request, id=None):
    if id is None:
        return JsonResponse({"error": "El ID es requerido en la URL"}, status=400)
    try:
        p = Programa.objects.get(id=id)
        return JsonResponse({"id": p.id, "nombre": p.nombre, "facultad": p.facultad.id, "activo": p.activo}, status=200)
    except Programa.DoesNotExist:
        return JsonResponse({"error": "Programa no encontrado."}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
def list_programas(request):
    if request.method == 'GET':
        items = Programa.objects.all()
        lst = [{"id": i.id, "nombre": i.nombre, "facultad_id": i.facultad.id, "activo": i.activo} for i in items]
        return JsonResponse({"programas": lst}, status=200)


# ---------- PeriodoAcademico CRUD ----------
@csrf_exempt
def create_periodo(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nombre = data.get('nombre')
            fecha_inicio = data.get('fecha_inicio')
            fecha_fin = data.get('fecha_fin')
            activo = data.get('activo', True)
            if not nombre or not fecha_inicio or not fecha_fin:
                return JsonResponse({"error": "nombre, fecha_inicio y fecha_fin son requeridos"}, status=400)
            fi = datetime.date.fromisoformat(fecha_inicio)
            ff = datetime.date.fromisoformat(fecha_fin)
            p = PeriodoAcademico(nombre=nombre, fecha_inicio=fi, fecha_fin=ff, activo=bool(activo))
            p.save()
            return JsonResponse({"message": "Periodo creado", "id": p.id}, status=201)
        except ValueError:
            return JsonResponse({"error": "Formato de fecha inválido. Use YYYY-MM-DD."}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
def update_periodo(request):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            id = data.get('id')
            if not id:
                return JsonResponse({"error": "ID es requerido"}, status=400)
            p = PeriodoAcademico.objects.get(id=id)
            if 'nombre' in data:
                p.nombre = data.get('nombre')
            if 'fecha_inicio' in data:
                p.fecha_inicio = datetime.date.fromisoformat(data.get('fecha_inicio'))
            if 'fecha_fin' in data:
                p.fecha_fin = datetime.date.fromisoformat(data.get('fecha_fin'))
            if 'activo' in data:
                p.activo = bool(data.get('activo'))
            p.save()
            return JsonResponse({"message": "Periodo actualizado", "id": p.id}, status=200)
        except PeriodoAcademico.DoesNotExist:
            return JsonResponse({"error": "Periodo no encontrado."}, status=404)
        except ValueError:
            return JsonResponse({"error": "Formato de fecha inválido. Use YYYY-MM-DD."}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
def delete_periodo(request):
    if request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            id = data.get('id')
            if not id:
                return JsonResponse({"error": "ID es requerido"}, status=400)
            p = PeriodoAcademico.objects.get(id=id)
            p.delete()
            return JsonResponse({"message": "Periodo eliminado"}, status=200)
        except PeriodoAcademico.DoesNotExist:
            return JsonResponse({"error": "Periodo no encontrado."}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
def get_periodo(request, id=None):
    if id is None:
        return JsonResponse({"error": "El ID es requerido en la URL"}, status=400)
    try:
        p = PeriodoAcademico.objects.get(id=id)
        return JsonResponse({"id": p.id, "nombre": p.nombre, "fecha_inicio": str(p.fecha_inicio), "fecha_fin": str(p.fecha_fin), "activo": p.activo}, status=200)
    except PeriodoAcademico.DoesNotExist:
        return JsonResponse({"error": "Periodo no encontrado."}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
def list_periodos(request):
    if request.method == 'GET':
        items = PeriodoAcademico.objects.all()
        lst = [{"id": i.id, "nombre": i.nombre, "fecha_inicio": str(i.fecha_inicio), "fecha_fin": str(i.fecha_fin), "activo": i.activo} for i in items]
        return JsonResponse({"periodos": lst}, status=200)


# ---------- Grupo CRUD ----------
@csrf_exempt
def create_grupo(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nombre = data.get('nombre')
            programa_id = data.get('programa_id')
            periodo_id = data.get('periodo_id')
            semestre = data.get('semestre')
            activo = data.get('activo', True)
            if not nombre or not programa_id or not periodo_id or semestre is None:
                return JsonResponse({"error": "nombre, programa_id, periodo_id y semestre son requeridos"}, status=400)
            programa = Programa.objects.get(id=programa_id)
            periodo = PeriodoAcademico.objects.get(id=periodo_id)
            g = Grupo(programa=programa, periodo=periodo, nombre=nombre, semestre=int(semestre), activo=bool(activo))
            g.save()
            return JsonResponse({"message": "Grupo creado", "id": g.id}, status=201)
        except (Programa.DoesNotExist, PeriodoAcademico.DoesNotExist):
            return JsonResponse({"error": "Programa o Periodo no encontrado."}, status=404)
        except ValueError:
            return JsonResponse({"error": "Semestre debe ser un entero"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
def update_grupo(request):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            id = data.get('id')
            if not id:
                return JsonResponse({"error": "ID es requerido"}, status=400)
            g = Grupo.objects.get(id=id)
            if 'nombre' in data:
                g.nombre = data.get('nombre')
            if 'programa_id' in data:
                g.programa = Programa.objects.get(id=data.get('programa_id'))
            if 'periodo_id' in data:
                g.periodo = PeriodoAcademico.objects.get(id=data.get('periodo_id'))
            if 'semestre' in data:
                g.semestre = int(data.get('semestre'))
            if 'activo' in data:
                g.activo = bool(data.get('activo'))
            g.save()
            return JsonResponse({"message": "Grupo actualizado", "id": g.id}, status=200)
        except Grupo.DoesNotExist:
            return JsonResponse({"error": "Grupo no encontrado."}, status=404)
        except (Programa.DoesNotExist, PeriodoAcademico.DoesNotExist):
            return JsonResponse({"error": "Programa o Periodo no encontrado."}, status=404)
        except ValueError:
            return JsonResponse({"error": "Semestre debe ser un entero"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
def delete_grupo(request):
    if request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            id = data.get('id')
            if not id:
                return JsonResponse({"error": "ID es requerido"}, status=400)
            g = Grupo.objects.get(id=id)
            g.delete()
            return JsonResponse({"message": "Grupo eliminado"}, status=200)
        except Grupo.DoesNotExist:
            return JsonResponse({"error": "Grupo no encontrado."}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
def get_grupo(request, id=None):
    if id is None:
        return JsonResponse({"error": "El ID es requerido en la URL"}, status=400)
    try:
        g = Grupo.objects.get(id=id)
        return JsonResponse({"id": g.id, "nombre": g.nombre, "programa_id": g.programa.id, "periodo_id": g.periodo.id, "semestre": g.semestre, "activo": g.activo}, status=200)
    except Grupo.DoesNotExist:
        return JsonResponse({"error": "Grupo no encontrado."}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
def list_grupos(request):
    if request.method == 'GET':
        items = Grupo.objects.all()
        lst = [{"id": i.id, "nombre": i.nombre, "programa_id": i.programa.id, "periodo_id": i.periodo.id, "semestre": i.semestre, "activo": i.activo} for i in items]
        return JsonResponse({"grupos": lst}, status=200)


# ---------- Asignatura CRUD ----------
@csrf_exempt
def create_asignatura(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nombre = data.get('nombre')
            codigo = data.get('codigo')
            creditos = data.get('creditos')
            if not nombre or not codigo or creditos is None:
                return JsonResponse({"error": "nombre, codigo y creditos son requeridos"}, status=400)
            a = Asignatura(nombre=nombre, codigo=codigo, creditos=int(creditos))
            a.save()
            return JsonResponse({"message": "Asignatura creada", "id": a.id}, status=201)
        except ValueError:
            return JsonResponse({"error": "creditos debe ser un entero"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
def update_asignatura(request):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            id = data.get('id')
            if not id:
                return JsonResponse({"error": "ID es requerido"}, status=400)
            a = Asignatura.objects.get(id=id)
            if 'nombre' in data:
                a.nombre = data.get('nombre')
            if 'codigo' in data:
                a.codigo = data.get('codigo')
            if 'creditos' in data:
                a.creditos = int(data.get('creditos'))
            a.save()
            return JsonResponse({"message": "Asignatura actualizada", "id": a.id}, status=200)
        except Asignatura.DoesNotExist:
            return JsonResponse({"error": "Asignatura no encontrada."}, status=404)
        except ValueError:
            return JsonResponse({"error": "creditos debe ser un entero"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
def delete_asignatura(request):
    if request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            id = data.get('id')
            if not id:
                return JsonResponse({"error": "ID es requerido"}, status=400)
            a = Asignatura.objects.get(id=id)
            a.delete()
            return JsonResponse({"message": "Asignatura eliminada"}, status=200)
        except Asignatura.DoesNotExist:
            return JsonResponse({"error": "Asignatura no encontrada."}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
def get_asignatura(request, id=None):
    if id is None:
        return JsonResponse({"error": "El ID es requerido en la URL"}, status=400)
    try:
        a = Asignatura.objects.get(id=id)
        return JsonResponse({"id": a.id, "nombre": a.nombre, "codigo": a.codigo, "creditos": a.creditos}, status=200)
    except Asignatura.DoesNotExist:
        return JsonResponse({"error": "Asignatura no encontrada."}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
def list_asignaturas(request):
    if request.method == 'GET':
        items = Asignatura.objects.all()
        lst = [{"id": i.id, "nombre": i.nombre, "codigo": i.codigo, "creditos": i.creditos} for i in items]
        return JsonResponse({"asignaturas": lst}, status=200)


# ---------- EspacioFisico CRUD ----------
@csrf_exempt
def create_espacio(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            sede_id = data.get('sede_id')
            tipo = data.get('tipo')
            capacidad = data.get('capacidad')
            ubicacion = data.get('ubicacion')
            recursos = data.get('recursos')
            disponible = data.get('disponible', True)
            if not sede_id or not tipo or capacidad is None:
                return JsonResponse({"error": "sede_id, tipo y capacidad son requeridos"}, status=400)
            sede = Sede.objects.get(id=sede_id)
            e = EspacioFisico(sede=sede, tipo=tipo, capacidad=int(capacidad), ubicacion=ubicacion, recursos=recursos, disponible=bool(disponible))
            e.save()
            return JsonResponse({"message": "Espacio creado", "id": e.id}, status=201)
        except Sede.DoesNotExist:
            return JsonResponse({"error": "Sede no encontrada."}, status=404)
        except ValueError:
            return JsonResponse({"error": "capacidad debe ser un entero"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
def update_espacio(request):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            id = data.get('id')
            if not id:
                return JsonResponse({"error": "ID es requerido"}, status=400)
            e = EspacioFisico.objects.get(id=id)
            if 'sede_id' in data:
                e.sede = Sede.objects.get(id=data.get('sede_id'))
            if 'tipo' in data:
                e.tipo = data.get('tipo')
            if 'capacidad' in data:
                e.capacidad = int(data.get('capacidad'))
            if 'ubicacion' in data:
                e.ubicacion = data.get('ubicacion')
            if 'recursos' in data:
                e.recursos = data.get('recursos')
            if 'disponible' in data:
                e.disponible = bool(data.get('disponible'))
            e.save()
            return JsonResponse({"message": "Espacio actualizado", "id": e.id}, status=200)
        except EspacioFisico.DoesNotExist:
            return JsonResponse({"error": "Espacio no encontrado."}, status=404)
        except Sede.DoesNotExist:
            return JsonResponse({"error": "Sede no encontrada."}, status=404)
        except ValueError:
            return JsonResponse({"error": "capacidad debe ser un entero"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
def delete_espacio(request):
    if request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            id = data.get('id')
            if not id:
                return JsonResponse({"error": "ID es requerido"}, status=400)
            e = EspacioFisico.objects.get(id=id)
            e.delete()
            return JsonResponse({"message": "Espacio eliminado"}, status=200)
        except EspacioFisico.DoesNotExist:
            return JsonResponse({"error": "Espacio no encontrado."}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
def get_espacio(request, id=None):
    if id is None:
        return JsonResponse({"error": "El ID es requerido en la URL"}, status=400)
    try:
        e = EspacioFisico.objects.get(id=id)
        return JsonResponse({"id": e.id, "sede_id": e.sede.id, "tipo": e.tipo, "capacidad": e.capacidad, "ubicacion": e.ubicacion, "recursos": e.recursos, "disponible": e.disponible}, status=200)
    except EspacioFisico.DoesNotExist:
        return JsonResponse({"error": "Espacio no encontrado."}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
def list_espacios(request):
    if request.method == 'GET':
        items = EspacioFisico.objects.all()
        lst = [{"id": i.id, "sede_id": i.sede.id, "tipo": i.tipo, "capacidad": i.capacidad, "ubicacion": i.ubicacion, "recursos": i.recursos, "disponible": i.disponible} for i in items]
        return JsonResponse({"espacios": lst}, status=200)


# ---------- Recurso CRUD ----------
@csrf_exempt
def create_recurso(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nombre = data.get('nombre')
            descripcion = data.get('descripcion')
            r = Recurso(nombre=nombre, descripcion=descripcion)
            r.save()
            return JsonResponse({"message": "Recurso creado", "id": r.id}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
def update_recurso(request):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            id = data.get('id')
            if not id:
                return JsonResponse({"error": "ID es requerido"}, status=400)
            r = Recurso.objects.get(id=id)
            if 'nombre' in data:
                r.nombre = data.get('nombre')
            if 'descripcion' in data:
                r.descripcion = data.get('descripcion')
            r.save()
            return JsonResponse({"message": "Recurso actualizado", "id": r.id}, status=200)
        except Recurso.DoesNotExist:
            return JsonResponse({"error": "Recurso no encontrado."}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
def delete_recurso(request):
    if request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            id = data.get('id')
            if not id:
                return JsonResponse({"error": "ID es requerido"}, status=400)
            r = Recurso.objects.get(id=id)
            r.delete()
            return JsonResponse({"message": "Recurso eliminado"}, status=200)
        except Recurso.DoesNotExist:
            return JsonResponse({"error": "Recurso no encontrado."}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
def get_recurso(request, id=None):
    if id is None:
        return JsonResponse({"error": "El ID es requerido en la URL"}, status=400)
    try:
        r = Recurso.objects.get(id=id)
        return JsonResponse({"id": r.id, "nombre": r.nombre, "descripcion": r.descripcion}, status=200)
    except Recurso.DoesNotExist:
        return JsonResponse({"error": "Recurso no encontrado."}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
def list_recursos(request):
    if request.method == 'GET':
        items = Recurso.objects.all()
        lst = [{"id": i.id, "nombre": i.nombre, "descripcion": i.descripcion} for i in items]
        return JsonResponse({"recursos": lst}, status=200)


# ---------- EspacioRecurso CRUD ----------
@csrf_exempt
def create_espacio_recurso(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            espacio_id = data.get('espacio_id')
            recurso_id = data.get('recurso_id')
            disponible = data.get('disponible', True)
            if not espacio_id or not recurso_id:
                return JsonResponse({"error": "espacio_id y recurso_id son requeridos"}, status=400)
            espacio = EspacioFisico.objects.get(id=espacio_id)
            recurso = Recurso.objects.get(id=recurso_id)
            er = EspacioRecurso(espacio=espacio, recurso=recurso, disponible=bool(disponible))
            er.save()
            return JsonResponse({"message": "EspacioRecurso creado", "espacio_id": espacio.id, "recurso_id": recurso.id}, status=201)
        except EspacioFisico.DoesNotExist:
            return JsonResponse({"error": "Espacio no encontrado."}, status=404)
        except Recurso.DoesNotExist:
            return JsonResponse({"error": "Recurso no encontrado."}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
def update_espacio_recurso(request):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            espacio_id = data.get('espacio_id')
            recurso_id = data.get('recurso_id')
            if not espacio_id or not recurso_id:
                return JsonResponse({"error": "espacio_id y recurso_id son requeridos"}, status=400)
            er = EspacioRecurso.objects.get(espacio_id=espacio_id, recurso_id=recurso_id)
            if 'disponible' in data:
                er.disponible = bool(data.get('disponible'))
            er.save()
            return JsonResponse({"message": "EspacioRecurso actualizado"}, status=200)
        except EspacioRecurso.DoesNotExist:
            return JsonResponse({"error": "Relación Espacio-Recurso no encontrada."}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
def delete_espacio_recurso(request):
    if request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            espacio_id = data.get('espacio_id')
            recurso_id = data.get('recurso_id')
            if not espacio_id or not recurso_id:
                return JsonResponse({"error": "espacio_id y recurso_id son requeridos"}, status=400)
            er = EspacioRecurso.objects.get(espacio_id=espacio_id, recurso_id=recurso_id)
            er.delete()
            return JsonResponse({"message": "EspacioRecurso eliminado"}, status=200)
        except EspacioRecurso.DoesNotExist:
            return JsonResponse({"error": "Relación Espacio-Recurso no encontrada."}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
def get_espacio_recurso(request, espacio_id=None, recurso_id=None):
    if espacio_id is None or recurso_id is None:
        return JsonResponse({"error": "espacio_id y recurso_id son requeridos en la URL"}, status=400)
    try:
        er = EspacioRecurso.objects.get(espacio_id=espacio_id, recurso_id=recurso_id)
        return JsonResponse({"espacio_id": er.espacio.id, "recurso_id": er.recurso.id, "disponible": er.disponible}, status=200)
    except EspacioRecurso.DoesNotExist:
        return JsonResponse({"error": "Relación Espacio-Recurso no encontrada."}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
def list_espacio_recursos(request):
    if request.method == 'GET':
        items = EspacioRecurso.objects.all()
        lst = [{"espacio_id": i.espacio.id, "recurso_id": i.recurso.id, "disponible": i.disponible} for i in items]
        return JsonResponse({"espacio_recursos": lst}, status=200)

# ---------- Usuario CRUD ----------
@csrf_exempt
def create_usuario(request):
    if request.method != 'POST':
        return JsonResponse({"error": "Método no permitido"}, status=405)
    try:
        data = json.loads(request.body)
        nombre = data.get('nombre')
        correo = data.get('correo')
        contrasena = data.get('contrasena') or data.get('contrasena_hash')
        rol_id = data.get('rol_id')
        activo = data.get('activo', True)
        if not nombre or not correo or not contrasena:
            return JsonResponse({"error": "nombre, correo y contrasena son requeridos"}, status=400)
        rol = None
        if rol_id:
            rol = Rol.objects.get(id=rol_id)
        u = Usuario(nombre=nombre, correo=correo, contrasena_hash=contrasena, rol=rol, activo=bool(activo))
        u.save()
        return JsonResponse({"message": "Usuario creado", "id": u.id}, status=201)
    except Rol.DoesNotExist:
        return JsonResponse({"error": "Rol no encontrado."}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({"error": "JSON inválido."}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
def update_usuario(request):
    if request.method != 'PUT':
        return JsonResponse({"error": "Método no permitido"}, status=405)
    try:
        data = json.loads(request.body)
        id = data.get('id')
        if not id:
            return JsonResponse({"error": "ID es requerido"}, status=400)
        u = Usuario.objects.get(id=id)
        if 'nombre' in data:
            u.nombre = data.get('nombre')
        if 'correo' in data:
            u.correo = data.get('correo')
        if 'contrasena' in data or 'contrasena_hash' in data:
            u.contrasena_hash = data.get('contrasena') or data.get('contrasena_hash')
        if 'rol_id' in data:
            u.rol = Rol.objects.get(id=data.get('rol_id')) if data.get('rol_id') else None
        if 'activo' in data:
            u.activo = bool(data.get('activo'))
        u.save()
        return JsonResponse({"message": "Usuario actualizado", "id": u.id}, status=200)
    except Usuario.DoesNotExist:
        return JsonResponse({"error": "Usuario no encontrado."}, status=404)
    except Rol.DoesNotExist:
        return JsonResponse({"error": "Rol no encontrado."}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({"error": "JSON inválido."}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
def delete_usuario(request):
    if request.method != 'DELETE':
        return JsonResponse({"error": "Método no permitido"}, status=405)
    try:
        data = json.loads(request.body)
        id = data.get('id')
        if not id:
            return JsonResponse({"error": "ID es requerido"}, status=400)
        u = Usuario.objects.get(id=id)
        u.delete()
        return JsonResponse({"message": "Usuario eliminado"}, status=200)
    except Usuario.DoesNotExist:
        return JsonResponse({"error": "Usuario no encontrado."}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({"error": "JSON inválido."}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
def get_usuario(request, id=None):
    if id is None:
        return JsonResponse({"error": "El ID es requerido en la URL"}, status=400)
    try:
        u = Usuario.objects.get(id=id)
        return JsonResponse({"id": u.id, "nombre": u.nombre, "correo": u.correo, "rol_id": (u.rol.id if u.rol else None), "activo": u.activo}, status=200)
    except Usuario.DoesNotExist:
        return JsonResponse({"error": "Usuario no encontrado."}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
def list_usuarios(request):
    if request.method == 'GET':
        items = Usuario.objects.all()
        lst = [{"id": i.id, "nombre": i.nombre, "correo": i.correo, "rol_id": (i.rol.id if i.rol else None), "activo": i.activo} for i in items]
        return JsonResponse({"usuarios": lst}, status=200)

# ---------- Horario CRUD ----------
@csrf_exempt
def create_horario(request):
    if request.method != 'POST':
        return JsonResponse({"error": "Método no permitido"}, status=405)
    try:
        data = json.loads(request.body)
        grupo_id = data.get('grupo_id')
        asignatura_id = data.get('asignatura_id')
        espacio_id = data.get('espacio_id')
        dia_semana = data.get('dia_semana')
        hora_inicio = data.get('hora_inicio')
        hora_fin = data.get('hora_fin')
        docente_id = data.get('docente_id')
        cantidad = data.get('cantidad_estudiantes')
        if not grupo_id or not asignatura_id or not espacio_id or not dia_semana or not hora_inicio or not hora_fin:
            return JsonResponse({"error": "Faltan campos requeridos"}, status=400)
        grupo = Grupo.objects.get(id=grupo_id)
        asignatura = Asignatura.objects.get(id=asignatura_id)
        espacio = EspacioFisico.objects.get(id=espacio_id)
        docente = Usuario.objects.get(id=docente_id) if docente_id else None
        hi = datetime.time.fromisoformat(hora_inicio)
        hf = datetime.time.fromisoformat(hora_fin)
        h = Horario(grupo=grupo, asignatura=asignatura, docente=docente, espacio=espacio, dia_semana=dia_semana, hora_inicio=hi, hora_fin=hf, cantidad_estudiantes=(int(cantidad) if cantidad is not None else None))
        h.save()
        return JsonResponse({"message": "Horario creado", "id": h.id}, status=201)
    except (Grupo.DoesNotExist, Asignatura.DoesNotExist, EspacioFisico.DoesNotExist, Usuario.DoesNotExist):
        return JsonResponse({"error": "Relacionada no encontrada."}, status=404)
    except ValueError:
        return JsonResponse({"error": "Formato de hora inválido o valor numérico incorrecto."}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({"error": "JSON inválido."}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
def update_horario(request):
    if request.method != 'PUT':
        return JsonResponse({"error": "Método no permitido"}, status=405)
    try:
        data = json.loads(request.body)
        id = data.get('id')
        if not id:
            return JsonResponse({"error": "ID es requerido"}, status=400)
        h = Horario.objects.get(id=id)
        if 'grupo_id' in data:
            h.grupo = Grupo.objects.get(id=data.get('grupo_id'))
        if 'asignatura_id' in data:
            h.asignatura = Asignatura.objects.get(id=data.get('asignatura_id'))
        if 'docente_id' in data:
            h.docente = Usuario.objects.get(id=data.get('docente_id')) if data.get('docente_id') else None
        if 'espacio_id' in data:
            h.espacio = EspacioFisico.objects.get(id=data.get('espacio_id'))
        if 'dia_semana' in data:
            h.dia_semana = data.get('dia_semana')
        if 'hora_inicio' in data:
            h.hora_inicio = datetime.time.fromisoformat(data.get('hora_inicio'))
        if 'hora_fin' in data:
            h.hora_fin = datetime.time.fromisoformat(data.get('hora_fin'))
        if 'cantidad_estudiantes' in data:
            h.cantidad_estudiantes = int(data.get('cantidad_estudiantes')) if data.get('cantidad_estudiantes') is not None else None
        h.save()
        return JsonResponse({"message": "Horario actualizado", "id": h.id}, status=200)
    except Horario.DoesNotExist:
        return JsonResponse({"error": "Horario no encontrado."}, status=404)
    except (Grupo.DoesNotExist, Asignatura.DoesNotExist, EspacioFisico.DoesNotExist, Usuario.DoesNotExist):
        return JsonResponse({"error": "Relacionada no encontrada."}, status=404)
    except ValueError:
        return JsonResponse({"error": "Formato de hora inválido o valor numérico incorrecto."}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({"error": "JSON inválido."}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
def delete_horario(request):
    if request.method != 'DELETE':
        return JsonResponse({"error": "Método no permitido"}, status=405)
    try:
        data = json.loads(request.body)
        id = data.get('id')
        if not id:
            return JsonResponse({"error": "ID es requerido"}, status=400)
        h = Horario.objects.get(id=id)
        h.delete()
        return JsonResponse({"message": "Horario eliminado"}, status=200)
    except Horario.DoesNotExist:
        return JsonResponse({"error": "Horario no encontrado."}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({"error": "JSON inválido."}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
 
@csrf_exempt
def get_horario(request, id=None):
    if id is None:
        return JsonResponse({"error": "El ID es requerido en la URL"}, status=400)
    try:
        h = Horario.objects.get(id=id)
        return JsonResponse({
            "id": h.id,
            "grupo_id": h.grupo.id,
            "asignatura_id": h.asignatura.id,
            "docente_id": (h.docente.id if h.docente else None),
            "espacio_id": h.espacio.id,
            "dia_semana": h.dia_semana,
            "hora_inicio": str(h.hora_inicio),
            "hora_fin": str(h.hora_fin),
            "cantidad_estudiantes": h.cantidad_estudiantes
        }, status=200)
    except Horario.DoesNotExist:
        return JsonResponse({"error": "Horario no encontrado."}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def list_horarios(request):
    if request.method == 'GET':
        items = Horario.objects.all()
        lst = [{
            "id": i.id,
            "grupo_id": i.grupo.id,
            "asignatura_id": i.asignatura.id,
            "docente_id": (i.docente.id if i.docente else None),
            "espacio_id": i.espacio.id,
            "dia_semana": i.dia_semana,
            "hora_inicio": str(i.hora_inicio),
            "hora_fin": str(i.hora_fin),
            "cantidad_estudiantes": i.cantidad_estudiantes
        } for i in items]
        return JsonResponse({"horarios": lst}, status=200)

# ---------- Horario_Fusionado CRUD ----------
@csrf_exempt
def create_horario_fusionado(request):
    if request.method != 'POST':
        return JsonResponse({"error": "Método no permitido"}, status=405)
    try:
        data = json.loads(request.body)
        grupo1_id = data.get('grupo1_id')
        grupo2_id = data.get('grupo2_id')
        grupo3_id = data.get('grupo3_id')
        asignatura_id = data.get('asignatura_id')
        espacio_id = data.get('espacio_id')
        dia_semana = data.get('dia_semana')
        hora_inicio = data.get('hora_inicio')
        hora_fin = data.get('hora_fin')
        docente_id = data.get('docente_id')
        cantidad = data.get('cantidad_estudiantes')
        comentario = data.get('comentario')
        if not grupo1_id or not grupo2_id or not asignatura_id or not espacio_id or not dia_semana or not hora_inicio or not hora_fin:
            return JsonResponse({"error": "Faltan campos requeridos"}, status=400)
        grupo1 = Grupo.objects.get(id=grupo1_id)
        grupo2 = Grupo.objects.get(id=grupo2_id)
        grupo3 = Grupo.objects.get(id=grupo3_id) if grupo3_id else None
        asignatura = Asignatura.objects.get(id=asignatura_id)
        espacio = EspacioFisico.objects.get(id=espacio_id)
        docente = Usuario.objects.get(id=docente_id) if docente_id else None
        hi = datetime.time.fromisoformat(hora_inicio)
        hf = datetime.time.fromisoformat(hora_fin)
        hfus = HorarioFusionado(grupo1=grupo1, grupo2=grupo2, grupo3=grupo3, asignatura=asignatura, docente=docente, espacio=espacio, dia_semana=dia_semana, hora_inicio=hi, hora_fin=hf, cantidad_estudiantes=(int(cantidad) if cantidad is not None else None), comentario=comentario)
        hfus.save()
        return JsonResponse({"message": "Horario fusionado creado", "id": hfus.id}, status=201)
    except (Grupo.DoesNotExist, Asignatura.DoesNotExist, EspacioFisico.DoesNotExist, Usuario.DoesNotExist):
        return JsonResponse({"error": "Relacionada no encontrada."}, status=404)
    except ValueError:
        return JsonResponse({"error": "Formato de hora inválido o valor numérico incorrecto."}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({"error": "JSON inválido."}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
def update_horario_fusionado(request):
    if request.method != 'PUT':
        return JsonResponse({"error": "Método no permitido"}, status=405)
    try:
        data = json.loads(request.body)
        id = data.get('id')
        if not id:
            return JsonResponse({"error": "ID es requerido"}, status=400)
        h = HorarioFusionado.objects.get(id=id)
        if 'grupo1_id' in data:
            h.grupo1 = Grupo.objects.get(id=data.get('grupo1_id'))
        if 'grupo2_id' in data:
            h.grupo2 = Grupo.objects.get(id=data.get('grupo2_id'))
        if 'grupo3_id' in data:
            h.grupo3 = Grupo.objects.get(id=data.get('grupo3_id')) if data.get('grupo3_id') else None
        if 'asignatura_id' in data:
            h.asignatura = Asignatura.objects.get(id=data.get('asignatura_id'))
        if 'docente_id' in data:
            h.docente = Usuario.objects.get(id=data.get('docente_id')) if data.get('docente_id') else None
        if 'espacio_id' in data:
            h.espacio = EspacioFisico.objects.get(id=data.get('espacio_id'))
        if 'dia_semana' in data:
            h.dia_semana = data.get('dia_semana')
        if 'hora_inicio' in data:
            h.hora_inicio = datetime.time.fromisoformat(data.get('hora_inicio'))
        if 'hora_fin' in data:
            h.hora_fin = datetime.time.fromisoformat(data.get('hora_fin'))
        if 'cantidad_estudiantes' in data:
            h.cantidad_estudiantes = int(data.get('cantidad_estudiantes')) if data.get('cantidad_estudiantes') is not None else None
        if 'comentario' in data:
            h.comentario = data.get('comentario')
        h.save()
        return JsonResponse({"message": "Horario fusionado actualizado", "id": h.id}, status=200)
    except HorarioFusionado.DoesNotExist:
        return JsonResponse({"error": "Horario fusionado no encontrado."}, status=404)
    except (Grupo.DoesNotExist, Asignatura.DoesNotExist, EspacioFisico.DoesNotExist, Usuario.DoesNotExist):
        return JsonResponse({"error": "Relacionada no encontrada."}, status=404)
    except ValueError:
        return JsonResponse({"error": "Formato de hora inválido o valor numérico incorrecto."}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({"error": "JSON inválido."}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
def delete_horario_fusionado(request):
    if request.method != 'DELETE':
        return JsonResponse({"error": "Método no permitido"}, status=405)
    try:
        data = json.loads(request.body)
        id = data.get('id')
        if not id:
            return JsonResponse({"error": "ID es requerido"}, status=400)
        h = HorarioFusionado.objects.get(id=id)
        h.delete()
        return JsonResponse({"message": "Horario fusionado eliminado"}, status=200)
    except HorarioFusionado.DoesNotExist:
        return JsonResponse({"error": "Horario fusionado no encontrado."}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({"error": "JSON inválido."}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    
@csrf_exempt
def get_horario_fusionado(request, id=None):
    if id is None:
        return JsonResponse({"error": "El ID es requerido en la URL"}, status=400)
    try:
        h = HorarioFusionado.objects.get(id=id)
        return JsonResponse({
            "id": h.id,
            "grupo1_id": h.grupo1.id,
            "grupo2_id": h.grupo2.id,
            "grupo3_id": (h.grupo3.id if h.grupo3 else None),
            "asignatura_id": h.asignatura.id,
            "docente_id": (h.docente.id if h.docente else None),
            "espacio_id": h.espacio.id,
            "dia_semana": h.dia_semana,
            "hora_inicio": str(h.hora_inicio),
            "hora_fin": str(h.hora_fin),
            "cantidad_estudiantes": h.cantidad_estudiantes,
            "comentario": h.comentario
        }, status=200)
    except HorarioFusionado.DoesNotExist:
        return JsonResponse({"error": "Horario fusionado no encontrado."}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def list_horarios_fusionados(request):
    if request.method == 'GET':
        items = HorarioFusionado.objects.all()
        lst = [{
            "id": i.id,
            "grupo1_id": i.grupo1.id,
            "grupo2_id": i.grupo2.id,
            "grupo3_id": (i.grupo3.id if i.grupo3 else None),
            "asignatura_id": i.asignatura.id,
            "docente_id": (i.docente.id if i.docente else None),
            "espacio_id": i.espacio.id,
            "dia_semana": i.dia_semana,
            "hora_inicio": str(i.hora_inicio),
            "hora_fin": str(i.hora_fin),
            "cantidad_estudiantes": i.cantidad_estudiantes,
            "comentario": i.comentario
        } for i in items]
        return JsonResponse({"horarios_fusionados": lst}, status=200)


# ---------- Prestamo CRUD ----------
@csrf_exempt
def create_prestamo(request):
    if request.method != 'POST':
        return JsonResponse({"error": "Método no permitido"}, status=405)
    try:
        data = json.loads(request.body)
        espacio_id = data.get('espacio_id')
        usuario_id = data.get('usuario_id')
        administrador_id = data.get('administrador_id')
        fecha = data.get('fecha')
        hora_inicio = data.get('hora_inicio')
        hora_fin = data.get('hora_fin')
        motivo = data.get('motivo')
        estado = data.get('estado', 'Pendiente')
        if not espacio_id or not fecha or not hora_inicio or not hora_fin:
            return JsonResponse({"error": "espacio_id, fecha, hora_inicio y hora_fin son requeridos"}, status=400)
        espacio = EspacioFisico.objects.get(id=espacio_id)
        usuario = Usuario.objects.get(id=usuario_id) if usuario_id else None
        administrador = Usuario.objects.get(id=administrador_id) if administrador_id else None
        f = datetime.date.fromisoformat(fecha)
        hi = datetime.time.fromisoformat(hora_inicio)
        hf = datetime.time.fromisoformat(hora_fin)
        p = PrestamoEspacio(espacio=espacio, usuario=usuario, administrador=administrador, fecha=f, hora_inicio=hi, hora_fin=hf, motivo=motivo, estado=estado)
        p.save()
        return JsonResponse({"message": "Prestamo creado", "id": p.id}, status=201)
    except EspacioFisico.DoesNotExist:
        return JsonResponse({"error": "Espacio no encontrado."}, status=404)
    except Usuario.DoesNotExist:
        return JsonResponse({"error": "Usuario no encontrado."}, status=404)
    except ValueError:
        return JsonResponse({"error": "Formato de fecha/hora inválido."}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({"error": "JSON inválido."}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
def update_prestamo(request):
    if request.method != 'PUT':
        return JsonResponse({"error": "Método no permitido"}, status=405)
    try:
        data = json.loads(request.body)
        id = data.get('id')
        if not id:
            return JsonResponse({"error": "ID es requerido"}, status=400)
        p = PrestamoEspacio.objects.get(id=id)
        if 'espacio_id' in data:
            p.espacio = EspacioFisico.objects.get(id=data.get('espacio_id'))
        if 'usuario_id' in data:
            p.usuario = Usuario.objects.get(id=data.get('usuario_id')) if data.get('usuario_id') else None
        if 'administrador_id' in data:
            p.administrador = Usuario.objects.get(id=data.get('administrador_id')) if data.get('administrador_id') else None
        if 'fecha' in data:
            p.fecha = datetime.date.fromisoformat(data.get('fecha'))
        if 'hora_inicio' in data:
            p.hora_inicio = datetime.time.fromisoformat(data.get('hora_inicio'))
        if 'hora_fin' in data:
            p.hora_fin = datetime.time.fromisoformat(data.get('hora_fin'))
        if 'motivo' in data:
            p.motivo = data.get('motivo')
        if 'estado' in data:
            p.estado = data.get('estado')
        p.save()
        return JsonResponse({"message": "Prestamo actualizado", "id": p.id}, status=200)
    except PrestamoEspacio.DoesNotExist:
        return JsonResponse({"error": "Prestamo no encontrado."}, status=404)
    except (EspacioFisico.DoesNotExist, Usuario.DoesNotExist):
        return JsonResponse({"error": "Relacionada no encontrada."}, status=404)
    except ValueError:
        return JsonResponse({"error": "Formato de fecha/hora inválido."}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({"error": "JSON inválido."}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
def delete_prestamo(request):
    if request.method != 'DELETE':
        return JsonResponse({"error": "Método no permitido"}, status=405)
    try:
        data = json.loads(request.body)
        id = data.get('id')
        if not id:
            return JsonResponse({"error": "ID es requerido"}, status=400)
        p = PrestamoEspacio.objects.get(id=id)
        p.delete()
        return JsonResponse({"message": "Prestamo eliminado"}, status=200)
    except PrestamoEspacio.DoesNotExist:
        return JsonResponse({"error": "Prestamo no encontrado."}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({"error": "JSON inválido."}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
def get_prestamo(request, id=None):
    if id is None:
        return JsonResponse({"error": "El ID es requerido en la URL"}, status=400)
    try:
        p = PrestamoEspacio.objects.get(id=id)
        return JsonResponse({
            "id": p.id,
            "espacio_id": p.espacio.id,
            "usuario_id": (p.usuario.id if p.usuario else None),
            "administrador_id": (p.administrador.id if p.administrador else None),
            "fecha": str(p.fecha),
            "hora_inicio": str(p.hora_inicio),
            "hora_fin": str(p.hora_fin),
            "motivo": p.motivo,
            "estado": p.estado
        }, status=200)
    except PrestamoEspacio.DoesNotExist:
        return JsonResponse({"error": "Prestamo no encontrado."}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    
def list_prestamos(request):
    if request.method == 'GET':
        items = PrestamoEspacio.objects.all()
        lst = [{
            "id": i.id,
            "espacio_id": i.espacio.id,
            "usuario_id": (i.usuario.id if i.usuario else None),
            "administrador_id": (i.administrador.id if i.administrador else None),
            "fecha": str(i.fecha),
            "hora_inicio": str(i.hora_inicio),
            "hora_fin": str(i.hora_fin),
            "motivo": i.motivo,
            "estado": i.estado
        } for i in items]
        return JsonResponse({"prestamos": lst}, status=200)


@csrf_exempt
def login(request):
    """
    POST JSON: { "correo": "...", "contrasena": "..." }
    Si las credenciales son correctas, se guarda user_id en la sesión.
    """
    if request.method != 'POST':
        return JsonResponse({"error": "Método no permitido"}, status=405)
    try:
        data = json.loads(request.body)
        correo = data.get('correo')
        contrasena = data.get('contrasena')
        if not correo or not contrasena:
            return JsonResponse({"error": "correo y contrasena son requeridos"}, status=400)
        try:
            u = Usuario.objects.get(correo=correo)
        except Usuario.DoesNotExist:
            return JsonResponse({"error": "Credenciales inválidas"}, status=401)
        # Nota: aquí se compara directamente con contrasena_hash. Si usas hash real,
        # reemplaza la comparación por la verificación correspondiente.
        if u.contrasena_hash != contrasena:
            return JsonResponse({"error": "Credenciales inválidas"}, status=401)
        # Guardar datos mínimos en sesión
        request.session['user_id'] = u.id
        request.session['correo'] = u.correo
        request.session['is_authenticated'] = True
        return JsonResponse({"message": "Login exitoso", "id": u.id, "nombre": u.nombre}, status=200)
    except json.JSONDecodeError:
        return JsonResponse({"error": "JSON inválido."}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
def logout(request):
    """
    POST o GET para cerrar sesión: limpia la sesión del usuario.
    """
    if request.method not in ('POST', 'GET'):
        return JsonResponse({"error": "Método no permitido"}, status=405)
    try:
        request.session.flush()
        return JsonResponse({"message": "Logout exitoso"}, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

