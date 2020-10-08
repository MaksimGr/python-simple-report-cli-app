
# Simple report with CLI

Application parse data in files and print report.

Installation
-----

`$ pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ simple_report_cli`

Usage
-----

`$ simple_report_cli --files path_to_folder` 

Optional parameters:

* `--help`          : Show help message and exit
* `--driver`        : Show driver statistic
* `--asc|desc`      : Order report by driver name

Example
-----

`$ simple_report_cli --files 'D:\report\'`

| N  | DRIVER           | CAR                  | BEST LAP |
|----|------------------|----------------------|----------|
| 1. | Driver 1         | Car 1                | 1:04.415 |
| 2. | Driver 2         | Car 2                | 1:12.434 |
| 3. | ...              | ...                  | ...      |
|----|------------------|----------------------|----------|
| 16.| Driver 16        | Car 16               | 4:13.028 |
| 17.| Driver 17        | Car 17               | 7:12.460 |

License
-------

[MIT License](LICENSE)