# To run this shell script from terminal type 'sh run.sh'
# Compulosory line below
cd ..
cd Reports/
rm -rf *
cd ..
cd Logs/
rm -rf *
cd Screenshots/
rm -rf *
cd ..

# Uncomment any one of the line
# pytest -v -s -m "sanity or regression" --html=Reports/reports_chrome.html --browser chrome
# pytest -v -s -m "sanity and regression" --html=Reports/reports_chrome.html --browser chrome
# pytest -v -s -m "regression" --html=Reports/reports_chrome.html --browser chrome
pytest -v -s -m "sanity" --html=Reports/reports_chrome.html --browser chrome

# pytest -v -s -m "sanity or regression" --html=Reports/reports_chrome.html --browser firefox
# pytest -v -s -m "sanity and regression" --html=Reports/reports_chrome.html --browser firefox
# pytest -v -s -m "regression" --html=Reports/reports_chrome.html --browser firefox
# pytest -v -s -m "sanity" --html=Reports/reports_chrome.html --browser firefox
