### Factorial (Technical Assignment)

Author: Dylan Muller <br>
Date Received: 20/01/2022 <br>
Date Completed : 21/01/2022 <br>

The following repository contains a docker build directory for the solution to the Corigine technical assignment. It consists of the following files:
* solution.py - The python 3 solution file
* build.sh - Script to build the docker container
* Dockerfile - The docker build file
* README.md - Documentation file

The solution was required to adhere to the following constraints:
1. Use Python3 - **Done**
2. Use numpy for math operations - **All math operations used numpy**
3. Avoid casting variables - **None casted**
4. Follow good programming practice - **The solution was implemented with good practices in mind**
5. Provide a compressed tarball of the docker build directory - **Done**
6. Implement multithreading - **Done***

### Instructions

Download this repository and then mark **build.sh** as executable: 
* $ chmod +x build.sh. 
After running the shell script a docker container with the tag: **factorial-digits** will be created. You can then run the solution with the following command: 
* $ sudo docker run --rm factorial-digits 100