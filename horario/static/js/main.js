const API_BASE_URL = 'http://localhost:8000/horario';

// ========== Rol API ==========
const RolAPI = {
  create: async (nombre, descripcion) => {
    const response = await fetch(`${API_BASE_URL}/roles/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ nombre, descripcion })
    });
    return response.json();
  },
  update: async (id, nombre, descripcion) => {
    const response = await fetch(`${API_BASE_URL}/roles/`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id, nombre, descripcion })
    });
    return response.json();
  },
  delete: async (id) => {
    const response = await fetch(`${API_BASE_URL}/roles/`, {
      method: 'DELETE',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id })
    });
    return response.json();
  },
  getById: async (id) => {
    const response = await fetch(`${API_BASE_URL}/roles/${id}/`, { method: 'GET' });
    return response.json();
  },
  list: async () => {
    const response = await fetch(`${API_BASE_URL}/roles/`, { method: 'GET' });
    return response.json();
  }
};

// ========== Sede API ==========
const SedeAPI = {
  create: async (nombre, direccion, ciudad, activa = true) => {
    const response = await fetch(`${API_BASE_URL}/sedes/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ nombre, direccion, ciudad, activa })
    });
    return response.json();
  },
  update: async (id, nombre, direccion, ciudad, activa) => {
    const response = await fetch(`${API_BASE_URL}/sedes/`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id, nombre, direccion, ciudad, activa })
    });
    return response.json();
  },
  delete: async (id) => {
    const response = await fetch(`${API_BASE_URL}/sedes/`, {
      method: 'DELETE',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id })
    });
    return response.json();
  },
  getById: async (id) => {
    const response = await fetch(`${API_BASE_URL}/sedes/${id}/`, { method: 'GET' });
    return response.json();
  },
  list: async () => {
    const response = await fetch(`${API_BASE_URL}/sedes/`, { method: 'GET' });
    return response.json();
  }
};

// ========== Facultad API ==========
const FacultadAPI = {
  create: async (nombre, activa = true) => {
    const response = await fetch(`${API_BASE_URL}/facultades/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ nombre, activa })
    });
    return response.json();
  },
  update: async (id, nombre, activa) => {
    const response = await fetch(`${API_BASE_URL}/facultades/`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id, nombre, activa })
    });
    return response.json();
  },
  delete: async (id) => {
    const response = await fetch(`${API_BASE_URL}/facultades/`, {
      method: 'DELETE',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id })
    });
    return response.json();
  },
  getById: async (id) => {
    const response = await fetch(`${API_BASE_URL}/facultades/${id}/`, { method: 'GET' });
    return response.json();
  },
  list: async () => {
    const response = await fetch(`${API_BASE_URL}/facultades/`, { method: 'GET' });
    return response.json();
  }
};

// ========== Programa API ==========
const ProgramaAPI = {
  create: async (nombre, facultad_id, activo = true) => {
    const response = await fetch(`${API_BASE_URL}/programas/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ nombre, facultad_id, activo })
    });
    return response.json();
  },
  update: async (id, nombre, facultad_id, activo) => {
    const response = await fetch(`${API_BASE_URL}/programas/`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id, nombre, facultad_id, activo })
    });
    return response.json();
  },
  delete: async (id) => {
    const response = await fetch(`${API_BASE_URL}/programas/`, {
      method: 'DELETE',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id })
    });
    return response.json();
  },
  getById: async (id) => {
    const response = await fetch(`${API_BASE_URL}/programas/${id}/`, { method: 'GET' });
    return response.json();
  },
  list: async () => {
    const response = await fetch(`${API_BASE_URL}/programas/`, { method: 'GET' });
    return response.json();
  }
};

