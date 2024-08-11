from playwright_script_generator import PlaywrightScriptGenerator

def main():
    # Example usage of PlaywrightScriptGenerator
    generator = PlaywrightScriptGenerator(
        url="https://example.com",
        browser_type="chromium",
        headless=True,
        screenshot_path="example_screenshot.png"
    )

    # Generate and save the script
    generator.save_script("playwright_script.py")

    # Optionally, run the script directly
    generator.run_script()

if __name__ == "__main__":
    main()

