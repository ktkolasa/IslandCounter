To build docker image and run the script within type:

> ./build_run_island_counter.sh <input_file.txt>

To run the script:

> ./run_island_counter.sh <input_file.txt>

Alternatively you can use the Makefile to build image from Dockerfile:
> make build
---

The input_file.txt should consist of an array of 1 and 0, eg:

0000100<br>
1000100<br>
1100000<br>
---
Ways to run tests:
1. Uncomment line
>#RUN pytest
> 
in Dockerfile. Tests will be run during build.

2. Setup and activate python virtual env and run there
>pytest

or
>make test
3. To run full suite of tests including the ones tagged as long-running (memory-consuming), run:
> pytest --longrun


---
Files to be used for testing/development purposes:
- dev_reqirements.txt -- to setup dev env

- Makefile -- to support formatting and testing

