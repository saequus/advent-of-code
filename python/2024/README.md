# Advent Of Code 2024


### Prepare
~~~
$ virtualenv -p python3.12 venv
~~~

### Run

~~~
$ python3 {day# script} {sample_data_file} -t {task_number: one of [1, 2]}

$ python3 day2.py data/day2_test.txt -t 1
> Safe reports number: 2

$ python3 day2.py data/day2_test.txt -t 2
> One-level-down safe reports number: 6
~~~

### Tests

~~~bash
$ PYTHONPATH=. venv/bin/pytest {test_script}

$ PYTHONPATH=. venv/bin/pytest tests/test_day2.py
~~~
