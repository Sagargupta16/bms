# CLAUDE.md

> This file stacks on top of the workspace root at `C:\Code\GitHub\`:
> - Root [`CLAUDE.md`](../../CLAUDE.md) -- voice, rules, routing map, references, skills, slash commands, conventions.
> - Root [`MEMORY.md`](../../MEMORY.md) -- live facts across repos.
> - Root [`STATUS.md`](../../STATUS.md) -- live PR/CI/security dashboard.
> - [`.claude/resources/`](../../.claude/resources/README.md) -- deep reference for collaboration, workflow, git, OSS, debugging, voice.
>
> Read those first. The guidance below only adds **repo-specific context** -- it does not override anything in the root.

## Project

BMS (Student Management System) -- FastAPI + MongoDB REST API for managing NIT Warangal student profiles: sign-up/sign-in, socials (Instagram/LinkedIn/GitHub), and competitive-programming handles (LeetCode, Codeforces, etc).

Legacy project in maintenance mode. No deployment; runs locally only.

## Stack

- **Language**: Python 3.11 (`.python-version`)
- **Framework**: FastAPI + Uvicorn
- **Database**: MongoDB via PyMongo
- **Package manager**: pip (`requirements.txt`)
- **Deploy target**: local-only (no CI, no deploy config)

## Run

```
pip install -r requirements.txt
cp config/secrets.yml.example config/secrets.yml   # then fill in MongoDB values
uvicorn main:app --reload
```

API at `http://localhost:8000`, Swagger at `/docs`.

## Test

No test suite. `pytest` and `coverage` are in `requirements.txt` but no tests exist.

## Entry points

- `main.py` -- FastAPI app, mounts the students router
- `routes/student_routes.py` -- all `/students` endpoints

## Key files

- `services/student_service.py` -- all business logic (CRUD, sign-up, sign-in)
- `models/student_model.py` -- Pydantic models, source of truth for request/response shapes
- `config/secrets_parser.py` -- loads `config/secrets.yml` and opens the Mongo connection at import time

## Gotchas

- `config/secrets_parser.py` reads `config/secrets.yml` with a relative path at import time -- run from the repo root, and the app dies at startup if the file is missing or MongoDB is unreachable.
- Passwords are stored and compared in plaintext (`sign_in_student` does a direct email+password `find_one`). Known debt -- fix before building any auth feature on top.
- `services/auth_service.py` is empty (0 bytes); auth logic actually lives in `student_service.py`.
- `.nvmrc` (Node 19) and the `node_modules` line in `.dockerignore` are template leftovers -- there is no Node code and no Dockerfile.
- `config/secrets.yml` is gitignored; never commit it.

## API routes

- `GET /students/` -- list all students (password excluded)
- `GET /students/{student_id}` -- get by Mongo ObjectId
- `POST /students/sign-up`, `POST /students/sign-in`
- `PUT /students/{student_id}` (+ `/password`, `/socials`, `/coding`)
- `DELETE /students/{student_id}`
- Full OpenAPI at `/docs` when the server is running.

## DB schema

- Single collection: `students` (no migrations; shapes defined by Pydantic models).

## Auth

- Plaintext email+password match against MongoDB. No JWT, no sessions, no hashing.
- Required config: `config/secrets.yml` with `mongodb.host`, `mongodb.port`, `mongodb.database`, `mongodb.connection_string` (names only, never values).
