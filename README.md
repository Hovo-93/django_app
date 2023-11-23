 ### Список технологий: Python, Django, DRF, Celery, Redis, Docker,Flower
 
## Подготовка и запуск проекта
#### Проверьте установлен ли у вас Docker
Прежде, чем приступать к работе, необходимо знать, что Docker установлен. Для этого достаточно ввести:
```bash
docker -v
```
Или скачайте [Docker Desktop](https://www.docker.com/products/docker-desktop) для Mac или Windows. [Docker Compose](https://docs.docker.com/compose) будет установлен автоматически. В Linux убедитесь, что у вас установлена последняя версия [Compose](https://docs.docker.com/compose/install/). Также вы можете воспользоваться официальной [инструкцией](https://docs.docker.com/engine/install/).

#### Шаг 1. Клонируйте репозиторий себе на компьютер
Введите команду:
```bash
git clone https://github.com/Hovo-93/django_app.git
```
#### Шаг 2. Создайте в клонированной директории файл .env можете попросить у меня 
Пример:
```bash

CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/0
EMAIL_HOST_USER=example@gmail.com
EMAIL_HOST_PASSWORD=qrzatthdijcvvyvisefs
FROM_EMAIL=ovo.aroyan@gmail.com

```

#### Шаг 3. Для пересборки и запуска контейнеров
```bash
    docker-compose up --build -d 

```

## Примеры
Для формирования запросов и ответов использована программа [Postman](https://www.postman.com/).
### 1. Получения списка всех книг
GET http://localhost:8000/book

### 2.Создания новой книги.
POST http://localhost:8000/book

### 3.Получения информации о конкретной книге.
GET http://localhost:8000/book/id/

### 4.Обновления информации о книге
PUT http://localhost:8000/book/id/

### 5.Удаления книги
DELETE http://localhost:8000/book/id/

### 6.Регистрация нового пользователя
POST http://localhost:8000/register/
```json
{
  "username": "Имя",
  "email": "Емайл"
}
```

