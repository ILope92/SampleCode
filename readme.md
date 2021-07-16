# Sample code
[![GitHub license](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](https://github.com/ILope92/SampleCode/blob/master/LICENSE)

Проект подразумевает под собой некоторый функционал, и основан на предпочтениях в функционале потенциальных работадателей (Тестовых заданий / задач фриланса). Возможны дополнения в функционале.
## Оглавление
- [Описание проекта](#description)
    - [Worker](#worker)
    - [Endpoints](#endpoints)
    - [Возможности](#opportunities)
- [Развернуть приложение](#deploy)
    - [Docker-compose](#docker)
    - [Запуск проекта](#start)
    - [Миграция Alembic](#alembic)
- [Подготовка к разработке](#dev)

<a name="description"></a>
## 1. Описание проекта
<a name="worker"></a>
## 1.1 Worker
На данном этапе, реализована малая часть функционала Backend части проекта. Реализован работающий в фоновом режиме Worker, задача которого рассматривать изменения в локальных файлах или нахождение новых файлов формата .csv в определённой папке.

После нахождения нового файла, либо изменения в нём, воркер сверяется с базой данных, и если есть новые данные - добавит их в базу. После чего будет снова ждать изменений.

<hr>
<a name="endpoints"></a>

## 1.2 Endpoints

Конечные точки предоставляют данные в нужном его виде для различных целей. Данные в этом проекте тестовые и представляют собой набор постов из социальной сети. Нужный вид возвращаемых данных был указан в моём техническом задании.
В проекте реализовано два метода для работы с базой:

- [/delete_post]() - Удаление поста используя уникальный идентификатор базы данных
- [/find_post]() - Поиск текста в постах. Возвращает последние 20 постов, отсортированные по дате создания.

<hr>
<a name="opportunities"></a>

## 1.3 Возможные улучшения
Данный список улучшений кажеться мне уместным на основе полученных данных из социальной сети ВКонтакте. Они не обязательно окажуться здесь, но приняты во внимание.
- Добавление пользователей и прав на получение данных
- JWT Authentication
- Выбор статичных файлов для Worker. Обновление данных в статичных файлах приведут к обновлению данных в базе, если только не был добавлен новый элемент.
- Добавление endpoint для редактирования данных.
- Изменение endpoint - [/delete_post](). Удаление по списку.
- Проверка постов на грамматические ошибки с помощью [PyEnchant]
<hr>

## 2. Развернуть приложение


### 2.1 Docker-compose
<a name="deploy"></a>

Сборка проекта внутри Docker контейнера
```bash
~ docker-compose build
```
<hr>

### 2.2 Запуск проекта
<a name="start"></a>
```bash
~ docker-compose up
or
~ make compose
```
<hr>

### 2.3 Миграция Alembic
<a name="alembic"></a>

Применение миграции c Python. Перейдите в корневую папку проекта.
```bash
~ python backend/utils/migrate upgrade head
```
По умолчанию он выберет адрес базы из .env.backend. Для применения миграции на другой адрес базы просто измените его:
```bash
~ python backend/utils/migrate --pg-url postgresql://admin:admin@0.0.0.0:5432/namedb upgrade head
```
<hr>
<a name="dev"></a>

### 3. Подготовка к разработке

### Linux
```bash
~ make devenv
~ source env/bin/activate
(env) docker-compose run -d -p 5432:5432 --name database-notion db / make db
(env) python -m alembic upgrade head / make migrate
(env) python -m uvicorn main:app / make app
or
(env) docker-compose run -d -p 3000:8000 --name application-notion app
```
#### Windows
```bash
~ python -m venv env
~ .\env\Scripts\activate
(env) python -m pip install pip --upgrade
(env) python -m pip install -r requirements.txt
(env) docker-compose run -d -p 5432:5432 --name database-notion db
(env) python -m alembic upgrade head
(env) python -m uvicorn main:app
or
(env) docker-compose run -d -p 3000:8000 --name application-notion app
```
Данные команды установят виртуальное окружение, запустят базу данных в контейнере Docker, применится миграция, и установят все необходимые зависимости.

### API документация
http://127.0.0.1:3000/api/docs/
http://127.0.0.1:3000/api/redocs/
