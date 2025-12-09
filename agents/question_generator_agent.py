class QuestionGeneratorAgent:
    def generate(self, product):
        name = product["name"]

        questions = [
            # Informational
            f"What is {name}?",
            f"What ingredients does {name} contain?",
            f"Is {name} suitable for oily skin?",

            # Usage
            f"How to apply {name}?",
            f"Can I use {name} at night?",
            f"Should I use sunscreen with {name}?",

            # Safety
            f"Does {name} cause irritation?",
            f"Is {name} safe for sensitive skin?",

            # Purchase
            f"What is the price of {name}?",
            f"How long does one bottle of {name} last?",

            # Comparison
            f"How is {name} different from other serums?",
            f"Is {name} better than similar Vitamin C serums?"
        ]

        return questions[:15]
