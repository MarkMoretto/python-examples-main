#!/usr/bin/env python3
"""
Purpose: https://stackoverflow.com/questions/69815544/extracting-multiple-strings-from-body-of-text
Date created: 2021-11-02

Contributor(s):
    Mark M.
"""

import re

sample = """Hi,
This is an automated email to notify you that your store, Store Name , has been temporarily deactivated on DoorDash.
Reason: Auto Triggered
Details: The store has been automatically temporarily deactivated for the day (ends 4AM next day), as the order cancellation rate threshold of 5% for EMAIL protocol has been exceeded
Deactivation Time
Created at: Friday, October 8, 2021 at 10:13 AM CDT
Scheduled end time: Saturday, October 9, 2021 at 4:00 AM CDT
Want to Reactivate?
Merchant portal: click "Resume" on your merchant portal doordash.com/merchant/hours/closures?store_id=2334058
Call us: call DoorDash customer support (650) 681 9470 to end your deactivation early.
Thanks,
DoorDash Merchant team""".strip()

keywords = "Store Name", "Reason", "Created at", "Scheduled end time"

# {a:b or a, b in [line.split(":") for line in sample.splitlines() if str(line).startswith(keywords)]}

data_dict = dict()
results = [line.split(":") for line in sample.splitlines() if str(line).startswith(keywords)]

enty_item = dict()
for r in results:
    data_dict[r[0]] = r[1].strip()

data_dict = dict()

