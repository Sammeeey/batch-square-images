# batch-square-images
command line tool to to "batch-square" .jpg images - centered, white background, based on longer side of original image

## How to use the batch-squarizer? (English 🇺🇸 🇬🇧 Windows 10)
- [clone repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) to the *Documents* directory of your computer

### Installation & Preparation
- install Python on your PC if you have not already done so

### Execution

#### Navigate to software files

1.  Open "Command Prompt" (CMD).

    1.  Press Windows key + R > type "cmd" > press Enter

2.  In CMD navigate to path where script (**square.py**) and the **requirements.txt** are located
    1. Enter text according to the following pattern (replace **YOUR_USERNAME** with yours):
        
        `cd C:\Users\**YOUR_USERNAME**\Documents\batch-square-images`

#### Create virtual environment (venv).

1.  Type the following text in CMD & press Enter (to create a virtual environment named "venv"):
    
    `py -m venv venv`

#### activate venv

1.  Type the following text in CMD & press Enter:

    `venv\Scripts\activate.bat`

#### **Requirements.txt in venv to install**
This conversation was marked as resolved by kiritocode1

1.  Type the following text in CMD & press Enter:

    `pip install -r requirements.txt`

#### Run the executable file (**square.py**) and follow the instructions

1.  Type the following text in CMD & press Enter:

    `py square.py`

#### follow instructions & find result

- follow instructions on the command line

After the script finished the processing you'll find your squarized images in a sub directory of your given path (which you will have provided on the command line while running the **square.py** script)

## known limitations

- only able to squarize jpg images so far

    You are welcome to add an issue or make a pull request with a fix for that issue
