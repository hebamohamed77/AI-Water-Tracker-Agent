# 💧 AI Water Tracker

An AI-powered hydration tracking assistant that helps you monitor your daily water intake, sends smart reminders, and provides personalised insights through an AI chat agent — built with LangChain, FastAPI, and Streamlit.

---

## 🚀 Features

- 🤖 **AI Chat Agent** — Ask questions about your hydration habits and get smart recommendations powered by LangChain + OpenAI
- 📊 **Intake Tracking** — Log and monitor your daily water consumption
- ⏰ **Smart Reminders** — Scheduled notifications to keep you hydrated throughout the day
- 🗄️ **Persistent Storage** — SQLite database to store your history and progress
- 🖥️ **Streamlit UI** — Clean, interactive web interface
- ⚡ **REST API** — FastAPI backend for fast, async data handling
- 🖱️ **CLI Support** — Run and manage the app directly from the terminal with Typer

---

## 🛠️ Tech Stack

| Layer | Library | Version |
|---|---|---|
| AI / LLM | LangChain | 0.1.12 |
| AI / LLM | OpenAI | 1.14.1 |
| AI / LLM | LlamaIndex | latest |
| Backend | FastAPI | 0.109.2 |
| Backend | Uvicorn | 0.27.0 |
| Database | SQLAlchemy | 2.0.27 |
| Database | sqlite-utils | 3.35.0 |
| Frontend | Streamlit | 1.31.1 |
| Scheduling | APScheduler | 3.10.4 |
| CLI | Typer | 0.9.0 |
| Logging | Loguru | 0.7.2 |
| Config | python-dotenv | 1.0.1 |

---

---

## ⚙️ Getting Started

### Prerequisites

- [Anaconda](https://www.anaconda.com/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) installed
- An [OpenAI API key](https://platform.openai.com/account/api-keys)

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-water-tracker.git
cd ai-water-tracker
```

### 2. Create and activate the conda environment

```bash
conda create --name Ai-water-tracker python=3.10
conda activate Ai-water-tracker
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Copy the example file and fill in your values:

```bash
cp .env.example .env
```

Then edit `.env`:

```env
OPENAI_API_KEY=your_openai_api_key_here
DATABASE_URL=sqlite:///./water_tracker.db
APP_ENV=development
```

### 5. Run the backend API

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### 6. Run the Streamlit UI

In a new terminal (with the environment activated):

```bash
streamlit run ui/app.py
```

The UI will open at `http://localhost:8501`

---

## 🔑 Environment Variables

| Variable | Description | Required |
|---|---|---|
| `OPENAI_API_KEY` | Your OpenAI API key | ✅ Yes |
| `DATABASE_URL` | SQLite database path | ✅ Yes |
| `APP_ENV` | `development` or `production` | Optional |

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Health check |
| `POST` | `/log` | Log a water intake entry |
| `GET` | `/history` | Get intake history |
| `GET` | `/summary` | Get daily summary |
| `POST` | `/chat` | Send a message to the AI agent |

Full interactive docs available at `http://localhost:8000/docs` once the server is running.

---

## 🖥️ CLI Usage

```bash
# Log water intake directly from terminal
python cli.py log --amount 500 --unit ml

# View today's summary
python cli.py summary

# Start the reminder scheduler
python cli.py start-reminders
```

---

## 🧪 Development Notes

- Logs are handled by **Loguru** and stored in `logs/app.log`
- Scheduled reminders use **APScheduler** with an in-memory job store in development
- Database migrations can be handled manually via **sqlite-utils** CLI

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a pull request

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

> Built with 💧 and Python 3.10 · Conda environment: `Ai-water-tracker`