from helper_functions import clear_screen
clear_screen()

# ============================
# INSTALLING PACKAGES WITH PIP
# ============================

'''
FIRST:
In the terminal, run one of these to install playwright:
    pip install playwright
    py -m pip install playwright
    pip3 install playwright
    python -m pip install playwright
    python3 -m pip install playwright
    
SECOND:
In the terminal, run one of these to have playwright install web browsers on your computer:
    playwright install
    py -m playwright install
    python -m playwright install
    python3 -m playwright install
'''

from playwright.sync_api import sync_playwright
print("If this prints, that means you installed the playwright package correctly")

with sync_playwright() as p:
    p.chromium.launch() 
print("If this prints, that means you ran 'playwright install' in the terminal correctly")


