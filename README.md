# Mysibsau backend
Серверная часть приложений "Мой СибГУ".  

## Структура проекта
- Каталог `src/` хранит в себе все исходники, о них позже;  
- `.env.example` - файл с переменными окружения, нужно переименовать в `.env`;  
- `fabfile.py` - скрипты для деплой при помощи fabric;  
- `gunicorn.service` и `nginx.conf` - конфиги для guincorn и nginx соответственно;  
- `Pipfile` и `Pipfile.lock` - список зависимостей, сформированный при помощи pipenv;  
- `.flake8` - настройки для flake8;  

Остальные файлы, на мой взгляд, не нуждаются в описании.

## Структура исходников
Все исходники лежат в папке `src/`. Она состоит из следющих каталогов:  
- `apps/` - все приложения:
    - `campus_sibsau/` - приложение, содержащее в себе различную статичную информацию о ВУЗе;  
    - `informing/` - приложение, отвечающее за информирование (новости, мероприятия, пуш уведомления);  
    - `support/` - помощь студентам;  
    - `surveys/` - опросы;  
    - `timetable/` - расписание.  
- `core/` - настройки проекта;  
- `logs/` - логи приложений;  
- `resources/` - медиа, статика и шаблоны проекта;  
- `tests/` - тесты для приложений;  
- `manage.py` - если вы не знаете что это, пожалуйста, не трогайте этот проект.

## Описание переменных окружения (.env)
`DEBUG` - включен режим отладки или нет;  
`SECRET_KEY` - секретный ключ django;  
`ADMIN_URL` - адрес по которому находится панель администратора;  

Настройки БД:  
- `DATABASE_HOST` - адрес базы данных;  
- `DATABASE_PORT` - порт базы данных;  
- `DATABASE_NAME` - название базы;  
- `DATABASE_USER` - пользователь, у которого есть доступ к этой базе;  
- `DATABASE_PASSWORD` - пароль этого пользователя.  

`SENTRY` - включено ли sentry;  
`DSN` - токен sentry;

`TG_TOKEN` - токен от telegram, нужен для отправки ошибок в лс;
`TG_DELVELOPER` - кому отправлять ошибки

Конфиги для деплоя:  
- `SERVER` - куда деплоить;  
- `SERVER_PORT` - порт SSH;  
- `SERVER_PASSWORD` - пароль суперюзера;  
- `SERVER_PATH` - папка в которую грузить исходники

## Описание структуры приложений:
Как правило, все приложения имеют следующую структуру:
- `api/` - папка для работы api:
    - `docs.py` - документация API методов для swager; 
    - `serializers.py` - сериалайзеры для моделек;  
    - `urls.py` - урлы для контроллеров;  
    - `views.py` - контроллеры.  
- `migrations/` - миграции приложения;  
- `services/` - сервисный слой;  
- `admin.py` - регистрация моделек в админке;  
- `apps.py` - настройки приложения;  
- `models.py` - модельки.  

## Пяснение за говнокод:
### Свои сериалайзеры
Мы хостились на сервере за 89 рублей в месяц, оперативы мало, проц слабенький. Когда прилетало по 10к запросов в день, сервер начинал задыхаться. Было обнаружено, что самым узким местом являются сериалайзеры из `DRF`. Поэтому переписал их на самый быстрый вариант.  

### Документация пишется руками?
`drf_yasg` умеет генерировать документацию только из сериалайзеров `DRF`, однако у нас ведь кастомные. Вот и приходится писать все руками.

### Мало тестов
Да, каюсь. Но момент упущен. Однако я постараюсь покрыть все покрыть хотя бы дымными тестами.