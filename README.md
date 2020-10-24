# MiksikeSolver
Written by Nikita Yezhikhin for automate solving Miksike

## Files
 - `multiacc.py` - solves Miksike for 2 or more acc per one time
 - `starter.py` - solves Miksike for 1 user per time
 - `solver.py` - base class and child classes for all disciplines (Summing, Multiplying, Comparing)
 - `driverstuff.py` - manages web browser
 - `chromedriver.exe` - chrome driver v86(Chromedriver version must be the same as your Chromebrowser version. 
 You can download Chromedriver from [chromedriver.chromium.org](https://chromedriver.chromium.org/downloads))
 - `dist folder`:
    - `chromedriver.exe` - chrome driver v86(Chromedriver version must be the same as your Chromebrowser version. 
    You can download Chromedriver from [chromedriver.chromium.org](https://chromedriver.chromium.org/downloads))
    - `starter.exe` - .exe file of `starter.py`
    - `multiacc.exe` - .exe file of `multiacc.py`
## chromedriver.exe
`chromedriver.exe` of corresponding version should be placed in the same folder with program
(if you are using executable program then you shoud place it in dist folder with the name **chromedriver.exe**,
otherwise: in the root folder)

## Using solver
1. Start up program from .py or .exe file
2. Input your account data in command prompt
3. Select necessary opiton from the list
4. Go to opened browser and open discipline on Miksike web page
(if you will need to solve a triathlon ect. then you need to select triathlon on web page and then select concrete discipline)
5. Press `Enter` in command prompt
6. Automate software will start solving discipline.
7. When the work will be done, you can repaet action starting from `4` option

## Requirements
1. **`Chrome brouser`**

If you will use python scripts, then:

2. Python v3.8(i don't know about other versions)
3. All python requirements in Requirements.txt
