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

- [Adding Postgres](https://drive.google.com/open?id=1qw0EJb-brsLA_Cbqf6AOWTdtUURnG1ZR)

### Deploying to Heroku

- After setting up Postgres, follow the changes here: [Postgres to Heroku Diff](https://github.com/devetrycodeforward/vue-flask-demo/pull/1/files)
    - If followed, You should have:
        - Ran `pipenv install gunicorn`
        - created your Procfile
        - updated main.py

- [Create a free Heroku account](https://signup.heroku.com/)
- [Download the Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
    - OSX / Windows: Click the purple button to get the latest Heroku version
    - Ubuntu: `sudo snap install --classic heroku`
- Verify your Heroku install: `heroku --version`
- Sign in: `heroku login`

- In the __root__ of your application (where your `client` and `server` folders are) run the command:
    - `heroku create THE_NAME_YOU_WANT_FOR_YOUR_URL`
    - Your app will be deployed at the url: `https://www.THE_NAME_YOU_WANT_FOR_YOUR_URL.herokuapp.com`

- Run `git remote`, you should see `origin` and `heroku`
- Now we are going to TEMPORARILY un-gitignore our `server/dist` folder
    - Remove `server/dist` from your .gitignore
    - Run `git add .`
    - Run `git commit -m "temporarily un-ignore dist folder for heroku deployment"`

- Let's now get our app up on the Herku servers
    - Run `git push heroku master`
- And allocate some resources to run our app
    - Run `heroku ps:scale web=1`

- Login to your Heroku account in your browser
    - Click on your app
    - Click on `Settings` on the top-right of the white toolbar
    - Click `Reveal Config Vars`
    - Add vars from you `.env` file the the config vars screen

- Restart your heroku server:
    - Run `heroku restart`
    - Your app should now be running

- __VERY IMPORTANT__: Re-ignore your `server/dist` folder:
    - Add `server/dist` back to your .gitignore 
    - Run `git rm -rf --cached .`
    - Run `git add .`
    - Run `git commit -m "Re-ignore dist folder after heroku deployment"`

