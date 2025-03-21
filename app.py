from flask import Flask, request, jsonify, render_template, redirect, url_for
import requests
import json
import os

app = Flask(__name__)

OLLAMA_API_URL = "http://localhost:11434/api/generate"
OLLAMA_LIST_URL = "http://localhost:11434/api/tags"

# Define different system prompts for different personas
SYSTEM_PROMPTS = {
    "default": "You are a helpful, friendly AI assistant.",
    "expert": "You are an expert AI assistant with deep knowledge in technology, science, and programming.",
    "creative": "You are a creative AI assistant who provides imaginative and artistic responses.",
    "sustainability": "You are a sustainability expert focused on environmental conservation and eco-friendly solutions.",
    "healthcare": "You are a healthcare assistant providing general health information (with appropriate disclaimers)."
}

# Define our template versions to demonstrate progression
TEMPLATE_VERSIONS = {
    "v1": "index_v1.html",  # Basic chat
    "v2": "index_v2.html",  # With personas
    "v3": "index_v3.html"   # With personas and model switching
}

# Current active version (default to the latest)
current_version = "v3"

@app.route('/')
def index():
    global current_version
    template = TEMPLATE_VERSIONS[current_version]
    
    # Get list of available models from Ollama (for v3)
    try:
        response = requests.get(OLLAMA_LIST_URL)
        models = [model['name'] for model in response.json()['models']]
    except:
        # Fallback if we can't get the list
        models = ["mistral", "llama2", "codellama"]
    
    return render_template(template, 
                          personas=list(SYSTEM_PROMPTS.keys()),
                          models=models,
                          versions=list(TEMPLATE_VERSIONS.keys()),
                          current_version=current_version)

@app.route('/switch/<version>')
def switch_version(version):
    global current_version
    if version in TEMPLATE_VERSIONS:
        current_version = version
    return redirect(url_for('index'))

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    chat_history = data.get('history', [])
    persona = data.get('persona', 'default')
    model = data.get('model', 'mistral')
    
    # Get the appropriate system prompt
    system_prompt = SYSTEM_PROMPTS.get(persona, SYSTEM_PROMPTS['default'])
    
    # Format the prompt with chat history for context
    formatted_history = f"System: {system_prompt}\n"
    for entry in chat_history[-5:]:  # Use last 5 messages for context
        formatted_history += f"{entry['role']}: {entry['content']}\n"
    
    # Prepare the request to Ollama
    ollama_request = {
        "model": model,
        "prompt": f"{formatted_history}Human: {user_message}\nAssistant:",
        "stream": False
    }
    
    try:
        # Send request to Ollama
        response = requests.post(OLLAMA_API_URL, json=ollama_request)
        response.raise_for_status()
        
        # Extract the response
        ollama_response = response.json()
        ai_message = ollama_response.get('response', 'Sorry, I could not generate a response.')
        
        return jsonify({
            "response": ai_message,
            "model": model,
            "persona": persona
        })
    except Exception as e:
        print(f"Error communicating with Ollama: {e}")
        return jsonify({
            "response": f"Error: {str(e)}",
            "model": model,
            "persona": persona
        }), 500

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    if not os.path.exists('templates'):
        os.makedirs('templates')
    app.run(debug=True)