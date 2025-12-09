def build_benefits_block(benefits):
    return {
        "benefits_list": benefits,
        "benefits_summary": ", ".join(benefits)
    }
