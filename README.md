# StudyMate LMS

StudyMate is a full-stack learning management system for schools. It brings course delivery, assignments, grading, schedules, student groups, academic records, awards, announcements, communities, and personal task management into one platform.

## Author

**Assylkhan Yeraliyev — software author and lead full-stack developer**

Assylkhan independently developed StudyMate over approximately 12–14 months as a personal full-stack project. His work covered product planning, the React/Redux frontend, the Django REST backend, database-backed school workflows, authentication, and deployment setup.

StudyMate was created to explore how one platform can make academic administration and everyday learning tasks easier for school managers, teachers, and students.

## Features

- Role-based access for managers, teachers, and students
- School, user, grade, group, and subject administration
- Courses, enrolments, syllabuses, and assignments
- Assignment marks, term marks, and annual marks
- Timetables for students, teachers, groups, rooms, and courses
- School and course announcements with discussions
- Student awards, leaderboards, and public profiles
- Communities and memberships
- Personal to-do lists and dashboards
- JWT authentication and a REST API

## Technology

- **Frontend:** React 18, Redux Toolkit, React Router, Material UI, Ant Design
- **Backend:** Python, Django, Django REST Framework, Simple JWT
- **Database:** SQLite for local development; the architecture can be adapted to PostgreSQL
- **Tooling:** Docker and Docker Compose

## Quick start with Docker

1. Copy the environment template:

   ```bash
   cp backend/.env.example backend/src/.env
   ```

2. Build and start both services:

   ```bash
   docker compose up --build
   ```

3. Open the frontend at `http://localhost:3000`. The API is available at `http://localhost:8000/api/`.

## Local development

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example src/.env
python src/manage.py migrate
python src/manage.py seed_db
python src/manage.py runserver
```

### Frontend

```bash
cd frontend
npm ci
cp .env.example .env
npm start
```

## Configuration

Backend settings are read from `backend/src/.env`. Frontend API configuration is read from `REACT_APP_API_URL`; it defaults to `http://127.0.0.1:8000/` for local development.

Do not commit production secrets, uploaded media, local databases, or `.env` files.

## Deploy on Render

This repository includes a `render.yaml` Blueprint that provisions:

- A React static site
- A Django web service
- A PostgreSQL database

After pushing the repository to GitHub:

1. Sign in to Render with GitHub.
2. Select **New → Blueprint**.
3. Connect the `yeraliyeeev/studymate-lms` repository.
4. Keep the Blueprint path as `render.yaml`.
5. Review the three resources and select **Deploy Blueprint**.

The initial deployment runs migrations and safely creates demo data only when the database is empty. Subsequent deployments preserve the existing database.

The free backend service can take a short time to wake after inactivity. When both deployments succeed, add the frontend URL to the GitHub repository's **Website** field.

## Demo account

After running `seed_db`, sign in locally with:

- Email: `admin@gmail.com`
- Password: `admin`

These credentials are for local demonstration only and must be replaced before deployment.

## Project structure

```text
backend/    Django REST API and application modules
frontend/   React single-page application
project/    Database schema reference files
```

## License and reuse

No open-source licence is included. Contact Assylkhan Yeraliyev before copying, redistributing, or reusing the code.
