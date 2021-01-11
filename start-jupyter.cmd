@ECHO OFF

SETLOCAL

:: Set to true for notebook, or anything else for lab.
SET use_notebook=false



SET cmd=
if [%use_notebook%] == [true] (
    SET cmd=jupyter notebook
) ELSE (
    SET cmd=jupyter lab
)

%cmd%