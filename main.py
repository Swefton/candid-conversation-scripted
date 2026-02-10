import time

import pandas as pd
from playwright.sync_api import sync_playwright


def fill_resident_form():
    # Load data (skipping the first metadata row)
    df = pd.read_csv("CC_filled.csv", skiprows=1, encoding="latin1")
    df["success_date"] = pd.to_datetime(df["success_date"]).dt.strftime("%m/%d/%Y")

    with sync_playwright() as p:
        # slow_mo helps prevent the script from outrunning the page animations
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()

        for index, row in df.iterrows():
            print(f"[{index + 1}/{len(df)}] Filling form for: {row['name']}")

            page.goto("https://msu.co1.qualtrics.com/jfe/form/SV_6uliglPIZF68XKS")
            time.sleep(3)

            # --- Login Logic ---
            if "auth" in page.url:
                print("Login detecting, attempting authorization")
                try:
                    page.get_by_label("email").wait_for(state="visible", timeout=5000)

                    print("Login input visible. Starting login process...")
                    page.get_by_label("email").fill("srivas75")
                    page.get_by_role("button", name="Next").click()

                    page.get_by_role("button", name="Password").click()

                    password_field = page.get_by_label("Password").and_(
                        page.get_by_role("textbox")
                    )
                    password_field.wait_for(state="visible", timeout=45000)
                    password_field.fill("PASSWORD")
                    page.get_by_role("button", name="Verify").click()

                except:
                    print(
                        "Auth URL detected but no login field found. Proceeding to form..."
                    )

            # --- Form Flow ---

            # 1. Start / Page 1
            page.get_by_role("button", name="Next").click()

            # 2. Resident Identity
            page.get_by_label("Resident Name").fill(str(row["name"]))
            page.get_by_label("Resident Email").fill(str(row["email"]))

            # Neighborhood Dropdown (Select "East" as per your flow)
            page.get_by_label("Neighborhood").select_option(
                label=str(row["neighborhood"])
            )
            page.get_by_role("button", name="Next").click()

            # 3. Location Details
            page.get_by_label("Community").select_option(label=str(row["community"]))
            page.get_by_label("Building").select_option(label=str(row["building"]))

            # Room Number (Searchable dropdown)
            page.get_by_role("textbox", name="Search for an option").click()
            page.get_by_role("option", name=str(row["room_number"])).click()

            page.get_by_role("button", name="Next").click()

            # 4. Interaction Result
            page.get_by_label("Please select the").select_option(
                label=str(row["interaction_type"])
            )

            # "Was it successful?" - Logic check
            is_success = str(row["is_successful"]).lower() == "yes"
            page.get_by_text(str(row["is_successful"]).title()).click()
            page.get_by_role("button", name="Next").click()

            # 5. Branching Logic
            if is_success:
                # Success Branch
                date_obj = pd.to_datetime(row["success_date"])
                month_idx = str(date_obj.month - 1)
                year_str = str(date_obj.year)
                day_label = date_obj.strftime("%B %d,").replace(" 0", " ")

                # 2. Open and configure the calendar widget
                page.get_by_role("textbox", name="Candid Conversation Date (if").click()
                page.get_by_label("Month").select_option(month_idx)
                page.get_by_role("spinbutton", name="Year").fill(year_str)
                page.get_by_role("spinbutton", name="Year").press("Enter")

                # 3. Select the specific day
                page.get_by_label(day_label, exact=False).click()

                page.get_by_role("textbox", name="Provide a 2-3 sentence").fill(
                    str(row["success_summary"])
                )
                for keyword in str(row["keywords"]).split(", "):
                    page.get_by_text(keyword).click()

                page.get_by_role("textbox", name="Briefly summarize any").fill(
                    str(row["follow_up_info"])
                )

                page.get_by_role("button", name="Next").click()
            else:
                # Failure Branch
                attempt_mapping = {
                    "1": "#QID44-1-label",
                    "2 to 3": "#QID44-2-label",
                    "4 or more": "#QID44-3-label",
                }

                val = str(row["attempt_count"]).strip()
                page.locator(attempt_mapping[val]).click()

                attempt_dates = str(row["attempt_dates"]).split(",")
                for date_str in attempt_dates:
                    date_obj = pd.to_datetime(date_str.strip())
                    month_idx = str(date_obj.month - 1)
                    year_str = str(date_obj.year)
                    day_label = date_obj.strftime("%B %d,").replace(" 0", " ")

                    page.get_by_role(
                        "textbox", name="Please list the dates you"
                    ).click()
                    page.get_by_label("Month").select_option(month_idx)
                    page.get_by_role("spinbutton", name="Year").fill(year_str)
                    page.get_by_role("spinbutton", name="Year").press("Enter")
                    page.get_by_label(day_label, exact=False).click()

                for strategy in str(row["strategies"]).split(", "):
                    page.get_by_text(strategy).click()

                for challenge in str(row["challenges"]).split(", "):
                    page.get_by_text(challenge).click()

                page.get_by_role("textbox", name="Please provide a narrative").fill(
                    str(row["effort_narrative"])
                )
                page.get_by_role("textbox", name="What do you plan to do").fill(
                    str(row["future_plan"])
                )

            # Final Submit
            time.sleep(2)
            page.get_by_role("button", name="Next").click()
            print(f"Successfully submitted for {row['name']}")
            time.sleep(1)

        browser.close()


if __name__ == "__main__":
    fill_resident_form()
