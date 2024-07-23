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