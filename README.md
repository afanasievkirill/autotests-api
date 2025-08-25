# autotests-api

<a id="markdown-описание" name="Предварительные настройки."></a>

## Предварительные настройки.

Подготовить виртуальное окружение Python.

```
$ python -m venv venv
```

Активировать виртуальное окружение Python.

```
$ .\\venv\Scripts\activate
```

Установить зависимости.

```
$ pip install -r requirements.txt
```

<a id="markdown-описание" name="Запуск тестов."></a>

## Запуск тестов.

```
python -m pytest -k "test_authentication" -s -v

python -m pytest -m "regression" --numprocesses=2

```


