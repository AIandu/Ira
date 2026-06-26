# main.py
from config import USER_PROFILE, REGISTRY_ENDPOINTS
from engine import AssetHunterEngine

def run_audit():
    print("=" * 60)
    print("      INITIALIZING PERSONAL RETIREMENT ASSET AUDIT ENGINE      ")
    print("=" * 60)
    
    # Initialize the engine with your profile configuration
    hunter = AssetHunterEngine(USER_PROFILE)
    vectors = hunter.map_search_vectors()
    
    print("\n[STEP 1] Identity Database Vectors Generated:")
    for name in vectors["search_names"]:
        print(f"   -> Name Target: {name}")
        
    print("\n[STEP 2] Location Filters Extracted:")
    for loc in vectors["search_locations"]:
        print(f"   -> Location: {loc['city']}, {loc['state']} {loc['zip']}")
        
    print("\n[STEP 3] Employer Filing Target Profiles:")
    for emp in vectors["search_employers"]:
        print(f"   -> Employer: {emp}")
        
    print("\n" + "-" * 60)
    print("MANUAL AUDIT ACTION BLUEPRINT")
    print("-" * 60)
    print(f"1. Run name targets against state vault: {REGISTRY_ENDPOINTS['nc_unclaimed']}")
    print(f"2. Cross-reference company Form 5500 filings via: {REGISTRY_ENDPOINTS['dol_efast']}")
    print("=" * 60)

if __name__ == "__main__":
    run_audit()
  
