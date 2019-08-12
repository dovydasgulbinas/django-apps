
PORT=8000
APP_URI=bc2mb/



test:
	coverage run manage.py test bmbhelper -v 2

serve: open
	python manage.py runserver

shell:
	python manage.py shell

open:
	open http://localhost:$(PORT)/$(APP_URI)

freeze:
	pip freeze > requirements.txt
	git add requirements.txt

build: