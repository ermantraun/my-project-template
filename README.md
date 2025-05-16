# projectname

Проект **projectname** — это backend-приложение, разработанное с использованием FastAPI, SQLAlchemy и Dishka (внедрение зависимостей).
Он спроектирован с чистой архитектурой, акцентом на модульность и тестируемость компонентов.

---

## 🚀 Технологии

- **FastAPI** — асинхронный веб-фреймворк для создания REST API
- **SQLAlchemy** — ORM для работы с PostgreSQL
- **Dishka** — библиотека для внедрения зависимостей
- **Pytest** — фреймворк для тестирования

---

## 📁 Структура проекта

```bash
projectname/
├── backend/
│   └── api/
│       └── v1/
│           ├── handlers/             # Обработка запросов, маршруты, HTTP-интерфейс
│           ├── application/          # Бизнес-логика и сценарии использования
│           │   └── user/             # Компонент пользователя
│           │       ├── dto.py
│           │       ├── exceptions.py
│           │       ├── interactors.py
│           │       ├── interfaces.py
│           │       └── validators.py
│           ├── domen/                # Доменные сущности (чистые Python-классы)
│           ├── infrastructure/       # Работа с БД, файлами и внешними сервисами
│           │   ├── db/
│           │   │   ├── database.py
│           │   │   ├── exceptions.py
│           │   │   ├── models.py
│           │   │   └── repositories.py
│           │   ├── file_storage/
│           │   │   ├── file_storage.py
│           │   │   └── exceptions.py
│           ├── config.py             # Конфигурация FastAPI, PostgreSQL, JWT и MinIO
│           ├── ioc.py                # DI-контейнеры Dishka
│           ├── main.py               # Точка входа FastAPI
│           ├── migrations/           # Миграции (если есть)
│           ├── test_direct_handlers.py # E2E тесты напрямую через функции
│           └── test_handlers.py      # E2E тесты через HTTP-клиент
├── requirements.txt
└── README.md
```

---

## ⚙ Конфигурация

```python
class Config(BaseModel):
    postgres: PostgresConfig
    fastapi: FastApiConfig
    jwt: JWTConfig
  
```

Каждая секция конфигурируется через переменные окружения. Пример `.env`:

```dotenv
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_DB=postgres

MINIO_USER=minioadmin
MINIO_PASSWORD=minioadmin
MINIO_HOST=localhost
MINIO_PORT=9000
```

---

## 🧪 Тестирование

```bash
pytest
```

---

## 🧱 Архитектура

Проект построен по принципам **чистой архитектуры**:

- **handlers** — внешний слой, взаимодействующий с клиентом (HTTP).
- **application** — бизнес-логика, разделённая по доменным компонентам.
- **domen** — ядро с доменными сущностями (не зависит ни от чего).
- **infrastructure** — адаптеры к базе данных, файлам и другим технологиям.
- **ioc** — конфигурация внедрения зависимостей.

---

## 📦 Установка

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## 🚀 Запуск

```bash
uvicorn backend.api.v1.main:app --reload
```
