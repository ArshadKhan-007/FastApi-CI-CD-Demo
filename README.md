# flask-cicd-demo 🚀

A simple FastAPI application containerized with Docker and automated using GitHub Actions CI/CD pipeline.

---

## What This Project Does

Every time code is pushed to the `main` branch, GitHub Actions automatically:
1. Spins up a fresh Ubuntu machine in the cloud
2. Clones the repository
3. Logs into Docker Hub
4. Builds the Docker image
5. Pushes the image to Docker Hub

No manual `docker build` or `docker push` needed. Ever.

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| FastAPI | Python web framework |
| Docker | Containerization |
| GitHub Actions | CI/CD pipeline automation |
| Docker Hub | Container image registry |

---

## Project Structure

```
flask-cicd-demo/
├── .github/
│   └── workflows/
│       └── ci.yml        # GitHub Actions pipeline
├── app.py                # FastAPI application
├── requirements.txt      # Python dependencies
├── Dockerfile            # Container build instructions
├── docker-compose.yml    # Local multi-container setup
└── .gitignore            # Keeps secrets out of git
```

---

## API Endpoints

| Method | Endpoint | Response |
|--------|----------|----------|
| GET | `/` | `{"message": "Hello from CI/CD pipeline!"}` |
| GET | `/health` | `{"status": "ok"}` |
| GET | `/ping` | `{"message": "pong"}` |

---

## Run Locally

**Without Docker:**
```bash
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 5000
```

**With Docker:**
```bash
docker build -t flask-cicd-demo .
docker run -p 5000:5000 flask-cicd-demo
```

**With Docker Compose:**
```bash
docker compose up
```

Visit: `http://localhost:5000`

---

## CI/CD Pipeline

The pipeline is defined in `.github/workflows/ci.yml`.

```
Push to main
     │
     ▼
GitHub Actions triggered
     │
     ▼
Checkout code
     │
     ▼
Login to Docker Hub
     │
     ▼
Build Docker image
     │
     ▼
Push to Docker Hub ✅
```

### Required GitHub Secrets

Go to **Repo → Settings → Secrets and variables → Actions** and add:

| Secret | Value |
|--------|-------|
| `DOCKERHUB_USERNAME` | Your Docker Hub username |
| `DOCKERHUB_TOKEN` | Docker Hub Personal Access Token |

> ⚠️ Never use your actual password. Always use an access token.

---

## What I Learned

- Writing a `Dockerfile` and optimizing image size with multi-stage builds
- Using Docker networking and Docker Compose
- Pushing images to Docker Hub
- Writing a GitHub Actions workflow from scratch
- Storing secrets securely using GitHub Secrets
- Automating the entire build + push process on every git push

---

## Docker Hub

Image available at:
```
docker pull <your-dockerhub-username>/flask-cicd-demo:latest
```
