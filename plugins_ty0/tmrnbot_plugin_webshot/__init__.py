from PIL import Image
from core import *
from plugins.h import h
from playwright.sync_api import Playwright, sync_playwright
import time
@on.message_created
def screenshot(event: Event):
  if event.message.content.startswith("网页截图 "):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(event.message.content[5:])
        time.sleep(5.0)
        screenshot = page.screenshot(path='example.png', full_page=True)
        browser.close()
        event.message_create(content=h.image(screenshot))