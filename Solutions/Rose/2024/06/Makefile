INPUT ?= sample.txt
all: elle py

elle: solution
	./solution $(INPUT)

solution: solution.le
	ellec solution.le -t

py: solution.py
	python3 solution.py $(INPUT)

time:
	hyperfine --warmup 3 'make solution' 'make py'

.PHONY: clean
clean:
	rm -f solution
