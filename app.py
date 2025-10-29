from flask import Flask, request, jsonify, send_from_directory
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
import chromadb
import openai
import os
from dotenv import load_dotenv
from werkzeug.utils import secure_filename
from flask_cors import CORS

# Load environment variables (for local development)
load_dotenv()

# Get OpenAI API key from environment
# This works both locally (.env file) and on Render (environment variables)
openai.api_key = os.getenv('OPENAI_API_KEY') or os.getenv('MYKEY')

if not openai.api_key:
    print("WARNING: OpenAI API key not found in environment variables!")

# Initialize Flask app
app = Flask(__name__, static_folder='.')
CORS(app)

# File upload settings
UPLOAD_FOLDER = 'data'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'docx'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize ChromaDB and LlamaIndex components
chroma_client = chromadb.EphemeralClient()
chroma_collection = chroma_client.create_collection("quickstart")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

def allowed_file(filename):
    """Check if the file extension is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def initialize_index():
    """Load documents and initialize the VectorStoreIndex."""
    try:
        # Check if data folder has any files
        if not os.path.exists("data") or not os.listdir("data"):
            print("WARNING: No documents found in data folder!")
            return VectorStoreIndex.from_documents(
                [], 
                storage_context=storage_context
            )
        
        documents = SimpleDirectoryReader("data").load_data()
        print(f"Loaded {len(documents)} documents from data folder")
        index = VectorStoreIndex.from_documents(
            documents, 
            storage_context=storage_context, 
            show_progress=True
        )
        return index
    except Exception as e:
        print(f"Error initializing index: {str(e)}")
        # Return an empty index if no documents exist
        return VectorStoreIndex.from_documents(
            [], 
            storage_context=storage_context
        )

# Load the index on server startup
print("Initializing index...")
index = initialize_index()
query_engine = index.as_query_engine()
print("Index initialized successfully!")

@app.route('/')
def home():
    """Serve the main HTML page."""
    return send_from_directory('.', 'index.html')

@app.route('/query', methods=['POST'])
def query():
    """Handle queries sent to the RAG pipeline."""
    data = request.get_json()
    query_text = data.get('query', '')
    if not query_text:
        return jsonify({"error": "Query text is required."}), 400

    try:
        response = query_engine.query(query_text)
        return jsonify({"response": str(response)})
    except Exception as e:
        print(f"Error processing query: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle document uploads and update the index."""
    if 'files' not in request.files:
        return jsonify({"error": "No files part"}), 400
    
    files = request.files.getlist('files')
    if not files or files[0].filename == '':
        return jsonify({"error": "No files selected"}), 400

    saved_files = []
    try:
        # Save all valid files
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                saved_files.append(filename)
                print(f"Saved file: {filename}")

        if saved_files:
            # Reinitialize the index with all documents including new ones
            global index, query_engine
            print("Reinitializing index with new documents...")
            index = initialize_index()
            query_engine = index.as_query_engine()
            print("Index reinitialized successfully!")

            return jsonify({
                "message": "Files uploaded and processed successfully",
                "files": saved_files
            })
        else:
            return jsonify({
                "error": "No valid files were uploaded. Allowed types: " + 
                        ", ".join(ALLOWED_EXTENSIONS)
            }), 400

    except Exception as e:
        print(f"Error processing uploads: {str(e)}")
        return jsonify({
            "error": f"Error processing uploads: {str(e)}"
        }), 500

if __name__ == '__main__':
    # Get port from environment variable (Render sets this)
    port = int(os.environ.get('PORT', 5000))
    # Run with host 0.0.0.0 to be accessible externally
    app.run(host='0.0.0.0', port=port, debug=False)
