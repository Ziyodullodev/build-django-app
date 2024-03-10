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

## 3. Poetry install dependencies

if you don't have poetry installed, you can install it with the following command:

```
pip install poetry
```

then run the following command:

```
poetry install
```

## 4. Run project

```
docker compose up --build
```