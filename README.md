## Collect TTs of Twitter in Brazil

This code aims to collect the trending topics of Twitter from time to time. The code is in the [src](./src) folder below.

### Previous settings

##### Twitter API

To set up the code, you first need to get credentials to use the [Twitter API](https://developer.twitter.com/en) and generate a new file called *twitter_config.txt* from the template provided inside the [settings](./settings) folder.

##### Dropbox API

To syncronize the outputs, create a folder *trends* inside the main folder.

```
mkdir ./trends
```

Then, generate your credentials to use Dropbox as shown in the [Developers website](https://www.dropbox.com/developers/apps/create), and fill your token in the blank field of *sync.py* code. After changing the code, change the name of the file to *sync_credentials.py*

```
mv ./src/sync.py ./src/sync_credentials.py
```




### Execution

To execute the code (Linux and OSx), you might set your crontab to call the script *run.sh* according to your schedule. For that we execute 

```
crontab -e
```

The contab used for this work collects the trends every half an hour, as shown below

```
0,30 * * * * /path_to_folder/src/run.sh >> /path_to_folder/out.txt 2>&1
```


https://stackoverflow.com/questions/12534135/crontab-not-executing-a-python-script


https://github.com/dropbox/dropbox-sdk-python/blob/master/example/updown.py
