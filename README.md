![yamdb workflow](https://github.com/Pavel-Maksimov/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
# REST-API-Yatube
Yamdb - это  база данных с отзывами пользователей о фильмах, книгах, музыке.<br>
Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Список категорий может быть расширен администратором.<br>
Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.<br>
В каждой категории есть произведения: книги, фильмы или музыка.<br>
Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). Новые жанры может создавать только администратор.
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.
________
## Пользовательские роли <br>
Аноним — может просматривать описания произведений, читать отзывы и комментарии. <br>
Аутентифицированный пользователь (user) — может читать всё, как и Аноним, может публиковать отзывы и ставить оценки произведениям (фильмам/книгам/песенкам), может комментировать отзывы; может редактировать и удалять свои отзывы и комментарии, редактировать свои оценки произведений. Эта роль присваивается по умолчанию каждому новому пользователю.<br>
Модератор (moderator) — те же права, что и у Аутентифицированного пользователя, плюс право удалять и редактировать любые отзывы и комментарии.<br>
Администратор (admin) — полные права на управление всем контентом проекта. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.<br>
### Самостоятельная регистрация новых пользователей<br>
Пользователь отправляет POST-запрос с параметрами email и username на эндпоинт /api/v1/auth/signup/.<br>
Сервис YaMDB отправляет письмо с кодом подтверждения (confirmation_code) на указанный адрес email.<br>
Пользователь отправляет POST-запрос с параметрами username и confirmation_code на эндпоинт /api/v1/auth/token/, в ответе на запрос ему приходит token (JWT-токен).<br>
В результате пользователь получает токен и может работать с API проекта, отправляя этот токен с каждым запросом.<br>
После регистрации и получения токена пользователь может отправить PATCH-запрос на эндпоинт /api/v1/users/me/ и заполнить поля в своём профайле (описание полей — в документации).<br>
### Создание пользователя администратором<br>
Пользователя может создать администратор — через админ-зону сайта или через POST-запрос на специальный эндпоинт api/v1/users/ (описание полей запроса для этого случая — в документации). В этот момент письмо с кодом подтверждения пользователю отправлять не нужно.
После этого пользователь должен самостоятельно отправить свой email и username на эндпоинт<br> ***/api/v1/auth/signup/*** ,<br> в ответ ему должно прийти письмо с кодом подтверждения.
Далее пользователь отправляет POST-запрос с параметрами username и confirmation_code на эндпоинт ***/api/v1/auth/token/***, в ответе на запрос ему приходит token (JWT-токен), как и при самостоятельной регистрации.<br>
### Ресурсы API YaMDb<br>
В текущей версии проекта обращение к ресурсам производится через путь ***<домен>/api/v1/<ресурс>***. <br>
Ресурсы:<br>
***/auth***: аутентификация.<br>
***/users***: пользователи.<br>
***/titles***: произведения, к которым пишут отзывы (определённый фильм, книга или песенка).<br>
***/categories***: категории (типы) произведений («Фильмы», «Книги», «Музыка»).<br>
***/genres***: жанры произведений. Одно произведение может быть привязано к нескольким жанрам.<br>
***/reviews***: отзывы на произведения. Отзыв привязан к определённому произведению.<br>
***/comments***: комментарии к отзывам. Комментарий привязан к определённому отзыву.<br>
### Стек технологий<br> 
Python3, Django 3.0, Simple JWT, PostgreSQL, Git, Pytest.
<br><br>

### Развёртывание проекта <br>
Развёртывание проекта предполагается в контейнере Docker 
(инструкция по установке: https://docs.docker.com/engine/install/). <br>
Для развёртывания проекта выполните следующие действия:<br>
Клонируйте репозиторий:
```
git clone https://github.com/Pavel-Maksimov/yamdb_final.git
```
Находясь в корневой папке проекта, выполните команду:
```
$ docker-compose up -d
```

Создайте и примените миграции:
```
$ docker-compose run web python manage.py makemigrations
$ docker-compose run web python manage.py migrate
```
Для сбора статики выполните команду:
```
$ docker-compose run web python manage.py collectstatic
```
Сервер будет доступен на хосте http://127.0.0.1/. <br>
Для создания суперюзера выполните команду:
```
$ docker-compose exec web python manage.py createsuperuser
```
Для заполнения базы данных начальными данными выполните команду:
```
$ docker exec -it <container_id> python manage.py shell
>>> from django.contrib.contenttypes.models import ContentType
>>> ContentType.objects.all().delete()
>>> quit()

$ docker exec -it <container_id> python manage.py loaddata fixtures.json
```

Для останова сервера выполните команду:
```
$ docker-compose down
```
Посмотреть работу проекта можно по ссылкам:<br>
***http://pavelmaksimov.co.vu/redoc/***<br>
 ***http://pavelmaksimov.co.vu/admin/*** <br>
***http://pavelmaksimov.co.vu/api/v1/users/***<br>
***http://pavelmaksimov.co.vu/api/v1/titles/***<br>
***http://pavelmaksimov.co.vu/api/v1/categories/***<br>
***http://pavelmaksimov.co.vu/api/v1/genres/***<br>
***http://pavelmaksimov.co.vu/api/v1/titles/1/reviews/***<br>
***http://pavelmaksimov.co.vu/api/v1/titles/2/reviews/***<br>
***http://pavelmaksimov.co.vu/api/v1/titles/2/reviews/1/comments/***<br>
***http://pavelmaksimov.co.vu/api/v1/titles/1/reviews/2/comments/***<br>

