## 📑 Data Versioning

Beyond the source code and experiment results, an important part of every ML product lifecycle involves data.

> More data beats clever algorithms, but better data beats more data.

#### Data Version Control - [DVC](https://dvc.org/)

Provides a git-like experience to organize your data, models, and experiments.

With DVC, we added the ability to maintain data versioning, without necessarily using the repository as storage.

### Dependencies

Create a `venv` and install dependencies

```bash
    # Create environment
    $ python3 -m venv venv  

    # Activate environment
    $ source venv/bin/activate

    # Install dependencies
    $ pip install -r requirements.txt
```

Also create a `.env` file with the following:

```bash
    # .env content'
    AWS_ACCESS_KEY_ID="XXXXXXXXXXXXXX"
    AWS_SECRET_ACCESS_KEY="aaaaaaaaaaaaaaaaaaaaaaaaaaa"
    AWS_REGION="xx-xxxx-2"
    AWS_LAMBDA_ROLE_ARN="arn:xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```


### 📌 How to use this project

#### Store Locally Data

1. Create a git repository

2. Init and configure dvc

```bash
 # Root of git repository run:
 $ dvc init

 # Download dataset:
 $ dvc get-url https://mlops-material.s3.us-east-2.amazonaws.com/data_v0.csv data/data.csv

 # Configure dvc to track file:
 $ dvc add data/data.csv
```

3. Commit and add change to git repository:

```bash
 $ git add data/data.csv.dvc data/.gitignore
 $ git commit -m "Add data to project"
 $ git push
```

4. Store data locally
 
 Create a repository outside the repository

```bash
 $ mkdir /home/user/dvcstore
```

 Configure DVC to use this folder as remote storage
 
```bash
  $ dvc remote add -d myremote /home/user/dvcstore
 
  # Upload data to the local storage:
  $ dvc push
``` 

Test the remote

```bash
 # Delete the file data/data.csv
 $ rm -rf .dvc/cache
 $ rm -f data/data.csv
 $ ls -la data/

 # Restore the file
 $ dvc pull
 $ ls -la data/
```

Add all changes

```bash
 $ git add .
 $ git commit -m "version 0"
 $ git push
 $ git tag -a v0.0.0 -m "Release version 0.0.0"
```

5. New features add to data

Update data folder with the new data

```bash
 $ dvc get-url --force https://mlops-material.s3.us-east-2.amazonaws.com/data_v1.csv data/data.csv
```

Create a train.py file (empty):

```bash
 $ touch src/train.py
```

Commit change in *git* and in *dvc*:

```bash
 $ dvc commit data/data.csv
 $ dvc push

 $ git add .
 $ git commit -m "version 1"
 $ git push
 $ git tag -a v0.0.1 -m "Release version 0.0.1"
```

6. Switch between data versions

Open the file data/data.csv and see the changes:

```bash
 # Version 0
 $ git checkout v0.0.0
 $ dvc checkout

 # Version 1
 $ git checkout v0.0.1
 $ dvc checkout
```

#### Store S3 Data

1. Create a git repository

2. Init and configure dvc

```bash
    $ dvc init
    $ dvc get-url https://mlops-material.s3.us-east-2.amazonaws.com/data_v0.csv data/data.csv
    $ dvc add data/data.csv
```

3. Commit data to git repository

```bash
    $ git add data/data.csv.dvc data/.gitignore
    $ git commit -m "Add data to project"
    $ git push
```

4. Create a S3 Bucket

Run this code to create a bucket:

```bash
    $ python3 src/utils/create_bucket.py
```

5. Configure S3 Storage

```bash
    $ dvc remote add myremote s3://<bucket-name>
    $ dvc remote default myremote
    $ dvc push
```

6. Check if data was stored

```bash
  $ python3 src/utils/read_bucket_content.py
```

7. Delete the bucket:

```bash
  $ python3 src/utils/delete_bucket.py
```

<br>

@2024, Insper. 9° Semester, Computer Engineering.
Machine Learning Ops & Interviews Discipline