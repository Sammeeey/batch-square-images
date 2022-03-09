# square.py

# functionality in short:
# - so far only a script (command line tool) to "batch-square" .jpg images
# - extends background of images with white color (based on longer side of image)
# - places picture in center of white background

# purpose / reason:
# - create squared images for usage in online shops 

# steps in the script:
# - create "square_images" sub directory if not existent yet
# - process all .jpg images from a certain directory (given by a user) one by one
#   - check width and height to determine long and short side
#   - copy image
# - create new image with white background 

# Props to Al Sweigart for the great book http://automatetheboringstuff.com/

from PIL import Image
import glob, os
from sys import argv
from pathlib import Path

# script, targetPath = argv

print('In which path do you want to sqaure images (based on longer side)?')
print("Please provide it a string, like: C:\\Users\\Name")
targetPath = Path(input())
os.chdir(targetPath)

# define directory for square images
# try to create directory for final square images
try:
    os.mkdir('square_images')
# if a directory with the above specified name already exists skip the creation of that directory (the existing directory will be used to save images later)
except FileExistsError:
    pass
finally:
    # define path where square images should be saved
    savePath = targetPath / 'square_images'

# process images to create squares (on white background), size based on longer side
for infile in glob.glob("*.jpg"):
    fileName, ext = os.path.splitext(infile)
    with Image.open(infile) as im:
        # width, height = im.size
        # width = im.width
        # height = im.height
        if im.width > im.height:
            longLength = im.width
            shortLength = im.height
            longSide = 'width'
            shortSide = 'height'
        else:
            longLength = im.height
            shortLength = im.width
            longSide = 'height'
            shortSide = 'width'
        sourceImage = im.copy()

    with Image.new(mode='RGB', size=(longLength, longLength), color='white') as newIm:
        # define distance from origin of coordinates (on the new (white) image), where the upper left corner of the paste image will be placed 
        upperLeft = round(longLength/2 - shortLength/2)
        if shortSide == 'height':
            pasteCoords = (0, upperLeft)
        else:   # if shortSide == 'width'
            pasteCoords = (upperLeft, 0)
        newIm.paste(im=sourceImage,
                    box=pasteCoords   #TODO: define correct place for image paste
                    )
        # change to square image directory
        # os.chdir()
        # save image in respective dicrectory, using original filename (adding '_square' suffix) and original file type
        newIm.save(fp=savePath / f'{fileName}_square{ext}') # possibly existing images with same name will be replaced by currently saved ones
        # os.chdir(targetPath)

# TODO: create Github issues
    # TODO: create github issues based on these TODOs
    # TODO: come up with more ideas for improvement of project or other nice ideas and issues
# TODO: clean up code
    # TODO: sort imports alphabetically
    # TODO: add comments to describe functionality
    # TODO: remove unnecessary code (outcommented parts)
# TODO: test if tool works for linux and MacOS
# TODO: improve github project
    # TODO: improve readme (description, etc.)
        # TODO: give shout-out to Al Sweigart (maybe link Twitter, book-link, etc.?)
        # TODO: maybe specify working python versions (initially built in Python 3.9.7)
        # TODO: maybe add used third party software/tools/libraries/frameworks etc.
        # TODO: edit readme to describe installation and use of tool
            # TODO: describe creation of virtual environment (venv; or link to source which describes it reliably) 
        # TODO: edit readme to describe script functionality
        # TODO: add before/after images
        # TODO: add live-use video (showing sample application of script and its functionality)
    # TODO: add sample images for quick testing (first only .jpg images until feature for processing of other images ist implemented)
    # TODO: adjust project description while improving and adjusting the project
    # TODO: choose and add a fitting license (optimally based on used libraries)
# TODO: eventually improve code
    # TODO: maybe add more output for user to understand and reproduce what's happening (for few photos it's quick)
    # TODO: rewrite code object-oriented (using functions and classes)
# TODO: make project work with different background colors (currently only white)
    # TODO: maybe ask user for a background color
# TODO: make project work for files which don't have .jpg extension
    # TODO maybe add feature to ask user which extension images have
    # TODO maybe even add feature to take all images - no matter which file extension
# TODO: maybe create GUI (maybe using Tkinter?) - would be really cool!😎
