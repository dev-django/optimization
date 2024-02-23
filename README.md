# Django Optimization

장고 성능 개선 코드 모음

Framework : Django 5.0.2 , DRF 3.14.0

Database : MySQL 8.0.35

# 시작하기
1. mysql 설치
```shell
docker compose up -d
```
2. 마이그레이션 파일 생성
```shell
python manage.py makemigrations 
```
3. 마이그레이트
```shell
python manage.py migrate
```
4. 정적파일준비
```shell
python manage.py collectstatic
```
5. 서버시작
```shell
python manage.py runserver
```


## 1. Pagination

