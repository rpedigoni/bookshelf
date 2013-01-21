test:
	coverage run --branch --source=. ./manage.py test
	coverage report --omit=*/migrations*,*/tests*,wsgi*,manage*,runner*

xml_coverage:
	coverage xml --omit=*/migrations*,*/tests*,wsgi*,manage*,runner*

test_html:
	coverage run --branch --source=. ./manage.py test
	coverage report --omit=*/migrations*,*/tests*,wsgi*,manage*,runner*
	coverage html --omit=*/migrations*,*/tests*,wsgi*,manage*,runner*
	open htmlcov/index.html

clean:
	rm -rf htmlcov/*
	rm .coverage
