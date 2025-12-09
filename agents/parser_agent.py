class ParserAgent:
    def __init__(self, data):
        self.data = data

    def parse(self):
        """Convert raw data into internal normalized model"""
        product = {
            "name": self.data.get("Product Name"),
            "concentration": self.data.get("Concentration"),
            "skin_type": self.data.get("Skin Type"),
            "ingredients": self.data.get("Key Ingredients"),
            "benefits": self.data.get("Benefits"),
            "usage": self.data.get("How to Use"),
            "side_effects": self.data.get("Side Effects"),
            "price": self.data.get("Price")
        }
        return product
