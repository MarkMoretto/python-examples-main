
"""
Purpose: how would you delete the repetitiveness of these 4 lines in python?
Date created: 2019-11-30
URI: https://stackoverflow.com/questions/59117482/how-would-you-delete-the-repetitiveness-of-these-4-lines-in-python/59117539#59117539

Contributor(s):
    Mark M.
"""






Most_Recent_Net_Income = float(json_r['financials'][0]['Net Income'])
Net_income_1_year = float(json_r['financials'][1]['Net Income'])
Net_income_2_year = float(json_r['financials'][2]['Net Income'])
Net_income_3_year = json_r['financials'][3]['Net Income']
Net_income_4_year = json_r['financials'][4]['Net Income']

output = "Most_Recent_Net_Income = float(json_r['financials'][0]['Net Income'])"
for i in range(1, 5):
    if i < 3:
        output += f"\nNet_income_{i}_year = float(json_r['financials'][{i}]['Net Income'])"
    else:
        output += f"\nNet_income_{i}_year = json_r['financials'][{i}]['Net Income']"

print(output)

[eval(i) for i in output.split('\n')]