@echo off
setlocal

REM ===== PEGAR NOME DA PASTA (PROJETO) =====
for %%I in (.) do set PROJETO=%%~nxI

REM ===== CONFIGURACOES =====
set BRANCH=main
set REMOTE=origin
set COMMIT_MSG=Atualizacao automatica

REM ===== URL DO REPOSITORIO =====
set REPO_URL=https://github.com/davigopi/%PROJETO%.git

echo Projeto: %PROJETO%
echo Repositorio: %REPO_URL%
echo.

REM ===== VERIFICAR SE E UM REPOSITORIO GIT =====
if not exist ".git" (
    echo Repositorio Git nao encontrado. Inicializando...
    git init
    git branch -M %BRANCH%
    git remote add %REMOTE% %REPO_URL%
)

REM ===== STATUS =====
git status

REM ===== ADICIONAR ARQUIVOS =====
git add .

REM ===== COMMIT =====
git commit -m "%COMMIT_MSG%"

REM ===== PUSH =====
git push -u %REMOTE% %BRANCH%

echo.
echo ✔ Upload concluido com sucesso!
pause