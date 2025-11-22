from playwright.sync_api import sync_playwright

# --- CONFIGURATION SECTION (EDIT THIS) ---
TARGET_WEBSITE = "https://www.bhphotovideo.com" # The site blocking you
OUTPUT_FILE = "auth.json"                       # Where to save the magic pass
# -----------------------------------------

def generate_human_pass():
    # Standard Modern User Agent (Update this if it's year 2026+)
    UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"

    with sync_playwright() as p:
        # 1. Launch with "AutomationControlled" disabled
        browser = p.chromium.launch(
            headless=False, 
            args=["--disable-blink-features=AutomationControlled"]
        )
        
        context = browser.new_context(user_agent=UA)

        # 2. Remove the 'webdriver' property so Cloudflare doesn't hide the box
        context.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });
        """)

        page = context.new_page()
        
        print(f"🚀 Opening {TARGET_WEBSITE}...")
        page.goto(TARGET_WEBSITE)
        
        print("\n" + "!"*60)
        print(f"🛑 HUMAN INTERVENTION NEEDED FOR: {TARGET_WEBSITE}")
        print("1. Solve any Captchas or Cloudflare boxes manually.")
        print("2. Ensure the actual website content is visible.")
        print("3. Come back here and press ENTER.")
        print("!"*60 + "\n")
        
        input("Press Enter to save the credentials...") 
        
        # 3. Save the file
        context.storage_state(path=OUTPUT_FILE)
        print(f"✅ Credentials saved to '{OUTPUT_FILE}'. You can now use this in your scraper.")
        
        browser.close()

if __name__ == "__main__":
    generate_human_pass()
