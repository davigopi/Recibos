@echo off
chcp 65001 >nul
setlocal EnableDelayedExpansion


REM ===== CRIAR OU SUBSTITUIR .gitignore =====
echo(

if exist ".gitignore" (
    echo .gitignore encontrado. Substituindo...
) else (
    echo .gitignore nao encontrado. Criando...
)

REM Desativar delayed expansion temporariamente
setlocal DisableDelayedExpansion

(
echo # OSX
echo .DS_Store
echo(
echo # Xcode
echo build/
echo *.pbxuser
echo !default.pbxuser
echo *.mode1v3
echo !default.mode1v3
echo *.mode2v3
echo !default.mode2v3
echo *.perspectivev3
echo !default.perspectivev3
echo xcuserdata
echo *.xccheckout
echo *.moved-aside
echo DerivedData
echo *.hmap
echo *.ipa
echo *.xcuserstate
echo **/.xcode.env.local
echo(
echo # Android/IntelliJ
echo build/
echo .idea
echo .gradle
echo local.properties
echo *.iml
echo *.hprof
echo .cxx/
echo *.keystore
echo !debug.keystore
echo .kotlin/
echo(
echo # node.js
echo node_modules/
echo npm-debug.log
echo yarn-error.log
echo(
echo # fastlane
echo **/fastlane/report.xml
echo **/fastlane/Preview.html
echo **/fastlane/screenshots
echo **/fastlane/test_output
echo(
echo # Bundle artifact
echo *.jsbundle
echo(
echo # Ruby / CocoaPods
echo **/Pods/
echo /vendor/bundle/
echo(
echo # Metro temporary files
echo .metro-health-check*
echo(
echo # testing
echo /coverage
echo(
echo # Yarn
echo .yarn/*
echo !.yarn/patches
echo !.yarn/plugins
echo !.yarn/releases
echo !.yarn/sdks
echo !.yarn/versions
echo(
echo # IDEs e Editores
echo .vscode/
echo *.swp
echo *.go
echo(
echo # Artefatos de Build do iOS
echo ios/build/
echo ios/DerivedData/
echo(
echo # Python Virtual Environments
echo venv/
echo .venv/
echo env/
echo scripts/pyvenv.cfg
echo(
echo # Variaveis de Ambiente (Seguranca)
echo .env
echo .env.local
echo .env.development.local
echo .env.test.local
echo .env.production.local
echo(
echo # --- Regras adicionais ---
echo Tabelas/bkp/
echo driver/
echo Logs/
echo Old/
echo chromedriver.exe
echo .mypy_cache/
echo __pycache__/
echo *.pyc
echo *.log
echo *.rar
echo senha.txt
echo senha.json
echo config/senha.json
) > .gitignore

endlocal

echo .gitignore atualizado com sucesso.
echo(


REM ===== VERIFICAR CONFIG GLOBAL DO GIT =====
for /f "delims=" %%A in ('git config --global user.name') do set GIT_NAME=%%A
for /f "delims=" %%A in ('git config --global user.email') do set GIT_EMAIL=%%A

echo ================================
echo   CONFIGURACAO GLOBAL DO GIT
echo ================================

if defined GIT_NAME (
    echo Usuario atual: !GIT_NAME!
    echo Email atual:   !GIT_EMAIL!
    echo(
    set /p TROCAR="Deseja alterar o usuário !GIT_NAME! ou o email !GIT_EMAIL! já configurado? (Deixe vazio para não): "

    if /I "!TROCAR!"=="" (
        echo Mantendo configuracao atual.
        echo(
    ) else (
        echo(
        echo Exemplo:
        echo Usuario: davigopi
        echo Email:   davigopi@gmail.com
        echo(
        set /p NOVO_NOME="Digite o novo user.name: "
        set /p NOVO_EMAIL="Digite o novo user.email: "

        git config --global user.name "!NOVO_NOME!"
        git config --global user.email "!NOVO_EMAIL!"

        set GIT_NAME=!NOVO_NOME!

        echo Configuracao atualizada com sucesso.
        echo(
        
    )
) else (
    echo Git ainda nao esta configurado globalmente.
    echo(
    echo Exemplo:
    echo Usuario: davigopi
    echo Email:   davigopi@gmail.com
    echo(
    set /p NOVO_NOME="Digite o user.name: "
    set /p NOVO_EMAIL="Digite o user.email: "

    git config --global user.name "!NOVO_NOME!"
    git config --global user.email "!NOVO_EMAIL!"

    set GIT_NAME=!NOVO_NOME!

    echo Configuracao aplicada com sucesso.
    echo(
)

REM ===== PEGAR NOME DA PASTA =====
for %%I in (.) do set PROJETO_LOCAL=%%~nxI

echo Projeto local detectado: %PROJETO_LOCAL%
echo(

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

echo(
echo Projeto que sera usado: %PROJETO%
echo Repositorio: %REPO_URL%
echo(

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

echo(
echo Upload concluido com sucesso!
pause