import hacker
import hacker_comp

from solver import ComparationHacker, MulAddDivDecHacker
from driverstuff import driver, NoSuchElementException

import asyncio


async def main(usr=None, pwd=None):
    username = ''
    password = ''
    base_url = 'https://miksike.net.ua/#pranglimine'

    if not usr or not pwd:
        username = input('Username: ')
        password = input('Password: ')

    driver.get(base_url)

    if not usr or not pwd:
        while not await login(username, password):
            await asyncio.sleep(0.5)
            username = input('Username: ')
            password = input('Password: ')
    else:
        if not await login(usr, pwd):
            print('Wrong acc data')
            return False

    await asyncio.sleep(0.5)

    start_msg = '1 - Adding, Dividing, Multiplication, Diferensation\n' +\
        '2 - Comparing\n' +\
        'Enter - End\n'

    while (choice := input(start_msg)) != '':
        if choice == '1':
            t = MulAddDivDecHacker()
        elif choice == '2':
            t = ComparationHacker()
        else:
            print('Bad choice')

        input('Press Enter when you will be ready')
        await t.Analize()

        await asyncio.sleep(0.5)

    if not usr or not pwd:
        driver.quit()

    return True


async def logout():
    try:
        logoutbtn = driver.find_element_by_xpath('//*[@id="top"]/form[1]/table/tbody/tr/td[3]/a')
    except NoSuchElementException as e:
        print('Error while logging out')
    else:
        logoutbtn.click()


async def login(usrnm, pwd):
    await asyncio.sleep(0.3)
    try:
        usernamefield = driver.find_element_by_xpath('//*[@id="top"]/form[1]/table/tbody/tr/td[3]/input[1]')
        pwdfield = driver.find_element_by_xpath('//*[@id="top"]/form[1]/table/tbody/tr/td[3]/input[2]')
        submitbtn = driver.find_element_by_xpath('//*[@id="top"]/form[1]/table/tbody/tr/td[3]/input[3]')
    except NoSuchElementException as e:
        print('Cant find nessesarry element')
    else:
        usernamefield.send_keys(usrnm)
        pwdfield.send_keys(pwd)
        submitbtn.click()

    await asyncio.sleep(0.3)

    try:
        driver.find_element_by_xpath('//*[@id="top"]/form[1]/table/tbody/tr/td[3]/font')
    except NoSuchElementException as e:
        print('Successfully logged in')
        return True
    else:
        print('Something went wrong')
    return False


if __name__ == '__main__':
    asyncio.run(main())
