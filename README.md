# AutoReg_Cusis
At CUHK, there is busy network during register coureses at the begining of the semister. Human reaction time is around 0.25s, while my programm clicking time is around 0.013. So, Auto-register programm can ensure students 
can enroll their interested courses even if the quota of courses is very limited.


the program is used for autmoating broswing CUSIS, and autoclick the enroll bottom for registering courses.
This program ONLY work on chrome driver version
# Change config.json with your infomation
"login_email": "1155xxxxxx@link.cuhk.edu.hk"

"login_password": "12345678"

"register_time": "20:20:00.000000"

"selenium_driver_PATH": the path of the selenium Chrome driver

# tutorial
1. install the selenium chrome driver in the computer [link](https://chromedriver.chromium.org/downloads)

2. format the config file with your input

3. run the programme

4. browse the shopping cart and select the courses you interested in

5. input your register mode

# register mode
### Validate
input "v" for validating the selected courses
### Enroll
input "e" for enrolling the selected courses

# Result
the program will auto click the bottom, good luck !!!