from logic_blocks.comparison_block import compare_products

class ComparisonAgent:
    def generate(self, product_a, product_b):
        comparison = compare_products(product_a, product_b)

        return {
            "product_a": product_a,
            "product_b": product_b,
            "comparison": comparison
        }
