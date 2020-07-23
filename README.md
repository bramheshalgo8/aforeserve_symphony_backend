# Aforeserve Symphony Backend

### Clone this repository and configure listed things

### Start with executing following commands

```python
pip3 install -r requirements.txt
```

### Configure DataBase
```bash
sudo apt update
sudo apt install mysql-server
sudo mysql_secure_installation
```

### Allow user to connect with database
```bash
sudo mysql -u root -p
Enter Password : XXXXXXXX
create user 'dev'@'publicIP' identified by <password>
grant all priveleges on *.* to 'dev'@'publicIP' with grant option;
flush priveleges;
```

### Create database and table
```bash
sudo mysql -u root -p
Enter Password : XXXXXXXX
create database aforeserve
use aforeserve
create table Tickets(--Copy Variable from Sql details.txt and put here--);
create table userdetails(--Copy Variable from Sql details.txt and put here--);
```

### Configure database in python file
```bash
nano create_db.py
```
```python
add --> engine = create_engine("mysql+pymysql://root:<password>@127.0.0.1/<database>?host=localhost?<table>=3306")
```

### Detailed structure of server.py (main file)
```python
@app.route('/newt/..')
```
- It is for creating new ticket in itsm and predciting class of ticket(Issue belogns to which category) and sending mail to respective client and it returns ticket id in client's app

```python
@app.route('/inoutserver/..')
```
- It is for sending incoming mail server and outgoing mail server to client's app

```python
@app.route('/userdetails/..')
```
- It is for registering new user if user doesn't exists else it will create new user and assign new unique key.

```python
@app.route('/oldt/..')
```
- It is for returing status and issue to client when he/she asks for.

```python
@app.route('/upt/..')
```
- It is for updating ticket in database and ITSM based on user solution

```python
@app.route('/know/..')
```
- It is for sending details of tickets raised by client previously

```python
@app.route('/getalluniqueid/..')
```
- It is for returning all unique ids present in database for checking if cleint is registered or not
