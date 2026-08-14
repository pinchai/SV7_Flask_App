import os

from werkzeug.utils import secure_filename

UPLOAD_DIR = os.path.join("static", "images")
os.makedirs(UPLOAD_DIR, exist_ok=True)

ALLOWED_EXT = {"png", "jpg", "jpeg", "gif"}


def allowed(name):
    return "." in name and name.rsplit(".", 1)[-1].lower() in ALLOWED_EXT


def upload_image(file, old_name=''):
    """Upload image to directory"""
    try:
        if file and allowed(file.filename):
            if old_name.strip() != '':
                filename = old_name
            else:
                filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_DIR, filename))
            return filename
    except ImportError as error:
        return f"error message: {error}"


def delete_image(file_name: str):
    """Delete image from directory"""
    try:
        image_path = os.path.join(UPLOAD_DIR, file_name)
        if os.path.exists(image_path):
            os.remove(image_path)
            return True
        else:
            return False
    except ImportError as error:
        return f"error message: {error}"
