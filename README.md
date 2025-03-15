# Building a Chat App with Ollama

This repository contains the code for a simple chat application built using Ollama, Flask, and basic HTML/CSS/JavaScript. It allows you to interact with large language models running locally on your machine.

Presented by [Actual Reality Technologies](https://actualreality.tech) and [Toledo Codes](https://toledo.codes)

## Setup Instructions

### Prerequisites

- Python 3.8+ installed
- Basic understanding of terminal/command line usage
- Sufficient disk space for language models (4-8GB per model)

### 1. Install Ollama

#### macOS
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

#### Linux
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

#### Windows
- Download the installer from [https://ollama.com/download](https://ollama.com/download)
- Run the installer and follow the prompts

### 2. Start Ollama
After installation, ensure Ollama is running:

#### macOS & Linux
Open a terminal and run:
```bash
ollama serve
```

#### Windows
Ollama should automatically start as a service after installation.

### 3. Pull a Language Model
Pull a model to use with the chat application:

```bash
# Pull the Mistral model (faster, smaller)
ollama pull mistral

# Pull Llama 3.2 (recommended for better quality responses)
ollama pull llama3.2:latest
```

You can also try other models like `llama2`, `codellama`, or specialized models. The Llama 3.2 model is recommended for this workshop as it provides excellent response quality while still running efficiently on most hardware.

### 4. Set Up the Project

Clone this repository or download the files:

```bash
git clone https://github.com/Actual-Reality/OllamaChatbot.git
cd ollama-chat
```

Or create the project structure manually:
```bash
mkdir -p ollama-chat/templates
cd ollama-chat
# Copy the app.py file to this directory
# Copy all HTML files to the templates directory
```

### 5. Create a Python Virtual Environment

#### macOS & Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### 6. Install Dependencies

```bash
pip install flask requests
```

### 7. Run the Application

```bash
python app.py
```

### 8. Access the Chat Interface

Open your web browser and navigate to:
```
http://localhost:5000
```

## Features

- Basic chat interface with local LLM integration
- Support for different AI personas
- Ability to switch between different language models
- Progressive versions showing the evolution of the application

## Troubleshooting

- If Ollama isn't responding, ensure the service is running with `ollama serve`
- For model download issues, check your internet connection and disk space
- If the Flask app doesn't start, ensure port 5000 is available

## Extension Ideas

- Add streaming responses
- Implement chat history persistence
- Create specialized personas for different use cases
- Add file upload capabilities for context

## License

MIT