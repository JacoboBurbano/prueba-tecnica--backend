# Backend - Usuario y Manejo de API

## Descripción
Este backend proporciona una API para la gestión de usuarios y actividades. Se ha desarrollado con Django y Django REST Framework (DRF), utilizando filtros dinámicos, paginación y documentación con Swagger.

## Tecnologías utilizadas
- **Django**: Framework principal.
- **Django REST Framework (DRF)**: Para la creación de la API.
- **MySQL**: Base de datos utilizada.
- **drf-yasg**: Generación de documentación Swagger.
- **Render.com**: Plataforma de despliegue.

## Endpoints principales

### Usuarios
- `GET /views/api/users/` → Obtiene la lista de usuarios con filtros dinámicos.
- `POST /views/api/users/` → Crea un nuevo usuario.
- `GET /views/api/users/{id}/` → Obtiene los detalles de un usuario específico.
- `PUT /views/api/users/{id}/` → Actualiza un usuario.
- `DELETE /views/api/users/{id}/` → Elimina un usuario.

### Actividades
- `GET /views/api/activities/` → Obtiene la lista de actividades con filtros dinámicos.
- `POST /views/api/activities/` → Crea una nueva actividad asociada a un usuario.
- `GET /views/api/activities/{id}/` → Obtiene los detalles de una actividad.
- `PUT /views/api/activities/{id}/` → Actualiza una actividad.
- `DELETE /views/api/activities/{id}/` → Elimina una actividad.

## Filtros dinámicos
Los filtros permiten buscar información de forma flexible. Se implementaron en `UserViewSet` y `ActivityViewSet` mediante `django-filter` y `SearchFilter` de DRF.

Ejemplo de uso:
```
GET /views/api/users/?search=manuel
GET /views/api/activities/?user_id=3&search=login
```
Esto permite buscar por nombre de usuario o filtrar actividades por usuario específico.

## Índices en la base de datos
Para optimizar las búsquedas, se añadieron índices en los campos más consultados:
```python
class Activity(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, blank=False)
    action = models.CharField(max_length=255)
    timestamp = models.DateField(auto_now_add=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['timestamp'])
        ]
        ordering = ['-timestamp']
        
    def __str__(self):
        return f"{self.user.username} - {self.action}"
```
Esto mejora el rendimiento en búsquedas y filtros.

## Paginación
Se implementó paginación global en `settings.py`:
```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
```
Cada consulta devuelve un máximo de 10 resultados por página.

## Documentación
La documentación Swagger está disponible en:
[Swagger UI](https://prueba-tecnica-backend-492t.onrender.com/swagger/)

Se generó con `drf-yasg`, añadiendo `swagger_auto_schema` a cada vista para especificar los parámetros y respuestas esperadas.

## Despliegue
El backend está desplegado en Render:
🔗 [API en producción](https://prueba-tecnica-backend-492t.onrender.com)

Se utilizó Render para facilitar el despliegue continuo y permitir pruebas en un entorno real.

## Pendientes
No se logró implementar JWT por falta de tiempo aunque la estructura esta echa.

---
### 📌 Autor: **Manuel Jacobo Burbano Jiménez**

