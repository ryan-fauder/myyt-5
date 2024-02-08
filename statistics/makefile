.PHONY: all

PYTHON_STAT_SERVER_INIT = app.py
PYTHON_STAT_MANAGER_INIT = app.py

DIR1 = statistics-server
DIR2 = statistics-manager


all: run_stat_server run_stat_manager

run_stat_server:
	@echo "Verificando diretório para script 1..."
	@if [ "$(CURDIR)" != "$(DIR1)" ]; then \
		echo "Entrando na pasta..."; \
		cd $(DIR1); \
		echo "Executando o comando Python para o STAT SERVER..."; \
		python3 $(PYTHON_STAT_SERVER_INIT); \
	fi

run_stat_manager:
	@echo "Verificando diretório para script 2..."
	@if [ "$(CURDIR)" != "$(DIR2)" ]; then \
		echo "Entrando na pasta..."; \
		cd $(DIR2); \
		echo "Executando o comando Python para o STAT MANAGER...;" \
		echo "$(CURDIR)"; \
		python3 $(PYTHON_STAT_MANAGER_INIT); \
	fi
