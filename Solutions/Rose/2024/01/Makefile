all: elle py

elle: solution
	./solution

solution: solution.le
	ellec solution.le -t

py: solution.py
	python3 solution.py

time:
	hyperfine --warmup 3 'make elle'
	hyperfine --warmup 3 'make py'

.PHONY: clean
clean:
	rm solution
