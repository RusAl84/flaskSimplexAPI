# flaskSimplexAPI - API для решения задач симплекс методом

## Запрос посылать сюда:
```http://127.0.0.1:5000/api/optimize```

## Тело запроса POST в формате JSON

```{"z": [6, 1, 5], "rests": [[7, 17, 17, 242], [16, 5, 1, 329], [18, 3, 3, 325]]}```

## Ответ в формате строка текста:

**x1 = 16.838596, x2 = 0.0, x3 = 7.3017544, Z = 137.540348**