// ========== PeriodoAcademico API ==========
const PeriodoAPI = {
  create: async (nombre, fecha_inicio, fecha_fin, activo = true) => {
    const response = await fetch(`${API_BASE_URL}/periodos/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ nombre, fecha_inicio, fecha_fin, activo })
    });
    return response.json();
  },
  update: async (id, nombre, fecha_inicio, fecha_fin, activo) => {
    const response = await fetch(`${API_BASE_URL}/periodos/`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id, nombre, fecha_inicio, fecha_fin, activo })
    });
    return response.json();
  },
  delete: async (id) => {
    const response = await fetch(`${API_BASE_URL}/periodos/`, {
      method: 'DELETE',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id })
    });
    return response.json();
  },
  getById: async (id) => {
    const response = await fetch(`${API_BASE_URL}/periodos/${id}/`, { method: 'GET' });
    return response.json();
  },
  list: async () => {
    const response = await fetch(`${API_BASE_URL}/periodos/`, { method: 'GET' });
    return response.json();
  }
};

// ========== Grupo API ==========
const GrupoAPI = {
  create: async (nombre, programa_id, periodo_id, semestre, activo = true) => {
    const response = await fetch(`${API_BASE_URL}/grupos/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ nombre, programa_id, periodo_id, semestre, activo })
    });
    return response.json();
  },
  update: async (id, nombre, programa_id, periodo_id, semestre, activo) => {
    const response = await fetch(`${API_BASE_URL}/grupos/`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id, nombre, programa_id, periodo_id, semestre, activo })
    });
    return response.json();
  },
  delete: async (id) => {
    const response = await fetch(`${API_BASE_URL}/grupos/`, {
      method: 'DELETE',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id })
    });
    return response.json();
  },
  getById: async (id) => {
    const response = await fetch(`${API_BASE_URL}/grupos/${id}/`, { method: 'GET' });
    return response.json();
  },
  list: async () => {
    const response = await fetch(`${API_BASE_URL}/grupos/`, { method: 'GET' });
    return response.json();
  }
};

// ========== Asignatura API ==========
const AsignaturaAPI = {
  create: async (nombre, codigo, creditos) => {
    const response = await fetch(`${API_BASE_URL}/asignaturas/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ nombre, codigo, creditos })
    });
    return response.json();
  },
  update: async (id, nombre, codigo, creditos) => {
    const response = await fetch(`${API_BASE_URL}/asignaturas/`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id, nombre, codigo, creditos })
    });
    return response.json();
  },
  delete: async (id) => {
    const response = await fetch(`${API_BASE_URL}/asignaturas/`, {
      method: 'DELETE',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id })
    });
    return response.json();
  },
  getById: async (id) => {
    const response = await fetch(`${API_BASE_URL}/asignaturas/${id}/`, { method: 'GET' });
    return response.json();
  },
  list: async () => {
    const response = await fetch(`${API_BASE_URL}/asignaturas/`, { method: 'GET' });
    return response.json();
  }
};

// ========== EspacioFisico API ==========
const EspacioAPI = {
  create: async (sede_id, tipo, capacidad, ubicacion, recursos, disponible = true) => {
    const response = await fetch(`${API_BASE_URL}/espacios/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ sede_id, tipo, capacidad, ubicacion, recursos, disponible })
    });
    return response.json();
  },
  update: async (id, sede_id, tipo, capacidad, ubicacion, recursos, disponible) => {
    const response = await fetch(`${API_BASE_URL}/espacios/`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id, sede_id, tipo, capacidad, ubicacion, recursos, disponible })
    });
    return response.json();
  },
  delete: async (id) => {
    const response = await fetch(`${API_BASE_URL}/espacios/`, {
      method: 'DELETE',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id })
    });
    return response.json();
  },
  getById: async (id) => {
    const response = await fetch(`${API_BASE_URL}/espacios/${id}/`, { method: 'GET' });
    return response.json();
  },
  list: async () => {
    const response = await fetch(`${API_BASE_URL}/espacios/`, { method: 'GET' });
    return response.json();
  }
};

