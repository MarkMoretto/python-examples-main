
"""
Purpose: Kiva financial query
Date created: 2020-05-04

Could use for predictions or something

Contributor(s):
    Mark M.
"""


import requests

base_url = 'https://api.kivaws.org/graphql?query='

qry = """
{
  lend {
    loans (filters: {gender: female, country: ["KE", "US"]}, limit: 5) {
      totalCount
      values {
        name
        loanAmount
        image {
          url(presetSize: small)
        }
        activity {
          name
        }
        geocode {
          country {
            isoCode
            name
          }
        }
        lenders (limit: 0) {
          totalCount
        }
        ... on LoanPartner {
          partnerName
        }
        ... on LoanDirect {
          trusteeName
        }
      }
    }
  }
}
""".strip()

r = requests.post(base_url+ graphql_query )
r.json()
