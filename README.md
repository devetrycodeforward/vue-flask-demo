# Vue-Flask-Demo

## Running

- **In one terminal tab**:
    - `cd client`
    - `npm install`
    - `npm run build`

- **In a new tab**:
    - `cd server`
    - `pipenv install`
    - `pipenv run python main.py`


### Environment Vars

Create a `.env` file with the following:

```
DB_USER=
DB_PASS=
DB_URL=
DB_NAME=
RUN_ENVIRONMENT=
```

**Note: if RUN_ENVIRONMENT == 'network', the app will connect to postgres according the the env variables above. Otherwise it will coneect to a local sqlite3 file**

### Video Code Along:

- [Google Drive Folder: 5 Parts](https://drive.google.com/drive/u/1/folders/181eR9eEgzrKf6oynVs5WZWTFiKZvsF8M)