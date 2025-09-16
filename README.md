# Bootstrap прототипы и простой сервер

## Файлы
- `index.html` — главная
- `catalog.html` — каталог
- `product.html` — карточка товара
- `cart.html` — корзина
- `contacts.html` — контакты
- `server.py` — HTTP-сервер, который на любой GET возвращает `contacts.html`

Bootstrap подключён с CDN.

## Запуск сервера
1. Установите Python 3.10+.
2. В корне проекта выполните:

```bash
python server.py
```

3. Откройте `http://127.0.0.1:8000` в браузере. Любой путь вернёт страницу «Контакты».

## Примечания
- Сервер читает содержимое из `contacts.html` через `with open()` и отправляет с заголовком `Content-type: text/html; charset=utf-8`.
- Для остановки сервера нажмите Ctrl+C в терминале.
