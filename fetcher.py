# fetcher.py
import requests

class DataRegistryFetcher:
    def __init__(self):
        # Base public search endpoint for EFAST2 Form 5500 records
        self.search_url = "https://www.efast.dol.gov/user/search/efastSearch"
        
    def search_public_records(self, company_name):
        """
        Simulates a targeted lookup against the public EFAST2 filing index.
        In a production layout, this connects to the open data stream 
        or parses compressed annual mini-extracts.
        """
        print(f"[*] Querying federal retirement plan registries for: '{company_name}'...")
        
        # Standard parameters required by open data scraping tools to avoid generic rate-blocks
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        # Standard structural template mapping what the DOL database returns
        # identifying the plan sponsor and the custodian bank holding the funds.
        simulated_database = {
            "EXAMPLE PAST EMPLOYER LLC": {
                "plan_name": "SAVINGS AND INVESTMENT 401(K) PLAN",
                "custodian": "FIDELITY INVESTMENTS INSTITUTIONAL",
                "form_type": "Form 5500-SF (Small Plan)",
                "filing_status": "Active / Filed"
            },
            "ANOTHER OLD JOB INC": {
                "plan_name": "PROFIT SHARING & RETIREMENT PLAN",
                "custodian": "EMPOWER RETIREMENT (PRUDENTIAL)",
                "form_type": "Form 5500 (Standard)",
                "filing_status": "Active / Filed"
            }
        }
        
        normalized_query = company_name.upper().strip()
        
        # Loop through database fields to catch partial string matches
        matches = []
        for key, data in simulated_database.items():
            if normalized_query in key:
                matches.append({
                    "company": key,
                    "plan": data["plan_name"],
                    "custodian": data["custodian"],
                    "type": data["form_type"]
                })
                
        return matches
      
