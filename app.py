from flask import Flask, request, jsonify, render_template_string
import os
from datetime import datetime

app = Flask(__name__)

# Simulación de IA simple para el examen
class SimpleAI:
    """Modelo de IA simple para clasificación de sentimientos"""
    
    def __init__(self):
        self.positive_words = ['bueno', 'excelente', 'genial', 'feliz', 'alegre', 'increíble', 'fantástico']
        self.negative_words = ['malo', 'terrible', 'triste', 'horrible', 'pésimo', 'awful']
    
    def predict_sentiment(self, text):
        """Predice el sentimiento de un texto"""
        text_lower = text.lower()
        positive_count = sum(1 for word in self.positive_words if word in text_lower)
        negative_count = sum(1 for word in self.negative_words if word in text_lower)
        
        if positive_count > negative_count:
            return "positivo", positive_count / (positive_count + negative_count + 1)
        elif negative_count > positive_count:
            return "negativo", negative_count / (positive_count + negative_count + 1)
        else:
            return "neutral", 0.5
    
    def generate_response(self, text):
        """Genera una respuesta basada en el sentimiento"""
        sentiment, confidence = self.predict_sentiment(text)
        
        responses = {
            "positivo": "¡Me alegra que estés de buen ánimo! 😊",
            "negativo": "Lamento que no te sientas bien. ¿Puedo ayudarte en algo? 🤗",
            "neutral": "Entiendo. ¿En qué más puedo ayudarte? 🤔"
        }
        
        return {
            "sentiment": sentiment,
            "confidence": round(confidence, 2),
            "response": responses[sentiment],
            "processed_at": datetime.now().isoformat()
        }

# Inicializar modelo IA
ai_model = SimpleAI()

# Template HTML para la interfaz
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CI/CD Flask IA - Maldonado</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .container {
            background: white;
            border-radius: 20px;
            padding: 40px;
            max-width: 600px;
            width: 100%;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        }
        h1 {
            color: #667eea;
            text-align: center;
            margin-bottom: 10px;
            font-size: 2em;
        }
        .subtitle {
            text-align: center;
            color: #666;
            margin-bottom: 30px;
            font-size: 0.9em;
        }
        .info-box {
            background: #f8f9fa;
            border-left: 4px solid #667eea;
            padding: 15px;
            margin-bottom: 20px;
            border-radius: 5px;
        }
        .info-box h3 {
            color: #667eea;
            margin-bottom: 10px;
            font-size: 1.1em;
        }
        .info-box p {
            color: #666;
            font-size: 0.9em;
            line-height: 1.6;
        }
        .input-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 8px;
            color: #333;
            font-weight: 500;
        }
        textarea {
            width: 100%;
            padding: 15px;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            font-size: 16px;
            resize: vertical;
            min-height: 100px;
            transition: border-color 0.3s;
        }
        textarea:focus {
            outline: none;
            border-color: #667eea;
        }
        button {
            width: 100%;
            padding: 15px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 10px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.2s;
        }
        button:hover {
            transform: translateY(-2px);
        }
        button:active {
            transform: translateY(0);
        }
        #result {
            margin-top: 20px;
            padding: 20px;
            border-radius: 10px;
            display: none;
        }
        .result-positive {
            background: #d4edda;
            border-left: 4px solid #28a745;
        }
        .result-negative {
            background: #f8d7da;
            border-left: 4px solid #dc3545;
        }
        .result-neutral {
            background: #fff3cd;
            border-left: 4px solid #ffc107;
        }
        .badge {
            display: inline-block;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.85em;
            font-weight: 600;
            margin-bottom: 10px;
        }
        .badge-positive { background: #28a745; color: white; }
        .badge-negative { background: #dc3545; color: white; }
        .badge-neutral { background: #ffc107; color: #333; }
        .version {
            text-align: center;
            color: #999;
            font-size: 0.8em;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🤖Prueba de test de sentimientos</h1>
        <p class="subtitle">Proyecto CI/CD - Examen Final</p>
        
        <div class="info-box">
            <h3>📊 Información del Despliegue</h3>
            <p><strong>Estudiante:</strong> Alejandro Maldonado</p>
            <p><strong>Versión:</strong> 1.0.5</p>
            <p><strong>Pipeline:</strong> GitHub Actions</p>
            <p><strong>Registro:</strong> GitHub Packages (GHCR)</p>
        </div>
        
        <div class="input-group">
            <label for="text">Ingresa un texto para analizar:</label>
            <textarea id="text" placeholder="Escribe algo aquí... por ejemplo: 'Este proyecto es excelente y funciona genial'"></textarea>
        </div>
        
        <button onclick="analyzeText()">🔍 Analizar Sentimiento</button>
        
        <div id="result"></div>
        
        <p class="version">v1.0.5 | Desplegado automáticamente vía CI/CD</p>
    </div>
    
    <script>
        async function analyzeText() {
            const text = document.getElementById('text').value;
            
            if (!text.trim()) {
                alert('Por favor ingresa un texto para analizar');
                return;
            }
            
            try {
                const response = await fetch('/api/analyze', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ text: text })
                });
                
                const data = await response.json();
                
                const resultDiv = document.getElementById('result');
                resultDiv.className = 'result-' + data.sentiment;
                resultDiv.innerHTML = `
                    <span class="badge badge-${data.sentiment}">
                        ${data.sentiment.toUpperCase()}
                    </span>
                    <p><strong>Confianza:</strong> ${(data.confidence * 100).toFixed(0)}%</p>
                    <p><strong>Respuesta:</strong> ${data.response}</p>
                    <p style="font-size: 0.85em; color: #666; margin-top: 10px;">
                        Procesado: ${new Date(data.processed_at).toLocaleString()}
                    </p>
                `;
                resultDiv.style.display = 'block';
            } catch (error) {
                alert('Error al analizar el texto: ' + error.message);
            }
        }
        
        document.getElementById('text').addEventListener('keypress', function(e) {
            if (e.key === 'Enter' && e.ctrlKey) {
                analyzeText();
            }
        });
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    """Página principal con interfaz de usuario"""
    return render_template_string(HTML_TEMPLATE)

@app.route('/health')
def health():
    """Endpoint de salud para verificar que la app está funcionando"""
    return jsonify({
        "status": "healthy",
        "version": "1.0.5",
        "timestamp": datetime.now().isoformat(),
        "service": "maldonado-cicd"
    })

@app.route('/api/analyze', methods=['POST'])
def analyze():
    """Endpoint API para análisis de sentimiento"""
    try:
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({"error": "Se requiere el campo 'text'"}), 400
        
        text = data['text']
        
        if not text.strip():
            return jsonify({"error": "El texto no puede estar vacío"}), 400
        
        result = ai_model.generate_response(text)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/info')
def info():
    """Información del proyecto"""
    return jsonify({
        "project": "CI/CD Flask con IA",
        "student": "Alejandro Maldonado",
        "version": "1.0.5",
        "features": [
            "Análisis de sentimientos con IA",
            "Pipeline CI/CD automatizado",
            "Tests automatizados",
            "Despliegue automático a VPS",
            "Publicación en GitHub Packages"
        ],
        "endpoints": {
            "/": "Interfaz web",
            "/health": "Health check",
            "/api/analyze": "Análisis de sentimiento (POST)",
            "/info": "Información del proyecto"
        }
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)