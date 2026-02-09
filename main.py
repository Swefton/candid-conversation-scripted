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
        #
        # next
        #
        # community drop down -> akers
        #
        # building drop down -> west akers
        #
        # room number drop down with search bar
        #
        # next
        #
        # corresponding interaction -> 3
        #
        # was it successful? -> drop down bool
        #
        # next
        #
        # if it was successful:
        #
        ## candid conversation date -> calendar type deal
        ##
        ## 2/3 sentence summary
        ##
        ## keywords selection
        ##
        ## briefly summarize information that was shared that would warrant follow up
        ##
        ## next
        #
        # if it wasn't successful
        #
        # how many times did you attempt to engage? 1/2 to 3/4 or more
        #
        # list the dates you attempted to engage with the resident - multiple date objects
        #
        # which strategies did you use - drop down for knocked on door, text message, email, social media or messaging app
        #
        # conversation challenges - multi box for resident declined or avoided interaction, resident seemed disinterested or disengaged, scheduling conflict, resident was unavailable
        #
        # provide a narrative summary of your efforts and challenges to complete the conversation
        #
        # what do you plan to do differently to increase the changes of a successful conversation for future candid conversations
        #
        # next to submit

        print("Form submitted successfully!")
        browser.close()


if __name__ == "__main__":
    fill_resident_form()
