run:
	[ -d .venv ] || make setup
	cd ./bin && ./run.sh
setup:
	cd ./bin && ./setup.sh
