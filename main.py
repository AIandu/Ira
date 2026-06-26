# main.py
from config import USER_PROFILE, REGISTRY_ENDPOINTS
from engine import AssetHunterEngine
from fetcher import DataRegistryFetcher

def run_audit():
    print("=" * 60)
    print("      INITIALIZING PERSONAL RETIREMENT ASSET AUDIT ENGINE      ")
    print("=" * 60)
    
    # 1. Initialize the engine with your configuration profile
    hunter = AssetHunterEngine(USER_PROFILE)
    vectors = hunter.map_search_vectors()
    
    # 2. Initialize the network fetcher
    fetcher = DataRegistryFetcher()
    
    print("\n[STEP 1] Identity Database Vectors Generated:")
    for name in vectors["search_names"]:
        print(f"   -> Name Target: {name}")
        
    print("\n[STEP 2] Target Employer Filing Scanning Phase:")
    found_assets = []
    for emp in vectors["search_employers"]:
        # Run the search via the fetcher module
        results = fetcher.search_public_records(emp)
        if results:
            found_assets.extend(results)
            for r in results:
                print(f"   [+] MATCH FOUND: {r['company']}")
        else:
            print(f"   [-] No direct active index match for: {emp}")
            
    print("\n" + "=" * 60)
    print("                 LIVE DATA AUDIT TARGET RESULTS                ")
    print("=" * 60)
    
    if found_assets:
        for idx, asset in enumerate(found_assets, 1):
            print(f"\nASSET #{idx}")
            print(f"  EMPLOYER:  {asset['company']}")
            print(f"  PLAN COORD: {asset['plan']}")
            print(f"  CUSTODIAN: {asset['custodian']} <--- [CALL THIS BANK]")
            print(f"  FILING:    {asset['type']}")
    else:
        print("\n[-] No database matches isolated. Transitioning to state registry protocols.")
        
    print("\n" + "-" * 60)
    print("MANUAL DEPLOYMENT LINK BLUEPRINT")
    print("-" * 60)
    print(f"1. Run identity vectors against state vaults: {REGISTRY_ENDPOINTS['nc_unclaimed']}")
    print("=" * 60)

if __name__ == "__main__":
    run_audit()
    
