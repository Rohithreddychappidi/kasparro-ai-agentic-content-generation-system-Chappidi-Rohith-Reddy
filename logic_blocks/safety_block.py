def build_safety_block(side_effects):
    return {
        "side_effects": side_effects,
        "warnings": [
            "Do a patch test before use",
            "Not recommended with strong exfoliants"
        ]
    }
