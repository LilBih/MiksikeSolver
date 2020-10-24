from driverstuff import driver, NoSuchElementException

import asyncio


class HackerBase:
    ElemsXPath = {}

    def Analize(self):
        raise NotImplementedError

    def solver(self, *args):
        raise NotImplementedError

    def LoadTryer(self, xpath=None):
        if xpath:
            try:
                driver.find_element_by_xpath(xpath)
            except NoSuchElementException as e:
                print('Can\'t load element ' + xpath)
                return False
            else:
                print('Successfully loaded element ' + xpath)
        else:
            for i in self.ElemsXPath:
                if i == '-':
                    continue
                try:
                    driver.find_element_by_xpath(self.ElemsXPath[i])
                except NoSuchElementException as e:
                    print('Can\'t load element ' + i + ' (' + self.ElemsXPath[i] + ')')
                    return False
                else:
                    print('Successfully loaded element ' + i + ' (' + self.ElemsXPath[i] + ')')
            return True

# test


class MulAddDivDecHacker(HackerBase):
    ElemsXPath = {
        'button_start': '//*[@id="btnAlusta"]',
        'sample': '//*[@id="txtTehtav"]',
        'okbutton': '//*[@id="OK"]',
        'status': '//*[@id="txtTeade"]',
        '-': '//*[@id="cmdMiinus"]',
        '1': '//*[@id="nr1"]',
        '2': '//*[@id="nr2"]',
        '3': '//*[@id="nr3"]',
        '4': '//*[@id="nr4"]',
        '5': '//*[@id="nr5"]',
        '6': '//*[@id="nr6"]',
        '7': '//*[@id="nr7"]',
        '8': '//*[@id="nr8"]',
        '9': '//*[@id="nr9"]',
        '0': '//*[@id="nr0"]',
    }

    def solver(self, *args):
        instr = args[0] if args[0][-1] != "=" else args[0][0:-1]

        while 'x' in instr:
            instr = instr.replace('x', '*', 1)

        result = eval(instr)

        for i in str(result):
            button = driver.find_element_by_xpath(self.ElemsXPath[i])
            button.click()

        return result

    async def Analize(self):
        driver.switch_to.window(driver.window_handles[1])

        if not self.LoadTryer():
            print('Error: Cant load any of nesesery elements')
            return

        button_start = driver.find_element_by_xpath(self.ElemsXPath['button_start'])

        print('Starting competition!!!')
        button_start.click()

        endStatus = driver.find_element_by_xpath(self.ElemsXPath['status']).text

        while endStatus != 'Час сплив!':
            endStatus = driver.find_element_by_xpath(self.ElemsXPath['status']).text

            sample = driver.find_element_by_xpath(self.ElemsXPath['sample']).text
            okbutton = driver.find_element_by_xpath('//*[@id="OK"]')

            if sample != "":
                sol = self.solver(sample)
                okbutton.click()

                print(sample + str(sol))

            await asyncio.sleep(0.1)

        print('Ending competition!!!')

        driver.switch_to.window(driver.window_handles[0])

class ComparationHacker(HackerBase):
    ElemsXPath = {
        'button_start': '//*[@id="btnAlusta"]',
        'sample1': '//*[@id="aVrd1"]',
        'sample2': '//*[@id="aVrd2"]',
        'status': '//*[@id="txtTeade"]',
        '>': '//*[@id="rohkem"]',
        '<': '//*[@id="vahem"]',
        '=': '//*[@id="sama"]'
    }

    def solver(self, *args):
        instr1 = args[0]
        instr2 = args[1]

        while 'x' in instr1:
            instr1 = instr1.replace('x', '*', 1)
        while 'x' in instr2:
            instr2 = instr2.replace('x', '*', 1)

        result1 = eval(instr1)
        result2 = eval(instr2)

        if result1 > result2:
            key = '>'
        elif result1 < result2:
            key = '<'
        else:
            key = '='

        button = driver.find_element_by_xpath(self.ElemsXPath[key])
        button.click()

        return key

    async def Analize(self):
        driver.switch_to.window(driver.window_handles[1])

        if not self.LoadTryer():
            print('Error: Cant load any of nesesery elements')
            return

        button_start = driver.find_element_by_xpath(self.ElemsXPath['button_start'])

        print('Starting competition!!!')
        button_start.click()

        endStatus = driver.find_element_by_xpath(self.ElemsXPath['status']).text
        sample1 = driver.find_element_by_xpath(self.ElemsXPath['sample1']).text
        sample2 = driver.find_element_by_xpath(self.ElemsXPath['sample2']).text

        while endStatus != 'Час сплив!':
            if sample1 != "" and sample2 != "":
                sol = self.solver(sample1, sample2)

                print(sample1 + sol + sample2)

            await asyncio.sleep(0.1)

            endStatus = driver.find_element_by_xpath(self.ElemsXPath['status']).text
            sample1 = driver.find_element_by_xpath(self.ElemsXPath['sample1']).text
            sample2 = driver.find_element_by_xpath(self.ElemsXPath['sample2']).text

        print('Ending competition!!!')

        driver.switch_to.window(driver.window_handles[0])
