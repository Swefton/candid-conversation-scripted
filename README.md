# candid-conversation-scripted

Declaratively fill up candid conversations

# Installation / Usage

* Setup `.venv` with requirements.txt
* Run `playwright install`
* Replace `email` and `password` appropriately so that the script can login to qualtrics to submit the form
* Setup `cc.csv` with appropriate information
* Run `python main.py`

> [!note]
> The `cc.csv` has a strict expectation for data input, consult the table below.

# Schema for `CC.csv`

| Column Name | Data Type | Description | All Possible / Example Values |
| --- | --- | --- | --- |
| **name** | str | Full name of the resident. | e.g., Sparty |
| **email** | str | University email address. | e.g., sparty@msu.edu |
| **neighborhood** | str | Campus neighborhood. | East |
| **community** | str | Resident hall community. | Akers |
| **building** | str | Specific building name. | West Akers, East Akers |
| **room_number** | str | Resident's room identifier. | e.g., AKW-575 |
| **interaction_type** | int | Candid conversation number. | 3 |
| **is_successful** | str | If a conversation occurred. | yes, no |

## Table to fill if outreach was successful
| Column Name | Data Type | Description | All Possible / Example Values |
| --- | --- | --- | --- |
| **success_date** | date | Date of interaction (MM/DD/YY). | e.g., 01/20/26 |
| **success_summary** | str | Narrative of the talk (min 2–3 sentences). | 2/3 sentences describing what you talked about. |
| **keywords** | str | Primary Topic. | Pick one from here - Academic challenges, Academic success, Campus navigation, Campus resources, Career or professional development, Conflict management, Cross cultural engagement, Involvement, Mental or emotional or physical or spiritual well being, Relationship building, Sense of belonging |
| **follow_up_info** | str | Future action notes. | eg. Follow up to give resident xyz resource. |

## Table to fill if outreach was unsuccessful
| Column Name | Data Type | Description | All Possible / Example Values |
| --- | --- | --- | --- |
| **attempt_count** | str | Number of failed attempts. | Pick one from -  1, 2 to 3, 4 or more |
| **attempt_dates** | str | Dates of outreach attempts. | Comma-separated list (e.g., 01/22/26, 01/24/26) |
| **strategies** | str | Method of Outreach. | Pick one from here - Knocked on door, Text message, Email, Social media or messaging app |
| **challenges** | str | Barrier to Interaction. | Pick one from here - Scheduling conflicts, Resident declined or avoided interaction, Resident seemed disinterested or disengaged, Resident was unavailable |
| **effort_narrative** | str | Outreach explanation. | 1–2 sentences explaining how you tried to reach out to resident. |
| **future_plan** | str | Next steps for contact. | e.g., "Find more time to speak in the hallway" |
