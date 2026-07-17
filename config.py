import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")


REPORT_FOLDER = os.path.join(BASE_DIR, "reports")

ALLOWED_EXTENSIONS = {"pdf"}


MAX_CONTENT_LENGTH = 10 * 1024 * 1024


SECRET_KEY = "_RESUME_ANALYZER_"