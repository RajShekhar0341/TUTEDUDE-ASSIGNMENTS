# Global Constants
# Application Configuration
APP_NAME = "TUTEDUDE"
APP_VERSION = "1.0.0"
DEBUG_MODE = True

# Database Configuration
DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "tutedude_db"
DB_USER = "admin"
DB_PASSWORD = "password"

# API Configuration
API_BASE_URL = "http://localhost:8000"
API_TIMEOUT = 30
MAX_RETRIES = 3

# File Paths
LOG_DIR = "./logs"
DATA_DIR = "./data"
CONFIG_DIR = "./config"

# Error Messages
ERROR_CONNECTION_FAILED = "Failed to establish connection"
ERROR_INVALID_INPUT = "Invalid input provided"
ERROR_NOT_FOUND = "Resource not found"

# Status Codes
STATUS_SUCCESS = 200
STATUS_BAD_REQUEST = 400
STATUS_NOT_FOUND = 404
STATUS_SERVER_ERROR = 500