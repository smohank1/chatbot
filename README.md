# RAG Chatbot - LlamaIndex & Flask

A Retrieval-Augmented Generation (RAG) chatbot built with Flask, LlamaIndex, ChromaDB, and OpenAI. Upload documents and ask questions about them!

## Features

- 📄 Upload multiple documents (PDF, TXT, DOCX)
- 💬 Interactive chat interface
- 🔍 Semantic search using ChromaDB vector store
- 🤖 Powered by OpenAI's language models
- 🎨 Clean, responsive UI

## Local Development

### Prerequisites

- Python 3.13.5
- OpenAI API key

### Setup

1. Clone the repository
```bash
git clone <your-repo-url>
cd <your-repo-name>
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory
```bash
OPENAI_API_KEY=your_openai_api_key_here
```

5. Run the application
```bash
python app.py
```

6. Open your browser and navigate to `http://localhost:5000`

## Deployment on Render

### Step 1: Push Code to GitHub

1. Initialize git (if not already done):
```bash
git init
git add .
git commit -m "Initial commit"
```

2. Push to GitHub:
```bash
git remote add origin <your-github-repo-url>
git branch -M main
git push -u origin main
```

### Step 2: Deploy on Render

1. Go to [render.com](https://render.com) and sign up/login
2. Click "New +" and select "Web Service"
3. Connect your GitHub repository
4. Render will auto-detect the `render.yaml` configuration

**OR manually configure:**

- **Name**: rag-chatbot (or your preferred name)
- **Region**: Oregon (or closest to you)
- **Branch**: main
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `python app.py`

### Step 3: Set Environment Variables

In your Render dashboard:
1. Go to your service's "Environment" tab
2. Add the following environment variable:
   - **Key**: `OPENAI_API_KEY`
   - **Value**: Your OpenAI API key

### Step 4: Deploy

Click "Create Web Service" and wait for deployment to complete (5-10 minutes).

Your app will be available at: `https://your-service-name.onrender.com`

## Important Notes for Free Tier

⚠️ **Render Free Tier Limitations:**
- Service spins down after 15 minutes of inactivity
- First request after spin-down takes 30-60 seconds to wake up
- Ephemeral storage means uploaded files are lost on restart/redeploy
- The sample document (`smartwatch-manual.pdf`) is included in the repo and will always be available

## Project Structure

```
.
├── app.py                      # Flask backend
├── index.html                  # Frontend UI
├── requirements.txt            # Python dependencies
├── render.yaml                 # Render configuration
├── .gitignore                  # Git ignore file
├── data/                       # Document storage
│   └── smartwatch-manual.pdf   # Sample document
└── README.md                   # This file
```

## How It Works

1. **Document Upload**: Users upload documents (PDF, TXT, DOCX)
2. **Indexing**: LlamaIndex processes documents and creates embeddings
3. **Vector Storage**: ChromaDB stores embeddings for fast retrieval
4. **Query**: User asks questions
5. **Retrieval**: System finds relevant document chunks
6. **Generation**: OpenAI generates answers based on retrieved context

## Technologies Used

- **Backend**: Flask, Python
- **RAG Framework**: LlamaIndex
- **Vector Store**: ChromaDB
- **LLM**: OpenAI GPT
- **Frontend**: Vanilla JavaScript, HTML, CSS

## Troubleshooting

### OpenAI API Key Error
Make sure your OpenAI API key is correctly set in the environment variables.

### Documents Not Loading
Check that documents are in the `data/` folder and are valid file types (PDF, TXT, DOCX).

### Connection Error
If running locally, ensure the Flask server is running on port 5000.

## License

MIT License

## Support

For issues or questions, please open an issue on GitHub.
