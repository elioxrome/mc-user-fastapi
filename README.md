# mc-user-fastapi

Microservicio en FastAPI con arquitectura hexagonal y datos mockeados en memoria.

## Arquitectura hexagonal

- `app/domain`: entidades de dominio (`User`)
- `app/application/ports`: puertos (contratos de repositorio)
- `app/application/use_cases`: casos de uso (`create`, `update`, `delete`)
- `app/infrastructure/repositories`: adaptadores (`InMemoryUserRepository`)
- `app/api/routes`: adaptadores de entrada HTTP (FastAPI)
- `app/main.py`: composición de la aplicación

## Requisitos

- Python 3.11+

## Ejecutar

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Ejecutar con Docker

```powershell
docker build -t mc-user-fastapi .
docker run --rm -p 8000:8000 mc-user-fastapi
```

El `Dockerfile` usa `uv` para instalar dependencias desde `requirements.txt`.

## Tests

```powershell
uv pip install -r requirements-dev.txt
uv run pytest
```

## Endpoints

- `POST /api/v1/users`
- `PUT /api/v1/users/{user_id}`
- `DELETE /api/v1/users/{user_id}`
- `GET /actuator/health`

## Ejemplos rápidos

Crear usuario:

```bash
curl -X POST http://127.0.0.1:8000/api/v1/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Ana","email":"ana@example.com"}'
```

Editar usuario:

```bash
curl -X PUT http://127.0.0.1:8000/api/v1/users/<id> \
  -H "Content-Type: application/json" \
  -d '{"name":"Ana Maria","email":"ana.maria@example.com"}'
```

Eliminar usuario:

```bash
curl -X DELETE http://127.0.0.1:8000/api/v1/users/<id>
```

Health:

```bash
curl http://127.0.0.1:8000/actuator/health
```