// ========== Recurso API ==========
const RecursoAPI = {
  create: async (nombre, descripcion) => {
    const response = await fetch(`${API_BASE_URL}/recursos/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ nombre, descripcion })
    });
    return response.json();
  },
  update: async (id, nombre, descripcion) => {
    const response = await fetch(`${API_BASE_URL}/recursos/`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id, nombre, descripcion })
    });
    return response.json();
  },
  delete: async (id) => {
    const response = await fetch(`${API_BASE_URL}/recursos/`, {
      method: 'DELETE',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id })
    });
    return response.json();
  },
  getById: async (id) => {
    const response = await fetch(`${API_BASE_URL}/recursos/${id}/`, { method: 'GET' });
    return response.json();
  },
  list: async () => {
    const response = await fetch(`${API_BASE_URL}/recursos/`, { method: 'GET' });
    return response.json();
  }
};

// ========== EspacioRecurso API ==========
const EspacioRecursoAPI = {
  create: async (espacio_id, recurso_id, disponible = true) => {
    const response = await fetch(`${API_BASE_URL}/espacio-recursos/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ espacio_id, recurso_id, disponible })
    });
    return response.json();
  },
  update: async (espacio_id, recurso_id, disponible) => {
    const response = await fetch(`${API_BASE_URL}/espacio-recursos/`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ espacio_id, recurso_id, disponible })
    });
    return response.json();
  },
  delete: async (espacio_id, recurso_id) => {
    const response = await fetch(`${API_BASE_URL}/espacio-recursos/`, {
      method: 'DELETE',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ espacio_id, recurso_id })
    });
    return response.json();
  },
  getById: async (espacio_id, recurso_id) => {
    const response = await fetch(`${API_BASE_URL}/espacio-recursos/${espacio_id}/${recurso_id}/`, { method: 'GET' });
    return response.json();
  },
  list: async () => {
    const response = await fetch(`${API_BASE_URL}/espacio-recursos/`, { method: 'GET' });
    return response.json();
  }
};

// ========== Usuario API ==========
const UsuarioAPI = {
  create: async (nombre, correo, contrasena, rol_id, activo = true) => {
    const response = await fetch(`${API_BASE_URL}/usuarios/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ nombre, correo, contrasena, rol_id, activo })
    });
    return response.json();
  },
  update: async (id, nombre, correo, contrasena, rol_id, activo) => {
    const response = await fetch(`${API_BASE_URL}/usuarios/`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id, nombre, correo, contrasena, rol_id, activo })
    });
    return response.json();
  },
  delete: async (id) => {
    const response = await fetch(`${API_BASE_URL}/usuarios/`, {
      method: 'DELETE',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id })
    });
    return response.json();
  },
  getById: async (id) => {
    const response = await fetch(`${API_BASE_URL}/usuarios/${id}/`, { method: 'GET' });
    return response.json();
  },
  list: async () => {
    const response = await fetch(`${API_BASE_URL}/usuarios/`, { method: 'GET' });
    return response.json();
  },
  login: async (correo, contrasena) => {
    const response = await fetch(`${API_BASE_URL}/login/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ correo, contrasena })
    });
    return response.json();
  },
  logout: async () => {
    const response = await fetch(`${API_BASE_URL}/logout/`, { method: 'POST' });
    return response.json();
  },
  changePassword: async (correo, old_contrasena, new_contrasena) => {
    const response = await fetch(`${API_BASE_URL}/change-password/`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ correo, old_contrasena, new_contrasena })
    });
    return response.json();
  }
};

