# AQA Python — SauceDemo Login Tests

## Стек
- Python 3.10
- Pytest
- Playwright
- allure-pytest
- Docker

### Установка
```bash
pip install -r requirements.txt
playwright install
```

### Запуск тестов
```bash
pytest --alluredir=allure-results
```

### Просмотр отчетов
```bash
allure serve allure-results
```

## Запуск в Docker

### Сборка образа
```bash
docker build -t ai-hunt-saucedemo-task .
```

### Запуск контейнера
```
docker run \
  -v $(pwd)/allure-results:/app/allure-results \
  ai-hunt-saucedemo-task
```