# AgriConnect

An Offline-First Platform for Tribal Farmers and NGOs

## Project Overview
AgriConnect is a full-stack web application designed to connect tribal farmers with local NGOs, VLEs, and agriculture experts. The platform enables farmers to report issues, receive personalized help, access government schemes, and track their growth—even in low or no-internet regions.

## Features

- 🔐 OTP-based authentication with role-based access control
- 🌍 Interactive map dashboard for issue visualization
- 📱 Offline-first issue reporting
- 🤖 AI-powered chatbot for agricultural assistance
- 📲 WhatsApp & IVR integration for low-bandwidth access
- 📊 PDF reports with data visualization
- 🌐 Multi-language support (English, Hindi, Telugu, Tamil)
- 📄 CSV data import/export
- 📚 AI-generated educational content
- 💬 Success stories and feedback system

## Tech Stack

### Frontend
- Next.js 14 (React 18)
- TypeScript
- Tailwind CSS
- Redux Toolkit
- Leaflet.js (for maps)
- i18next (for internationalization)
- Chart.js (for data visualization)

### Backend
- FastAPI
- Python 3.10+
- Supabase (Auth & Database)
- MongoDB (for document storage)
- LangChain (for AI features)
- Twilio (for WhatsApp/IVR)

## Getting Started

### Prerequisites
- Node.js 18+ and npm
- Python 3.10+
- Docker (for local development with Supabase)

### Installation
1. Clone the repository
2. Set up the backend:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Set up the frontend:
   ```bash
   cd frontend
   npm install
   ```

## Development

### Running the Backend
```bash
cd backend
uvicorn main:app --reload
```

### Running the Frontend
```bash
cd frontend
npm run dev
```

## License
MIT
