from flask import Flask, jsonify, request
import os
import socket
from datetime import datetime

app = Flask(__name__)

# Configuration from environment variables
VERSION = os.getenv('VERSION', '1.0.0')
ENV = os.getenv('ENV', 'local')

@app.route('/')
def home():
    """Main endpoint - returns app info"""
    return jsonify({
        'message': 'Welcome to my GCP practice app!',
        'version': VERSION,
        'environment': ENV,
        'hostname': socket.gethostname(),
        'timestamp': datetime.now().isoformat()
    })

@app.route('/health')
def health():
    """Health check endpoint (important for Cloud Run)"""
    return jsonify({
        'status': 'healthy',
        'service': 'my-web-app'
    }), 200

@app.route('/echo', methods=['POST'])
def echo():
    """Echo back JSON data - useful for testing"""
    data = request.get_json()
    return jsonify({
        'received': data,
        'processed_at': datetime.now().isoformat()
    })

@app.route('/info')
def info():
    """System information endpoint"""
    return jsonify({
        'python_version': os.sys.version,
        'environment_vars': {
            'PORT': os.getenv('PORT', 'not set'),
            'ENV': ENV,
            'VERSION': VERSION
        }
    })

@app.route('/api/v1/status')
def api_status():
    """API status endpoint"""
    return jsonify({
        'api_version': 'v1',
        'status': 'operational',
        'endpoints': [
            '/',
            '/health',
            '/info',
            '/echo',
            '/api/v1/status'
        ]
    })

if __name__ == '__main__':
    # Cloud Run sets the PORT environment variable
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)
