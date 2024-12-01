all: make-elle make-py

make-elle: solution.le
	@ellec solution.le -t && ./solution
	@rm ./solution

make-py: solution.py
	@python3 solution.py
