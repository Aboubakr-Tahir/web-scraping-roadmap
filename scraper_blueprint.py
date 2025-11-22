from playwright.sync_api import sync_playwright

# --- 1. CONFIGURATION SECTION (EDIT THIS PER SITE) ---
TARGET_URL = "https://www.bhphotovideo.com/c/product/1840289-REG/canon_6536c002_eos_r5_mark_ii.html"
AUTH_FILE = "auth.json"  # Must match the filename from Step 1

# ⚠️ CRITICAL: This MUST be identical to the UA used in Step 1.
# If you change it here, Cloudflare will reject your key.
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
# -----------------------------------------------------

def run_vip_scraper():
    with sync_playwright() as p:
        # 2. SETUP (Standard Stealth Launch)
        # We use the same stealth args as Step 1 to ensure our fingerprint matches
        browser = p.chromium.launch(
            headless=False, # Keep False to look human. Set to True only if testing confirms it works.
            args=["--disable-blink-features=AutomationControlled"]
        )
        
        # 3. INJECT THE VIP KEY (storage_state)
        # This loads your saved cookies & local storage instantly
        context = browser.new_context(
            storage_state=AUTH_FILE, 
            user_agent=UA 
        )
        
        # Apply the webdriver fix here too, just to be safe
        context.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
        """)
        
        page = context.new_page()
        
        print(f"🚀 Visiting {TARGET_URL} with VIP Pass...")
        page.goto(TARGET_URL)
        
        # 4. THE BUSINESS LOGIC (EDIT THIS PER SITE)
        try:
            # A. VERIFICATION: Wait for an element that ONLY appears if you are logged in/passed
            # For B&H, it's the product title. For Amazon, it might be '#productTitle'.
            # This confirms Cloudflare didn't block us.
            print("⏳ Verifying access...")
            page.wait_for_selector('h1[data-selenium="productTitle"]', timeout=10000)
            
            # B. EXTRACTION: Grab the data you want
            title = page.locator('h1[data-selenium="productTitle"]').inner_text()
            
            # Example of handling missing data (like price) safely
            if page.locator('.price').count() > 0:
                price = page.locator('.price').first.inner_text()
            else:
                price = "Price not found"
            
            print("-" * 30)
            print(f"✅ DATA SECURED:")
            print(f"Title: {title}")
            print(f"Price: {price}")
            print("-" * 30)
            
        except Exception as e:
            print(f"❌ FAILED: Cloudflare rejected the key or the selector was wrong.")
            print(f"Error details: {e}")
            print("👉 SOLUTION: Run '1_get_access.py' again to refresh 'auth.json'.")
            
        browser.close()

if __name__ == "__main__":
    run_vip_scraper()
