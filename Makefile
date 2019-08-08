
PORT=8000
APP_URI=helper/

test:
	coverage run manage.py test bmbhelper -v 2

serve: open
	python manage.py runserver

shell:
	python manage.py shell

open:
	open http://localhost:$(PORT)/$(APP_URI)
