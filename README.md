# Человек — просто о сложном

Образовательный сайт на Django: системы органов, карточки о здоровье и поиск.

## Запуск на Windows

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py runserver
```

Открой http://127.0.0.1:8000/ . Для фотографии на главной нужен интернет.

Источники: [MedlinePlus: анатомия](https://medlineplus.gov/anatomy.html), [MedlinePlus: здоровье](https://medlineplus.gov/healthtopics.html), [ВОЗ](https://www.who.int/news-room/fact-sheets/detail/noncommunicable-diseases).

Материалы сайта носят образовательный характер и не заменяют консультацию врача.

## Настройки при размещении в интернете

Для локального учебного запуска Django создаёт временный ключ автоматически. При размещении задай `DJANGO_SECRET_KEY` в переменных окружения сервера, установи `DJANGO_DEBUG=false` и укажи домен в `DJANGO_ALLOWED_HOSTS`. Не публикуй настоящий ключ в GitHub.

### Render

- Build Command: `pip install -r requirements.txt && python manage.py collectstatic --no-input`
- Start Command: `gunicorn human_site.wsgi:application --bind 0.0.0.0:$PORT`
- Environment Variable: `DJANGO_DEBUG=false`

Render автоматически передаёт имя сайта в `RENDER_EXTERNAL_HOSTNAME`; Django добавляет его в разрешённые домены. Для постоянных сессий задай отдельный `DJANGO_SECRET_KEY` в настройках сервиса.
