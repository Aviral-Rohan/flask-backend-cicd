# Flask Backend (CI/CD with Jenkins)

A small Flask API used with the Express frontend.

- `GET /health` – health check
- `POST /submit` – accepts `name` and `email`, returns JSON

## Run locally
```bash
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python app.py          # http://localhost:5000
python -m pytest -v    # run the tests
```

## CI/CD
The `Jenkinsfile` runs on every push: checkout → install dependencies → test → deploy → health check.
