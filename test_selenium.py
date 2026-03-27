import undetected_chromedriver as uc
from selenium import webdriver
import os

print("=" * 60)
print("SELENIUM & CHROME DIAGNOSTIC TEST")
print("=" * 60)

# Check Python version
import sys
print(f"\n✓ Python version: {sys.version}")

# Check if Chrome is installed
print("\n[1] Checking for Chrome browser...")
chrome_paths = [
    "/usr/bin/google-chrome",
    "/usr/bin/chromium",
    "/usr/bin/chromium-browser",
    "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
]

chrome_found = False
for path in chrome_paths:
    if os.path.exists(path):
        print(f"✅ Chrome found at: {path}")
        chrome_found = True
        break

if not chrome_found:
    print("❌ Chrome NOT found in common locations")
    print("   Common paths checked:")
    for path in chrome_paths:
        print(f"   - {path}")

# Try to open Chrome with undetected_chromedriver
print("\n[2] Attempting to open Chrome with undetected_chromedriver...")
try:
    driver = uc.Chrome()
    print("✅ Chrome opened successfully!")
    
    print("\n[3] Testing browser navigation...")
    driver.get("https://www.google.com")
    print("✅ Successfully navigated to Google!")
    
    print("\n[4] Checking browser info...")
    print(f"✓ Page title: {driver.title}")
    
    driver.quit()
    print("\n✅ ALL TESTS PASSED! Selenium is working correctly.")
    
except Exception as e:
    print(f"\n❌ ERROR: {type(e).__name__}")
    print(f"Message: {e}")
    print(f"\nFull error details:")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 60)
