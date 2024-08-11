import streamlit as st
from playwright_script_generator import PlaywrightScriptGenerator

def main():
    st.title("Playwright Script Generator")

    # Collect user inputs
    url = st.text_input("URL", value="https://example.com")
    browser_type = st.selectbox("Browser Type", options=["chromium", "firefox", "webkit"], index=0)
    headless = st.checkbox("Headless Mode", value=True)
    screenshot_path = st.text_input("Screenshot Path", value="screenshot.png")
    file_name = st.text_input("Script File Name", value="generated_script.py")

    # Generate script when button is clicked
    if st.button("Generate Script"):
        generator = PlaywrightScriptGenerator(
            url=url,
            browser_type=browser_type,
            headless=headless,
            screenshot_path=screenshot_path
        )
        generator.save_script(file_name)
        st.success(f"Script generated and saved as {file_name}")

if __name__ == "__main__":
    main()

