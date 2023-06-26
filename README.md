# `Algorand`

Micro web application to display a graph of the differences of different search algorithms and use for specific tasks.

___

## *Project Status*

***Completed &#10003;***
___
## Functionality
- [DRF API](https://github.com/Segfaul/algorand/blob/f0023c2ca9e891717626eddc2d32812651cc7654/algorand/api/views.py#L13-L27) for transferring images of comparison graphs of the 3 leading index search algorithms in the sequence
- [Generic view classes](https://github.com/Segfaul/algorand/blob/f0023c2ca9e891717626eddc2d32812651cc7654/algorand/algos/views.py#L13-L41) for showing and checking algorithms
- [Registration/Authentication](https://github.com/Segfaul/algorand/blob/f0023c2ca9e891717626eddc2d32812651cc7654/algorand/algos/views.py#L44-L71) of users via the standard Abastract User model
- [Implementation of search algorithms](https://github.com/Segfaul/algorand/blob/f0023c2ca9e891717626eddc2d32812651cc7654/algorand/algos/algo_dir/algo.py#L11-L131) (*Interpolation, Binary, Fibonacci*) followed by [validation](https://github.com/Segfaul/algorand/blob/f0023c2ca9e891717626eddc2d32812651cc7654/algorand/algos/forms.py#L21-L66)
- [AJAX requests](https://github.com/Segfaul/algorand/blob/f0023c2ca9e891717626eddc2d32812651cc7654/algorand/algos/static/algos/js/ajax.js) for dynamic chart loading, as well as switching between application pages

## Technologies and Frameworks
- Python 3.11 
- Django 4.2.1
- DRF 3.14.0
- AJAX
- HTML, CSS, JS
- SQLite 3
___

## Installation

1. Clone the repository to the local machine

    ```shell
    git clone https://github.com/Segfaul/algorand.git
    ```

2. Go to the repository directory

    ```shell
    cd algorand
    ```

3. Create and activate a virtual environment

    ```shell
    python -m venv env
    source env/bin/activate
    ```

4. Set project dependencies

    ```shell
    pip install -r requirements.txt
    ```

5. Go to the news_editor directory

    ```
    cd algorand
    ```

6. Create database migrations and apply them

    ```python
    python manage.py makemigrations
    python manage.py migrate
    ```

7. Create a Django project superuser (admin)

    ```python
    python manage.py createsuperuser
    ```

9. Run the project on localhost in the background

    ```python
    python manage.py runserver &
    ```

10. In case of a problem, the program will stop automatically or you can stop execution using

    ```shell
    ps aux | grep ".py"
    kill PID
    ```

11. Go to the site and enter the previously created data of the superuser (step 7)

    ```shell
    http://127.0.0.1:8000
    ```

12. In the future you can deploy the project on a remote server

    ```python
    python manage.py runserver 123.123.123.123:8000 &
    ```
___

## Additional Information

Interpolation search is better than binary search under ideal conditions (the elements of a given array are uniformly distributed). However, in cases of non-uniform distribution Binary search preserves asymptotics in **O(log(n))**, while Interpolation loses efficiency up to **O(n)**.
___
