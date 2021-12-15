# Testing_instruments
### Issue_1
Тестирование функции, кодирующей строку в соответсвии с таблицей азбуки Морзе, с помощью doctest.\
#### Описание шагов для запуска:
Запуск тестов из командной строки 
```python
$ python -m doctest test_issue_1.py
```
Чтобы прошел второй тест модифицируем поведение doctest с помощью флага -o NORMALIZE_WHITESPACE
```python
$ python -m doctest -v -o NORMALIZE_WHITESPACE test_issue_1.py
```
### Issue_2
Тестирование функции, декодирующей строку из азбуки Морзе в английский, с помощью параметрического pytest.\
#### Описание шагов для запуска:
Запуск тестов из командной строки
```python
$ pytest test_issue_2
```
Запуск конкретного теста test_decode
```python
$ python -m pytest test_issue_2.py::test_decode
```
### Issue_3
Тестирование функции, кодирующей значения в бинарное представление, с помощью unittest.\
#### Описание шагов для запуска:
Запуск всех тестов из командной строки 
```python
$ python -m unittest test_issue_3.py
```
Запуск 1 конкретного теста test_ft
```
$ python -m unittest test_issue_3.TestOneHotEncoder.test_ft
```
### Issue_4
Тестирование функции, кодирующей значения в бинарное представление, с помощью pytest.\
#### Описание шагов для запуска:
Запуск всех тестов из командной строки
```python
$ pytest test_issue_4.py
```
### Issue_5
Тестирование функции, возвращающей текущий год.
#### Описание шагов для запуска:
Запуск всех тестов из командной строки
```python
$ pytest test_issue_5.py
```
Проверяем, что мы покрыли нашими тестами 100% кода, с помощью coverage
```python
$ pip install coverage
$ pip install pytest-cov
$ python -m pytest --cov .
```
Формируем HTML отчет по покрытию
```python
$ python -m pytest --cov . --cov-report html
```
Ссылка на отчёт: 
http://localhost:63342/AAA_python_tests/htmlcov/test_issue_5_py.html?_ijt=vmap2iuqhlkro70loamu62i71j

