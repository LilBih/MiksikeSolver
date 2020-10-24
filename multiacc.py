import starter
import asyncio

from driverstuff import driver

username = None
pwd = None
accs = {}

print('Welcome to multiacc')

asyncio.run(asyncio.sleep(1))

while username != '' or pwd != '':
    if username == '' or pwd == '':
        print('Bad acc data. Try one more time.')
        asyncio.run(asyncio.sleep(1))
        continue

    asyncio.run(asyncio.sleep(1))

    if username:
        accs[username] = pwd

    username = input('Username: ')
    pwd = input('Password: ')

for i in accs:
    asyncio.run(asyncio.sleep(1))
    print('Logginning as ' + i)
    if not asyncio.run(starter.main(i, accs[i])):
        print('Error:' + i + '(' + accs[i] + ') is wrong data')

    asyncio.run(starter.logout())

driver.quit()
