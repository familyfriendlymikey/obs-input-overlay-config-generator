## OBS Input Overlay Config Generator

I was using [this](https://github.com/univrsal/input-overlay) OBS plugin and wanted to create my own keyboard overlay for OBS,
but creating the config file was really tedious, so I made this script to generate the config file for me.

## Pros & Cons
Once you create a "texture" file of all the keys you might use,
you can rearrange the keys however you want very quickly just by updating `config.py`.

However, in order to accomplish this behavior,
all keys must be rectangles of exactly the same dimensions in the texture file.
So, if you want the `space` key to be wider than the `q` key for example, this script is not for you.

## Requirements
This script operates on the following conventions:
- There is only one row of keys in your texture file (with the highlighted keys right below them).
- There is a 1px border around the entire texture file.
- There is a 3px gap between each key in the texture file.

## Usage

### Get the dimensions

If you're creating your own texture file,
first let the script help you get the dimensions of the file.

1. Update `config.py` with the
	- Height and width of each key you will use in the texture file.
	- Order of the keys in the texture file.
1. Run `python3 gen.py -p` to get the height and width you will need to use in the texture file.

### Make a texture file
I recommend using the free online image editor [photopea](https://www.photopea.com/).

Create a new project with the height and width you just got.
Referencing `example_texture.png`, ensure that
- All keys are exactly the same dimensions.
- There is a 3px gap between each key.
- There is a 1px gap around the entire image.

![example texture file](/example_texture.png)

### Create an overlay config
Update `config.py` with the

- Arrangement of keys you'd like to show up in the overlay.
- Gap in pixels between each key you'd like in the overlay.

Run `python3 gen.py`.

Done!