// ========== Horario API ==========
const HorarioAPI = {
  create: async (grupo_id, asignatura_id, espacio_id, dia_semana, hora_inicio, hora_fin, docente_id, cantidad_estudiantes) => {
    const response = await fetch(`${API_BASE_URL}/horarios/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ grupo_id, asignatura_id, espacio_id, dia_semana, hora_inicio, hora_fin, docente_id, cantidad_estudiantes })
    });
    return response.json();
  },
  update: async (id, grupo_id, asignatura_id, espacio_id, dia_semana, hora_inicio, hora_fin, docente_id, cantidad_estudiantes) => {
    const response = await fetch(`${API_BASE_URL}/horarios/`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id, grupo_id, asignatura_id, espacio_id, dia_semana, hora_inicio, hora_fin, docente_id, cantidad_estudiantes })
    });
    return response.json();
  },
  delete: async (id) => {
    const response = await fetch(`${API_BASE_URL}/horarios/`, {
      method: 'DELETE',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id })
    });
    return response.json();
  },
  getById: async (id) => {
    const response = await fetch(`${API_BASE_URL}/horarios/${id}/`, { method: 'GET' });
    return response.json();
  },
  list: async () => {
    const response = await fetch(`${API_BASE_URL}/horarios/`, { method: 'GET' });
    return response.json();
  }
};

// ========== HorarioFusionado API ==========
const HorarioFusionadoAPI = {
  create: async (grupo1_id, grupo2_id, grupo3_id, asignatura_id, espacio_id, dia_semana, hora_inicio, hora_fin, docente_id, cantidad_estudiantes, comentario) => {
    const response = await fetch(`${API_BASE_URL}/horarios-fusionados/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ grupo1_id, grupo2_id, grupo3_id, asignatura_id, espacio_id, dia_semana, hora_inicio, hora_fin, docente_id, cantidad_estudiantes, comentario })
    });
    return response.json();
  },
  update: async (id, grupo1_id, grupo2_id, grupo3_id, asignatura_id, espacio_id, dia_semana, hora_inicio, hora_fin, docente_id, cantidad_estudiantes, comentario) => {
    const response = await fetch(`${API_BASE_URL}/horarios-fusionados/`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id, grupo1_id, grupo2_id, grupo3_id, asignatura_id, espacio_id, dia_semana, hora_inicio, hora_fin, docente_id, cantidad_estudiantes, comentario })
    });
    return response.json();
  },
  delete: async (id) => {
    const response = await fetch(`${API_BASE_URL}/horarios-fusionados/`, {
      method: 'DELETE',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id })
    });
    return response.json();
  },
  getById: async (id) => {
    const response = await fetch(`${API_BASE_URL}/horarios-fusionados/${id}/`, { method: 'GET' });
    return response.json();
  },
  list: async () => {
    const response = await fetch(`${API_BASE_URL}/horarios-fusionados/`, { method: 'GET' });
    return response.json();
  }
};

// ========== PrestamoEspacio API ==========
const PrestamoAPI = {
  create: async (espacio_id, usuario_id, administrador_id, fecha, hora_inicio, hora_fin, motivo, estado = 'Pendiente') => {
    const response = await fetch(`${API_BASE_URL}/prestamos/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ espacio_id, usuario_id, administrador_id, fecha, hora_inicio, hora_fin, motivo, estado })
    });
    return response.json();
  },
  update: async (id, espacio_id, usuario_id, administrador_id, fecha, hora_inicio, hora_fin, motivo, estado) => {
    const response = await fetch(`${API_BASE_URL}/prestamos/`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id, espacio_id, usuario_id, administrador_id, fecha, hora_inicio, hora_fin, motivo, estado })
    });
    return response.json();
  },
  delete: async (id) => {
    const response = await fetch(`${API_BASE_URL}/prestamos/`, {
      method: 'DELETE',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id })
    });
    return response.json();
  },
  getById: async (id) => {
    const response = await fetch(`${API_BASE_URL}/prestamos/${id}/`, { method: 'GET' });
    return response.json();
  },
  list: async () => {
    const response = await fetch(`${API_BASE_URL}/prestamos/`, { method: 'GET' });
    return response.json();
  }
};

// Export APIs for use in other modules
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    RolAPI, SedeAPI, FacultadAPI, ProgramaAPI, PeriodoAPI, GrupoAPI,
    AsignaturaAPI, EspacioAPI, RecursoAPI, EspacioRecursoAPI, UsuarioAPI,
    HorarioAPI, HorarioFusionadoAPI, PrestamoAPI
  };
}