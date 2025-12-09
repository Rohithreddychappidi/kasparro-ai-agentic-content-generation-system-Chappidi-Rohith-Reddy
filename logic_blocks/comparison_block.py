def compare_products(a, b):
    return {
        "price_comparison": f"{a['price']} vs {b['price']}",
        "ingredient_overlap": list(set(a["ingredients"]) & set(b["ingredients"])),
        "benefit_difference": {
            "product_a": a["benefits"],
            "product_b": b["benefits"]
        }
    }
