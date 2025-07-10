# AgriConnect - Setup Instructions

## Prerequisites

- Node.js 18+ and npm
- Python 3.10+
- Docker (for local Supabase development)
- Git

## Backend Setup

1. **Create and activate a virtual environment**
   ```bash
   cd backend
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the `backend` directory with the following variables:
   ```
   DATABASE_URL=postgresql://postgres:postgres@localhost:5432/postgres
   SECRET_KEY=your-secret-key-here
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=1440
   ```

4. **Run database migrations**
   ```bash
   # After setting up Supabase locally or connecting to a remote instance
   alembic upgrade head
   ```

5. **Start the backend server**
   ```bash
   uvicorn app.main:app --reload
   ```
   The API will be available at `http://localhost:8000`

## Frontend Setup

1. **Install dependencies**
   ```bash
   cd frontend
   npm install
   ```

2. **Set up environment variables**
   Create a `.env.local` file in the `frontend` directory (a template is provided as `.env.local.example`)

3. **Start the development server**
   ```bash
   npm run dev
   ```
   The frontend will be available at `http://localhost:3000`

## Supabase Setup

1. **Set up a new project**
   - Go to [Supabase](https://supabase.com/) and create a new project
   - Get your project URL and anon/public key from Project Settings > API

2. **Set up database tables**
   - Import the SQL schema from `supabase/schema.sql`
   - Or set up tables through the Supabase dashboard

3. **Configure authentication**
   - Enable Phone authentication in the Authentication > Providers section
   - Add your Twilio credentials for OTP verification

## Twilio Setup

1. **Create a Twilio account**
   - Sign up at [Twilio](https://www.twilio.com/)
   - Get your Account SID and Auth Token from the dashboard

2. **Set up a WhatsApp Sandbox**
   - Go to Twilio Console > Messaging > Try it out > Send a WhatsApp message
   - Follow the instructions to connect your phone number to the sandbox

## Development Workflow

1. **Backend Development**
   - API documentation is available at `http://localhost:8000/docs`
   - Write tests in the `tests` directory
   - Run tests with `pytest`

2. **Frontend Development**
   - Follow the component structure in `src/components`
   - Use TypeScript for type safety
   - Write tests with Jest and React Testing Library

## Deployment

### Backend

1. **Docker**
   ```bash
   docker build -t agriconnect-backend .
   docker run -p 8000:8000 agriconnect-backend
   ```

2. **Platform.sh**
   - Follow the Platform.sh documentation for Python applications
   - Set up the required environment variables

### Frontend

1. **Vercel**
   - Connect your GitHub repository to Vercel
   - Set up environment variables in the Vercel dashboard
   - Deploy!

2. **Netlify**
   - Connect your GitHub repository to Netlify
   - Set up build command: `npm run build`
   - Set publish directory: `out`
   - Add environment variables

## Testing

### Backend Tests
```bash
cd backend
pytest
```

### Frontend Tests
```bash
cd frontend
npm test
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT
