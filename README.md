# Wishlist

## Описание

Это небольшое приложение на Flask для ведения списка желаемых покупок.

- Язык: python3.12
- Фреймворк: Flask + SQLAlchemy
- База данных: sqlite
- Контейнеризация: Docker
- Фронт: Bootstrap 5

## Локальный запуск приложения

### С использованием Docker

1. Склонировать репозиторий

```bash
git clone https://github.com/sitdoff/wishlist
```

2. Перейти в папку проекта

```bash
cd wishlist
```

3. Запустить сборку и запуск контейра

```
docker build --tag=sitdoff/wishlist . && docker run -it -p 8000:8000 sitdoff/wishlist
```

4. Приложение будет доступно по http://localhost:8000

### Без использования Docker

1. Склонировать репозиторий

```bash
git clone https://github.com/sitdoff/wishlist
```

2. Перейти в папку проекта

```bash
cd wishlist
```

3. Создать и активировать виртуальное окружение.
4. Установить зависимости в виртуальное окружение.
5. Запустить приложение командой

```bash
flask --app application.main run
```
