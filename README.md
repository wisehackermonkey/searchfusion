# Search fusion 

### makes it super easy to find stuff on your computer
## local gui app that allows you to search for images and text files by tags autogenrated by ml classifiers


# install
# install conda
```bash
cd ~
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
~/miniconda3/bin/conda init bash
```
# close and open terminal
```bash
conda --version
conda create -n searchfusion python=3.8
conda activate searchfusion
pip install 'transformers[torch]' pillow
```


# examples of just using the classifer script
```bash
python blip.py --text "A " --input_file ./images/muffin.png --verbose > classified_images.txt
 ```


### Explanation
1. **Argument Parsing**: Added `--verbose` flag to enable verbose mode.
2. **Logging Configuration**: Configured logging to suppress all messages except critical ones by default. If `--verbose` is enabled, it shows warning messages.
3. **Logging Messages**: Added `logging.warning` calls at key points to provide messages when verbose mode is enabled.

### How to Run
1. **Using default values and suppressing messages**:
   ```bash
   python script.py < image_file.png
   ```

2. **Using verbose mode**:
   ```bash
   python script.py --verbose < image_file.png
   ```

3. **Providing a text prompt, input file, and verbose mode**:
   ```bash
   python script.py --text "A cute " --input_file ./images/muffin.png --verbose
   ```

This setup will suppress all messages except for the `print` output unless the `--verbose` flag is used.


## glob a bunch of files
cat ./images/crypto.png | python blip.py --text "A " >> classified_images.txt
cat ./images/crypto.png | python blip.py --text "photo of " --verbose >> classified_images.txt
ls ./images/*.* | parallel -j 2 'cat {} | python blip.py --text "a " --verbose >> classified_images.txt'



# todo add a hash value as a key
# add squel lite? idk
# interface?


# rip grep the file with fuzzy search

# search bar




# external resources
https://huggingface.co/Salesforce/blip-image-captioning-large

# target output
![alt text](image.png)


```bash
sudo apt-get install ripgrep
pip install ripgrepy
```

### prompt
```python
write a python script 

create a database using sqlite 
witht the following columns 

image_descriptions 
    path TEXT,
    description TEXT,
    hash TEXT
path (text) (path to file) (has the abspath of the image file)
description(text)
hash (text) (md5 hash of the file) make entry unique on this key

create the database call it image_descriptions

up_sert the file  "/home/o/github/searchfusion/images/tor.png" into the database
description = "a photo of a shady guy holding a onion"
db name "demo.db"
code only
```


# prompt
```python
create a python script 
that searches a sqlite database.
   db table name: image_descriptions
    path TEXT PRIMARY KEY,
    description TEXT,
    hash TEXT

key word search on description

create a commandline search input display the results 
for each result
"<path make fixed with on largest file name, strip the path to just the file name like '.../tor.png'>, <Description 'where a substring is found change console characters to red use '\033[91m'' >

add command line arguments 
--db 'demo.db'
--query -q 'onion'
script name is search.py
code only, example use
```


# prompt
```python
create a python script 
file name: jobs.py
search all sub directories (recusivly) for images using find
input is a list of directories to search within example ['./images', './secret']

images = 'png, jpg, gif, webp, bmp'


create a priority queue store in a sqlite database called jobs.db table name jobs_queue
        path TEXT, (abspath)
        time (time created)
        hash TEXT UNIQUE 
        completed BOOL
create a sqlite database. db file name images.db
   db table name: image_descriptions
    path TEXT,
    description TEXT,
    hash TEXT UNIQUE PRIMARY KEY
NUMWORKERS = 2
if there is jobs in the queue the pull off NUM_WORKERS
and run the shell command  
parallel NUMORKERS 'python blip.py --text "photo of " --verbose  --input_file {path} '
if NUMWORKERS is more than 1 then run multiple  python blip.py --text "photo of " --verbose  --input_file {path} '

store the results of each job into the image_descriptions table

code only, example use
```

# prompt

```python
convert this python script to accept list of image files from ls ./path/to/dir/*.png | vit.py 
vit.py (name of the script)
example path = ./images/*.png 

intalize  processor and model at the top of the file 
```