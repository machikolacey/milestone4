# Machiko Lacey Pianist website

## UX

## Features

## Deployment

This project was developed on Github, using Gitpod as IDE. It has only master branch.
This is pushed and deployed on to heroku.

Deployed project is found here:

https://milestone3-data-centric-mlk.herokuapp.com/

This project utilises Mongo DB to use NO-SQL (non-relational) database.
Before cloning the project:

<ol>
<li>Add a database collection 'brightonCafes' on <a href="https://www.mongodb.com/cloud/atlas" target="_blank">MongoDB Atlas</a></li>
<li>Create a database and these tables: 
   <ul>
   <li>cafes</li>
   <li>areas</li>
   <li>users</li>
   <li>memories</li>
   </ul>
</li>
</ol>

## To run this project on your local repository
This project will be deployed following these steps:
<ol>
<li>Add your own repository on your Github account</li>
<li>Click the green 'Gitpod' button on top-right corner of this repo(If you can't find the button, install 'Gitpod' extension on your Chrome browser</li>
<li>Gitpod launches</li>
<li>Run the following command (Replace the 'USERNAME' and 'REPO' to your username and repo name):</li>
 
```

git remote set-url origin https://github.com/USERNAME/REPO.git

```


<li>Add env.py file on your root folder, add these lines:
 
```
import os

os.environ['SECRET_KEY'] = '- YOUR SECRET KEY - '
os.environ['MONGO_URI'] = '- YOUR MONGO URI -' 

```
</li>
<li>Run this command below to install all the modules on requirements.txt file:

```

pip3 install -r requirements.txt

```
</li>
<li>Run the code by running this code below:
 
```

python3 app.py

```

</li>
</ol>


## Remote Deployment (Run the project on Heroku.com)
If you want to add it to your Heroku account, follow the instructions below:

<ol>
<li>Add an app for this project</li>
<li>Add environment variables 'SECRET_KEY' and 'MONGO_URI' on your app</li> 
<li>Add PORT on your app</li> 
<li>On your Gitpod workspace, login to heroku by running this code below:
 
 
```

heroku login -i

```

</li> 
<li>Select your app by running this code below (Replace '- YOUR APP NAME -' with your own app name):
 
```

git init

heroku git:remote -a  - YOUR APP NAME -

```

</li>
<li>Run this code below to push the code to your Heroku app:

```

git push heroku master

```

</li>
<li>When the app is deployed, click on 'Open App' button to run your app </li>
</ol>

## Technologies Used

## Testing

### Test Results


### Acknowledgements

