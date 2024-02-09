.PHONY: run_netscanner run_replikate

run_netscanner:
	python3 netscanner/app.py

run_replikate:
	@if [ -f "$(dir)" ]; then \
		echo "Movendo arquivo para ./replikate"; \
		mv "$(dir)" ./replikate/; \
	fi
	@if [ "$(CURDIR)" != "replikate" ]; then \
		echo "Entrando na pasta..."; \
		cd replikate; \
		python3 app.py $(dir); \
	fi

run_overloader:
	python3 overloader/fake-client/app.py