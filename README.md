# stepic_autotest_part4
tests for http://selenium1py.pythonanywhere.com/

Сначала все писал в папке venv, но потом понял свою ошибку и вынес все из нее, поэтому последний коммит одинаковый для мноих файлов

Если при запуске тестов возникают проблемы с импортом, типа таких: ImportError: attempted relative import with no known parent package
То попробуйте в строках импорта перед pages добавить точку, например вот так:
from .pages.base_page import BasePage