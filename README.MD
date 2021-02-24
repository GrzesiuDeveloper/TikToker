# TikToker

TikToker is a Python program for botting views to TikTok videos.

## Installation

Download the zipped folder through GitHub, then etract it.

After that, `cd` to the directory and run the following command to install the dependencies needed:
```bash
pipenv install
```

## Usage
Getting the viewbot up and running is an extremely simple process.
First, run the Python file:
```bash
python3 main.py
```

Then, specify the TikTok video you would like to viewbot:

```
Please input your video url (It should look like this: 
https://www.tiktok.com/@USERNAME/video/VIDEOID)
> YOUR VIDEO
```

After that, go to the two browser windows and solve the captcha on each.

Finally, just sit back and relax, and look at your videos views go up!

Sample Output:
```
$ tiktok python3 main.py
---TikTok Viewbot---
My GitHub: recanman
How this works is that it uses Selenium to click buttons and type in the URL that you
specify in an external service that gives views. It would be really expensive to keep
up a network of bots for viewbotting use. I cannot guarantee that
the website will be up though.
Please input your video url (It should look like this: 
https://www.tiktok.com/@USERNAME/video/VIDEOID)
> https://www.tiktok.com/@tiktok/video/6584647400055377158

Solve the captcha in the web browser to continue.
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GNU Affero General Public License v3.0](https://choosealicense.com/licenses/agpl-3.0/)
