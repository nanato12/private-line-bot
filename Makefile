check:
	black --check --verbose . \
		--exclude="(akad\/*|cherline\/*|line\/*)"

format:
	black --verbose . \
		--exclude="(akad\/*|cherline\/*|line\/*)"
