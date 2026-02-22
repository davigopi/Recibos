@echo off
chcp 65001 >nul
setlocal EnableDelayedExpansion

REM ===== VERIFICAR CONFIG GLOBAL DO GIT =====
for /f "delims=" %%A in ('git config --global user.name') do set GIT_NAME=%%A
for /f "delims=" %%A in ('git config --global user.email') do set GIT_EMAIL=%%A

echo ================================
echo   CONFIGURACAO GLOBAL DO GIT
echo ================================

if defined GIT_NAME (
    echo Usuario atual: !GIT_NAME!
    echo Email atual:   !GIT_EMAIL!
    echo.
    set /p TROCAR="Deseja alterar? S/N: "

    if /I "!TROCAR!"=="S" (
        echo.
        echo Exemplo:
        echo Usuario: davigopi
        echo Email:   davigopi@gmail.com
        echo.
        set /p NOVO_NOME="Digite o novo user.name: "
        set /p NOVO_EMAIL="Digite o novo user.email: "

        git config --global user.name "!NOVO_NOME!"
        git config --global user.email "!NOVO_EMAIL!"

        set GIT_NAME=!NOVO_NOME!

        echo Configuracao atualizada com sucesso.
        echo.
    ) else (
        echo Mantendo configuracao atual.
        echo.
    )
) else (
    echo Git ainda nao esta configurado globalmente.
    echo.
    echo Exemplo:
    echo Usuario: davigopi
    echo Email:   davigopi@gmail.com
    echo.
    set /p NOVO_NOME="Digite o user.name: "
    set /p NOVO_EMAIL="Digite o user.email: "

    git config --global user.name "!NOVO_NOME!"
    git config --global user.email "!NOVO_EMAIL!"

    set GIT_NAME=!NOVO_NOME!

    echo Configuracao aplicada com sucesso.
    echo.
)

REM ===== PEGAR NOME DA PASTA =====
for %%I in (.) do set PROJETO_LOCAL=%%~nxI

echo Projeto local detectado: %PROJETO_LOCAL%
echo.

REM ===== PEDIR NOME DO PROJETO NO GITHUB =====
set /p PROJETO_GITHUB="Digite o nome do projeto no GitHub (Enter para usar %PROJETO_LOCAL%): "

if "%PROJETO_GITHUB%"=="" (
    set PROJETO=%PROJETO_LOCAL%
) else (
    set PROJETO=%PROJETO_GITHUB%
)

REM ===== CONFIGURACOES =====
set BRANCH=main
set REMOTE=origin
set COMMIT_MSG=Atualizacao automatica
set REPO_URL=https://github.com/!GIT_NAME!/%PROJETO%.git

echo.
echo Projeto que sera usado: %PROJETO%
echo Repositorio: %REPO_URL%
echo.

REM ===== VERIFICAR SE E UM REPOSITORIO GIT =====
if not exist ".git" (
    echo Repositorio Git nao encontrado. Inicializando...
    git init
    git branch -M %BRANCH%
    git remote add %REMOTE% %REPO_URL%
) else (
    REM Se ja existir remote, atualiza automaticamente
    git remote set-url %REMOTE% %REPO_URL% >nul 2>&1
)

REM ===== VERIFICAR SE EXISTEM ALTERACOES =====
git add .

git diff --cached --quiet
if %errorlevel%==0 (
    echo Nenhuma alteracao para commit.
) else (
    git commit -m "%COMMIT_MSG%"
)

REM ===== PUSH =====
git push -u %REMOTE% %BRANCH%

echo.
echo Upload concluido com sucesso!
pause