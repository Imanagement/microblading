from django.utils.translation import get_language

def get_path_to_home_page():
    current_language = get_language()
    return '/' if current_language == 'en' else '/es/'