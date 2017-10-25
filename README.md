# naver-software-crawler

**naver-software-crawler** downloads every single data from one category that you select from [Naver Software](http://software.naver.com/).

## Prerequisites
   - Python 3.6
   - Selenium
   - Chrome
   - [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

## Usage

Select one category and copy the main address like below.  
<img src="asset/naver-software-main.png" width="300px">

Clone this repo and enter

    $ python git clone https://github.com/sjang42/naver-software-crawler.git 
    $ cd naver-software-crawler

Execute crawler.py with needed options

    $ python crawler.py --help
    $ python crawler.py --address=[your_wanted_address] --id=[your_naver_id] --password=[your_naver_password] --driver=[path_to_chrome_driver]

## Example & Screenshot

This code will crawl all the fonts on [Naver Software](http://software.naver.com/).

    $ python crawler.py --address=http://software.naver.com/software/fontList.nhn?categoryId=I0100000 --id=your_naver_id --password=your_naver_password --driver=path_to_chrome_driver

<img src="asset/naver-software-font.png" width="300px">



Caution
----------------

Naver Software sometimes stops your action and let you go dump url. when this is happend, crawler will stop and will display the address that need to be preceed from. When you get this address, you execute crawler.py with **--goingon=True**. See **crawler.py --help** for more information. Auto re-starts feature will be added. Pull request is always welcome.
