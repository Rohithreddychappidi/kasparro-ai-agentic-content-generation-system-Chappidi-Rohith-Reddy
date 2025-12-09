def generate_answer(question, product):
    name = product["name"]

    # Usage related answers
    if "apply" in question.lower() or "use" in question.lower():
        return product["usage"]

    if "sunscreen" in question.lower():
        return "Yes, you must apply sunscreen after using this serum because Vitamin C increases sun sensitivity."

    # Ingredient related answers
    if "ingredient" in question.lower():
        ingredients = ", ".join(product["ingredients"])
        return f"It contains the following key ingredients: {ingredients}."

    # Skin suitability answers
    if "oily" in question.lower() or "skin" in question.lower():
        return f"It is suitable for {product['skin_type']} skin types."

    # Side effects / safety
    if "irritation" in question.lower() or "safe" in question.lower() or "sensitive" in question.lower():
        return f"Possible side effects include: {product['side_effects']}."

    # Price
    if "price" in question.lower():
        return f"The price of {name} is {product['price']}."

    # Comparison question (generic)
    if "different" in question.lower() or "better" in question.lower():
        return f"{name} focuses on {', '.join(product['benefits'])}. It is designed for {product['skin_type']}."

    # Generic fallback
    return f"{name} is designed to improve your skin health and provide visible results with regular use."
