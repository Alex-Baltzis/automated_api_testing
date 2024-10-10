# Automated Api Testing

A brief description of your project. Explain what it does and what its purpose is.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Prerequisites](#prerequisites)
3. [Project Setup Instructions](#project-setup-instructions)
   - [1. Clone the repository](#1-clone-the-repository)
   - [2. Set up the Python virtual environment](#2-set-up-the-python-virtual-environment)
   - [3. Activate the virtual environment](#3-activate-the-virtual-environment)
   - [4. Install dependencies](#4-install-dependencies)
   - [5. Run the project](#5-run-the-project)
4. [Test report](#Test-report)

---

## Project Overview

This project aims to test an API through automated testing procedures. 
The API used is a mocked one by https://fakerestapi.azurewebsites.net/index.html
A user has the ability to selectively locally run the tests (using something like Python Test Explorer for Visual Studio Code) or batch run them using the pytest command in the main project directory.  

> [!WARNING]
> Whenever one would like to batch run the tests locally using the `pytest` command  
it is advisable to have to `pytest.ini` in the directory. But when one wants to  
selectively run tests using the before mentioned Python Test Explorer for Visual Studio Code  
he/she has to remove the `pytest.ini` from the directory because it somehow inteferes with  
the execution of the extension.

An automated CI logic has also been implemented. Every time something is pushed or merged into the origin/master branch an action is triggered, the tests run and a report is produced as an artifact, giving detailed overview to the user how his/her commits affected the project. 

### Structure
1. All the tests ofthe project exists within the `test_api` folder.  
A subdirectory for each topic exists and then a .py for rach endpoint containing  
all the corresponding testcases of the later one.  

2. Helping classes are contained within the `utils` folder.   
    - __ApiClient__ helping constructing all the http comands
    - __Book__ helping constructing and comparing book related responses
    - __Author__ helping constructing and comparing author related responses
    
3. The report generated files exists in `report`  
4. Any needed settings in `config`--> `settings.py`. For the time being, only the base url of the API under testing is set up there

---

## Prerequisites

Before setting up the project, make sure you have the following tools installed:

- Python >=3.8 ([Download here](https://www.python.org/downloads/))
- Git ([Download here](https://git-scm.com/downloads))
- A method of creating a virtual env such as `virtualenv`(optional) or the native method  
  with python `python -m venv <myenvname>`
- All the other prerequisites will be installed in the venv through the `requirements.txt`

---

## Project Setup Instructions

Follow the steps below to set up the project on your local machine:

### 1. Clone the repository

Go to your desired location

```
cd <desired_path>
```

Clone the project from the GitHub repository:

```bash
git clone https://github.com/Alex-Baltzis/automated_api_testing.git
cd automated_api_testing
```

### 2. Set up the Python virtual environment

Set up a virtual environment to isolate the project’s dependencies. This helps avoid conflicts between dependencies of different projects. 2 ways possible
```
pip install virtualenv
virtualenv env_name
```
or
```
python -m venv env_name
```

### 3. Activate the virtual environment
Activate the virtual environment
```
cd .\venv\Scripts
activate
```

### 4. Install dependencies
With the virtual environment activated, install the required dependencies using  
`requirements.txt`. You have to navigate to the main project directory (/automated_api_testing)
```
cd ..
cd ..
pip install -r requirements.txt
```

### 5. Run the project
Once everything is set up, you can run the project or the tests as needed. By being in the main  
project directory, type
```
# Running pytest for the tests
pytest
```
Make sure to deactivate the virtual environment once you're done by running:
```
deactivate
```

---

## Test report

Once the tests have run, an automated report (pytest_html_report.html) will be generated within the  
/report folder. By opening that, one can see the results of the run.    

<figure>
  <img src="https://pbs.twimg.com/media/EhAJhF-X0AABPp_.jpg:large" alt="Image description">
  <figcaption>This is a sample image.</figcaption>
</figure>

### CI

As previously mentioned very time something is pushed or merged into the origin/master branch an action is triggered, the tests run and a report is produced as an artifact, giving detailed overview to the user how his/her commits affected the project.

One could check the artifact by  
- Going to the Actions  
- Click on a desired action
- at the end there will be the pytest-html-report.html artifact

