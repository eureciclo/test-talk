Talk Tests
==========

Talk de testes - eureciclo - 14/12/2023


How to run
----------

First install python 3.11, then:

### Setup virtual env

```
virtualenv .env
source .env/bin/activate
pip install -r requirements.txt
```

### Run Server

```
 ENV=dev PYTHONPATH=$PWD uvicorn controller.main_controller:app --reload --host 0.0.0.0
```

### Tests

```
ENV=test PYTHONPATH=$PWD pytest tests
```

or use docker.
