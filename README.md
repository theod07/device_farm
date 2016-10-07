# device_farm

# to create a .zip file for aws devicefarm
rm test_bundle.zip
pip freeze > requirements.txt
pip wheel --wheel-dir wheelhouse -r requirements.txt
find . -name '__pycache__' -type d -exec rm -r {} +
find . -name '*.pyc' -exec rm -f {} +
find . -name '*.pyo' -exec rm -f {} +
find . -name '*~' -exec rm -f {} +
zip -r test_bundle.zip tests/ wheelhouse/ requirements.txt



mobile iOS commit a6301edeadb66ffd422672089885ab65e3741eac
iphone5		7.0.4		couldn't launch setup suite
iphone5		8.3			timeout while waiting for screenshot (kiosk test); failed in delete_all_cookies in google test
iphone5		8.0			OK 
iphone5c	8.1			OK
iphone5c 	9.1			OK ; BadStatusLine in google test
iphone5c	8.4			No internet service
iphone5c	7.1.2		Setup test failed
iphone5c 	8.0.2		BadStatusLine(google test); BadStatusLine(solvhealth); BadStatusLine(kiosk)
iphone5c 	9.0			OK
iphone5s	8.2			BadStatusLine(google test); BadStatusLine(solvhealth); BadStatusLine(kiosk)
iphone5s	7.1.1		Setup test failed
iphone5s	9.2			
iphone5s	8.1.1		WebDriverException: Message (solvhealth) Could not set socket option SO_OPPORTUNISTIC: Invalid Argument; Kiosk test ok
iphone6		9.2.1		OK
iphone6		8.1.2		BadStatusLine(google test); BadStatusLine(solvhealth); BadStatusLine(kiosk) Could not set socket option SO_OPPORTUNISTIC: Invalid Argument;
iphone6+	9.3.1		Failed to start Appium server.
iphone6+ 	9.2.1		Setup test failed
iphone6+	8.1.3		BadStatusLine(google test); Could not set socket option SO_OPPORTUNISTIC: Invalid Argument;
iphone6s	9.2			3x failed tests in test_ios.py. Logs empty
iphone6s+	9.2.1		BadStatusLine(google test)
iphoneSE	9.3			OK