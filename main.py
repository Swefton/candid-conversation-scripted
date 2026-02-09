from playwright.sync_api import sync_playwright


def fill_resident_form():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://msu.co1.qualtrics.com/jfe/form/SV_6uliglPIZF68XKS")

        if "auth" in page.url:
            print("Auth detected in URL. Starting login process...")

            page.get_by_label("email").fill("")
            page.get_by_role("button", name="Next").click()

            page.get_by_role("button", name="Password").click()

            password_field = page.get_by_label("Password").and_(
                page.get_by_role("textbox")
            )
            password_field.fill("")
            page.get_by_role("button", name="Verify").click()

        # press next
        #
        # resident name label
        #
        # resident email label
        #
        # resident neighborhood drop down menu -> east

        print("Form submitted successfully!")
        browser.close()


if __name__ == "__main__":
    fill_resident_form()
