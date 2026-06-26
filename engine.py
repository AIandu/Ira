# engine.py

class AssetHunterEngine:
        def __init__(self, profile):
        self.profile = profile
        self.first = profile["first_name"].upper()
        self.middle = profile["middle_name"].upper()
        self.all_lasts = [ln.upper() for ln in profile["last_names"]]
        

    def generate_identity_matrix(self):
        """Builds every possible variation of your legal name profile."""
        variations = [
            f"{self.first} {self.last}",
            f"{self.first} {self.middle} {self.last}",
            f"{self.first} {self.middle[0]} {self.last}" if self.middle else "",
            f"{self.last}, {self.first}"
        ]
        # Clean out any empty strings and remove duplicates
        return sorted(list(set([v for v in variations if v])))

    def map_search_vectors(self):
        """Assembles names, zip codes, and target companies into search parameters."""
        names = self.generate_identity_matrix()
        locations = self.profile["past_addresses"]
        employers = [emp.upper() for emp in self.profile["target_employers"]]
        
        return {
            "search_names": names,
            "search_locations": locations,
            "search_employers": employers
        }
      
