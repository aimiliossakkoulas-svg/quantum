import sys
from pathlib import Path

try:
    from app import create_app
except ImportError:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from __init__ import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
