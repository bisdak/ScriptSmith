from playwright_template import script_template

class PlaywrightScriptGenerator:
    def __init__(self, url, browser_type="chromium", headless=True, screenshot_path="screenshot.png"):
        self.url = url
        self.browser_type = browser_type
        self.headless = headless
        self.screenshot_path = screenshot_path

    def generate_script(self):
        # Dictionary of dynamic values
        values = {
            "url": self.url,
            "browser_type": self.browser_type,
            "headless": str(self.headless),  # Convert boolean to string
            "screenshot_path": self.screenshot_path
        }
        # Substitute values in the template
        return script_template.substitute(values)

    def save_script(self, file_name="generated_script.py"):
        # Generate the script
        script_content = self.generate_script()
        # Save it to a file
        with open(file_name, 'w') as file:
            file.write(script_content)
        print(f"Script saved to {file_name}")

    def run_script(self):
        # Execute the generated script directly
        exec(self.generate_script())