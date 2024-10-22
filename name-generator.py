import random

class NameGenerator:
    def __init__(self):
        self.first_names = [
            # Traditional names
            "Alexander", "Benjamin", "Catherine", "Diana", "Eleanor", "Frederick",
            # Modern names
            "Kai", "Luna", "Nova", "Phoenix", "Quinn", "Zephyr",
            # Global names
            "Aisha", "Chen", "Diego", "Fatima", "Hassan", "Indira",
            # Scandinavian names
            "Anders", "Bjorn", "Freya", "Henrik", "Ingrid", "Astrid",
            # Celtic names
            "Aoife", "Cian", "Niamh", "Rowan", "Siobhan", "Tadhg"
        ]
        
        self.last_names = [
            # English/American
            "Anderson", "Bradley", "Crawford", "Davidson", "Edwards",
            # Global surnames
            "Kim", "Liu", "Patel", "Rodriguez", "Singh",
            # Occupational surnames
            "Baker", "Fisher", "Mason", "Smith", "Wright",
            # Nature-based surnames
            "Forest", "Rivers", "Stone", "Winter", "Woods",
            # Place-based surnames
            "Cornwall", "Hamilton", "Montgomery", "Richmond", "Wellington"
        ]
        
        self.used_combinations = set()

    def generate_name(self):
        if len(self.used_combinations) >= len(self.first_names) * len(self.last_names):
            return "No more unique combinations available"
            
        while True:
            first = random.choice(self.first_names)
            last = random.choice(self.last_names)
            full_name = f"{first} {last}"
            
            if full_name not in self.used_combinations:
                self.used_combinations.add(full_name)
                return full_name

    def generate_multiple(self, count):
        names = []
        for _ in range(count):
            name = self.generate_name()
            if name == "No more unique combinations available":
                break
            names.append(name)
        return names

# Example usage
generator = NameGenerator()

# Generate a single name
print("Single name:", generator.generate_name())

# Generate multiple names
print("\nMultiple names:")
for name in generator.generate_multiple(5):
    print(name)
