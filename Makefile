VENV_DIRNAME = venv

ifeq ($(OS), Windows_NT)
RMDIR_CMD=rd /s /q
RM_CMD=del
RUN_EXEC=powershell .\run.ps1
ACTIVATE_VENV=.\$(VENV_DIRNAME)\Scripts\activate.bat
else
RMDIR_CMD=rm -rf
RM_CMD=rm -rf
RUN_EXEC=./run.sh
ACTIVATE_VENV=source ./$(VENV_DIRNAME)/bin/activate
endif

all: start

start: $(RUN_EXEC)

clear_env:
    $(RMDIR_CMD) $(VENV_DIRNAME)

venv:
    python3 -m venv $(VENV_DIRNAME)
    $(ACTIVATE_VENV)


install:
    pip3 install -r requirements.txt


.PHONY: all
