all: elle py

elle: solution
	@./solution
	@rm ./solution

solution:
	@ellec solution.le -t

py: solution.py
	@python3 solution.py
