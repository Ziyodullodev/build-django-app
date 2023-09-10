starting project

## 1. Clone project

``` 
git clone project-link.git
```

## 2. Install dependencies

```
cd project-name
virtualenv venv
source venv/bin/activate
```

## 3. Docker build

```
docker-compose build
```

## 4. Run project

```
docker-compose up
```

## Additional

```
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser
```

## Enter docker bash

```
docker exec -it project-name_web_1 bash
docker compose exec web bash
```
