@REM To run this bat file copy it in root folder of this project and db click

@REM Uncomment anyone of the line
@REM pytest -v -s -m "sanity or regression" --html=Reports/reports_chrome.html --browser chrome
@REM pytest -v -s -m "sanity and regression" --html=Reports/reports_chrome.html --browser chrome
@REM pytest -v -s -m "regression" --html=Reports/reports_chrome.html --browser chrome
@REM pytest -v -s -m "sanity" --html=Reports/reports_chrome.html --browser chrome

@REM pytest -v -s -m "sanity or regression" --html=Reports/reports_chrome.html --browser firefox
@REM pytest -v -s -m "sanity and regression" --html=Reports/reports_chrome.html --browser firefox
@REM pytest -v -s -m "regression" --html=Reports/reports_chrome.html --browser firefox
@REM pytest -v -s -m "sanity" --html=Reports/reports_chrome.html --browser firefox