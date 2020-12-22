# Tags

## Running locally

### Actually, you can easy run it with docker-compose
```
docker-compose build
docker-compose up
```
#### But in such case you will not be able to create super user (at least in easy way)
1)
```
git clone https://github.com/aperekhozhuk/Tags
```
2)
```
cd Tags
```
3)
```
python3 -m venv env
```
4)
```
source env/bin/activate
```
5)
```
pip install -r requirements.txt
```
6)
```
cd tags_app
```
7)
```
python3 manage.py migrate
```
8)
```
python3 manage.py createsuperuser
```
9)
```
python3 manage.py runserver 
```

# Open http://localhost:8000/ in your browser
