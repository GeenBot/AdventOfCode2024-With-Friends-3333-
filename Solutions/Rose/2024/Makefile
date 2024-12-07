DAY ?= 01
KIND ?= elle
INPUT ?= sample.txt

both: elle py

all:
	@$(foreach file, $(shell find . -mindepth 1 -type d -exec basename {} \; | sort -n), \
		echo "Day $(file)"; \
	    make $(KIND) DAY=$(file); \
		echo; \
	)

elle: $(DAY)/solution
	@./$(DAY)/solution $(DAY)/$(INPUT)

$(DAY)/solution: $(DAY)/solution.le
	@ellec $(DAY)/solution.le -o $(DAY)/solution -z -O3

py: $(DAY)/solution.py
	@python3 $(DAY)/solution.py $(DAY)/$(INPUT)

time:
	hyperfine --warmup 3 'make solution' 'make py'

.PHONY: clean
clean:
	rm -f $(DAY)/solution
