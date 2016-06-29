# daily-yoda
Python module for producing a yoda quote of the day

## Usage

```python
$ python
>>> import dailyyoda
>>> dy = dailyyoda.dailyyoda('yoda')
>>> dy.get_quote('today')
'Do. Or do not. There is no try.'
>>> quit()
```

`get_quote()` accepts various date strings and formats.  For example:
 * 1977-5-25
 * May 25, 1977
 * 5/25/1977
 * yesterday
 * today
 * tomorrow

## testing

The tests directory has a suite of comprehensive tests for dailyyoda

```bash
$ cd tests
$ python test_dailyyoda.py
......
----------------------------------------------------------------------
Ran 6 tests in 0.004s

OK
$ echo $?
0
```

## installation

```bash
sudo python setup.py install
```

_note: quotes.db is built when setup is run

## removal

```bash
sudo pip uninstall dailyyoda==0.1.0
```

_tip: use `$ pip freeze | grep dailyyoda` to discover installed version._


