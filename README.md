# Krutrim Project

A FastAPI backend API that uses [Krutrim API](https://cloud.olakrutrim.com/console/inference-service?section=api-keys) for the chat interaction with Krutrim-spectre-v2 model using websocket connection.

For more information about the Krutrim API, visit the [Krutrim API Documentation](https://cloud.olakrutrim.com/console/docs?section=models).

## Project Setup

1. Clone the repository

```bash
git clone https://github.com/adistrim/krutrim.git
```

2. Create `.env` file in the backend directory and add the following environment variables

```env
KRUTRIM_API_KEY=YOUR_API_KEY
KRUTRIM_URL=KRUTRIM_URL_FROM_DOCUMENTATION
FIREBASE_DATABASE_URL=YOUR_FIREBASE_DATABASE_URL
```

3. Generate a Firebase service account key and save it as `serviceAccountKey.json` in the backend directory.

### Option 1: Virtual Environment

1. Create a virtual environment

```bash
python -m venv venv
```

2. Activate the virtual environment

```bash
source venv/bin/activate  # For Unix/macOS
venv\Scripts\activate  # For Windows
```

3. Install the dependencies

```bash
pip install -r backend/requirements.txt
```

4. Run the FastAPI server

```bash
cd backend
uvicorn app.main:app --reload
```

5. Run the test

```bash
cd ..
python test/test.py
```

### Option 2: Docker

1. Build the Docker image

```bash
cd backend
docker build -t krutrim-backend .
```

2. Run the Docker container

```bash
docker run -d -p 8000:8000 krutrim-backend
```

5. Run the test

```bash
cd ..
python test/test.py
```

Note: If your server is running on a different port, change the port in the test file on line `6` and `7`.

### Frontend is still in development.

## LICENSE

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
