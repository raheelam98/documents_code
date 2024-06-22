# Commands 

Documentation of Python, Chatgpt , Fast API, Docker Container, Kubernetes 

**Note**
File Permissions with chmod -- only for mac user

current working directory
```bash
pwd
```

grants all users full read, write, and execute permissions on the specified folder and its contents
```bash
chmod <permission> <directory or filename>

sudo chmod -R 777 /path/to/folder

sudo chmod -R 777  /Users/user-name/Documents/folder-name
```

view hidden files on Mac
Press Command + Shift + . (the period key). This will show hidden files in the folder.

To hide the files again, press Command + Shift + . again.

**clone repository**

Note :- copy URL 

<div style="text-align: center;">
    <img alt="" src="./images/i_clone_https.png" width="300px"></img>
</div>


```shell
git clone URL
```

**push code to repository** 

(i) :- Open terminal

(ii) :-  Set your local project as the current working directory

current working directory
```shell
pwd
```

(iii)  :-  copy path 

```shell
cd path
```

(iv)  :- check files
```shell
ls
```

### push code to repository :: (case I)

Step 1 :- Initialize the local directory as a Git repository 

```shell
git init
```

Step 2 :- Add the files in your new local repository. Your files will now be the staged for their first commit.

```shell
git add .

git status
```
note:- dot is use for current dir

Step 3 :-  Commit the file that you have staged in your local repository
(Connect the files with local repository)

```bash
git commit -m “first commit”
```
flag -m :- message

Step 4 :-  Push the code in your local repository  to Github

```bash
git push --set-upstream origin main
```

Add username and password (if required / for first time)

### push code into specific repository  in two minute:: (case II)

#### create new repository

**Step I :- select new** 

<div style="text-align: center;">
    <img alt="" src="./images/i_new_repository.png" width="800px"></img>
</div>

**Step II :- create repository**

<div style="text-align: center;">
    <img alt="" src="./images/i_creat_repository.png" width="500px"></img>
</div>

**Step III  :- copy first 3 lines and past on terminal** 

note :- app terminal

<div style="text-align: center;">
    <img alt="" src="./images/i_copy_first_3lines.png" width="500px"></img>
</div>

press enter

**Step IV :-  write command**

```bash
git add .
```
note:- dot is use for current dir

**Step V :- copy last 4 lines and past on terminal**

<div style="text-align: center;">
    <img alt="" src="./images/i_copy_last_4lines.png" width="500px"></img>
</div>

press enter

**Step VI  :- refresh page**

<div style="text-align: center;">
    <img alt="" src="./images/i_refresh.png" width="500px"></img>
</div>

### terminal 

<div style="text-align: center;">
    <img alt="" src="./images/i_terminal.png" width="500px"></img>
</div>

Push Code to your GitHub Account - Under 3 Minutes
https://www.youtube.com/watch?v=vpRkAoCqX3o

How to Show Hidden Files on Mac
https://www.youtube.com/watch?v=8HvedBfa7S0 


#### …or create a new repository on the command line

echo "# Document_Coding" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/raheelam98/Document_Coding.git
git push -u origin main

####  …or push an existing repository from the command line

git remote add origin https://github.com/raheelam98/Document_Coding.git

git branch -M main

git push -u origin main



# documents_code
