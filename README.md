Statuscast
==========
Cast status of a script with a nice simple look.
Cast nice looking status messages for your script tasks.

Goal and Philosophy
-------------------
**Statuscast** originally made for private use cases, but why not share it? 🍰
First public python package made by me. Contribution, bug fixes and feature requests are welcome.

Table of Contents
-----------------

1. [Documentation](#documentation)

   1. [Installation](#installation)
   2. [Examples](#examples)
   3. [Quickstart](#quickstart)

2. [License](#license)

Documentation
-------------

Installation
------------
``` {.sourceCode .bash}
$ pip install statuscast
```

Quickstart
----------
``` {python}
from statuscast import Cast
import time

task = Cast('Do something')
# Stuff
time.sleep(2)
task.complete()
```
Outputs:
![Alt Text](https://raw.githubusercontent.com/DigitalArc/statuscast/master/docs/quick_start.gif)

Examples
--------
- [simple_task.py](./docs/examples/simple_task.py)
- [simple_task_with_info.py](./docs/examples/simple_task_with_info.py)
- [simple_task_with_errors.py](./docs/examples/simple_task_with_errors.py)
- [advanced_task_with_errors.py](./docs/examples/advanced_task_with_errors.py)

License
-------
Copyright (c) 2018 DigitalArc (twitter: @thedigitalarc)

Licensed under the MIT license.