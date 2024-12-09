from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)  

openai.api_key = "api key here"

@app.route("/analyze", methods=["POST"])
def analyze_code():
    print(request.json)
    
    data = request.json  
    code = data.get("code")  
    language = data.get("language", "Python")  

    try:
        response = openai.Completion.create(
             model="gpt-3.5-turbo",  
        messages=[
            {"role": "system", "content": "You are an AI assistant that analyzes code for performance bottlenecks."},
            {"role": "user", "content": f"Analyze the following {language} code for performance issues and suggest optimizations:\n\n{code}"}
        ],
        max_tokens=500  
        )
        
        return jsonify({"analysis": response['choices'][0]['message']['content'].strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
