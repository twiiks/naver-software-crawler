import argparse
from selenium import webdriver
import time


def parse_args():
    desc = "help download every element in naver software"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument(
        '--address',
        type=str,
        default='',
        help='put the address of specific category',
        required=True)
    parser.add_argument(
        '--id', type=str, default='', help='put an id for naver', required=True)
    parser.add_argument(
        '--password',
        type=str,
        default='',
        help='put a password for naver',
        required=True)
    parser.add_argument(
        '--driver',
        type=str,
        default='',
        help='put a chrome driver',
        required=True)
    parser.add_argument(
        '--waittime',
        type=int,
        default=15,
        help='every page it will wait for waittime seconds before going next',
        required=False)

    parser.add_argument(
        '--goingon',
        type=bool,
        default=False,
        help=
        'It should be true when you are giving the address of specific software not the first category page',
        required=False)

    return parser.parse_args()


def itsDone(current_url):
    print('download is done!!')
    print('the last address for download was :\n', current_url)


def itsStopped(current_url):
    print('It seems like naver stopped your action.\
you can start from address :\n', current_url,
          '\nwhen you start again with above address,\
you need to set going on as true')


def goNextPage(isFirstElement, driver, current_url):
    if isFirstElement:
        path = '//*[@id="content"]/div[3]'
        isFirstElement = False
    else:
        path = '//*[@id="content"]/div[4]'
    try:
        driver.find_element_by_xpath(path).click()
    except:
        itsDone(current_url)
        exit()
    return isFirstElement


def main():
    isFirstElement = True
    args = parse_args()

    if args is None:
        exit()
    if args.goingon:
        isFirstElement = False

    driver = webdriver.Chrome(args.driver)
    driver.implicitly_wait(3)

    # login naver
    driver.get('http://naver.com')
    time.sleep(1)
    driver.find_element_by_name('id').send_keys(args.id)
    driver.find_element_by_name('pw').send_keys(args.password)
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="frmNIDLogin"]/fieldset/span/input').click()

    # go to naver software
    driver.get(args.address)
    time.sleep(2)

    # click first element
    if not args.goingon:
        driver.find_element_by_xpath('//*[@id="slot0"]/a/div/div[1]').click()
        time.sleep(2)

    while (True):
        current_url = driver.current_url
        # first click for download
        driver.find_element_by_xpath('//*[@id="_sticked_guide"]/div[1]').click()
        time.sleep(2)

        # check if new tab is opened by clicking download.
        # if so, just close it and go next page
        if len(driver.window_handles) >= 2:
            driver.switch_to_window(driver.window_handles[1])
            ## if you want to do something before closing new tab, code below
            ##
            ##
            driver.close()
            driver.switch_to_window(driver.window_handles[0])
            time.sleep(1)
            isFirstElement = goNextPage(isFirstElement, driver, current_url)
            time.sleep(2)
            continue

        # try clicking for poped up download, if N/A go next page
        try:
            driver.find_element_by_id('showUseRangeLayerDownloadLink').click()
        except:
            driver.execute_script(
                "window.scrollTo(0, -document.body.scrollHeight);")
            time.sleep(1)
            isFirstElement = goNextPage(isFirstElement, driver, current_url)
            continue
        time.sleep(2)

        # click download for last acception
        try:
            driver.find_element_by_xpath(
                '//*[@id="downloaderAlert"]/a[3]').click()
        except:
            itsStopped(current_url)
            exit()

        time.sleep(2)

        # click next, if there is no next anymore, program is finished
        # try:
        isFirstElement = goNextPage(isFirstElement, driver, current_url)
        # driver.find_element_by_xpath('//*[@id="content"]/div[3]').click()
        # except:
        # break
        time.sleep(args.waittime)


if __name__ == '__main__':
    main()