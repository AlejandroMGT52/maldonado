import unittest
import json
from app import app, SimpleAI

class TestFlaskApp(unittest.TestCase):
    """Tests para la aplicación Flask"""
    
    def setUp(self):
        """Configuración antes de cada test"""
        self.app = app.test_client()
        self.app.testing = True
    
    def test_health_endpoint(self):
        """Test del endpoint de salud"""
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'healthy')
        self.assertEqual(data['version'], '1.0.5')
        self.assertIn('timestamp', data)
    
    def test_index_endpoint(self):
        """Test de la página principal"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Analizador de Sentimientos', response.data)
    
    def test_info_endpoint(self):
        """Test del endpoint de información"""
        response = self.app.get('/info')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data['version'], '1.0.5')
        self.assertIn('student', data)
    
    def test_analyze_positive_sentiment(self):
        """Test de análisis de sentimiento positivo"""
        response = self.app.post('/api/analyze',
                                  data=json.dumps({'text': 'Este proyecto es excelente y genial'}),
                                  content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['sentiment'], 'positivo')
        self.assertIn('confidence', data)
        self.assertIn('response', data)
    
    def test_analyze_negative_sentiment(self):
        """Test de análisis de sentimiento negativo"""
        response = self.app.post('/api/analyze',
                                  data=json.dumps({'text': 'Esto es terrible y malo'}),
                                  content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['sentiment'], 'negativo')
    
    def test_analyze_neutral_sentiment(self):
        """Test de análisis de sentimiento neutral"""
        response = self.app.post('/api/analyze',
                                  data=json.dumps({'text': 'El clima está nublado'}),
                                  content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['sentiment'], 'neutral')
    
    def test_analyze_empty_text(self):
        """Test con texto vacío"""
        response = self.app.post('/api/analyze',
                                  data=json.dumps({'text': ''}),
                                  content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('error', data)
    
    def test_analyze_missing_text(self):
        """Test sin campo text"""
        response = self.app.post('/api/analyze',
                                  data=json.dumps({}),
                                  content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('error', data)

class TestSimpleAI(unittest.TestCase):
    """Tests para el modelo de IA"""
    
    def setUp(self):
        """Configuración antes de cada test"""
        self.ai = SimpleAI()
    
    def test_positive_prediction(self):
        """Test de predicción positiva"""
        sentiment, confidence = self.ai.predict_sentiment("Todo es genial y excelente")
        self.assertEqual(sentiment, "positivo")
        self.assertGreater(confidence, 0)
    
    def test_negative_prediction(self):
        """Test de predicción negativa"""
        sentiment, confidence = self.ai.predict_sentiment("Esto es terrible y malo")
        self.assertEqual(sentiment, "negativo")
        self.assertGreater(confidence, 0)
    
    def test_neutral_prediction(self):
        """Test de predicción neutral"""
        sentiment, confidence = self.ai.predict_sentiment("El día está normal")
        self.assertEqual(sentiment, "neutral")
        self.assertEqual(confidence, 0.5)
    
    def test_generate_response(self):
        """Test de generación de respuesta"""
        result = self.ai.generate_response("Me siento feliz")
        self.assertIn('sentiment', result)
        self.assertIn('confidence', result)
        self.assertIn('response', result)
        self.assertIn('processed_at', result)

if __name__ == '__main__':
    unittest.main()