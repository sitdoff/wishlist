debug:
	flask --app application run --host 0.0.0.0 --port 8000 --debug

gunicorn:
	gunicorn -w 4 -b 0.0.0.0:8000 application:app 

build:
	docker build --tag=sitdoff/wishlist . && docker run -it -p 8000:8000 sitdoff/wishlist
