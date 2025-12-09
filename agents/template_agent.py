import json
from logic_blocks.benefits_block import build_benefits_block
from logic_blocks.usage_block import build_usage_block
from logic_blocks.safety_block import build_safety_block
from logic_blocks.faq_answer_block import generate_answer

class TemplateAgent:
    def __init__(self):
        pass

    def generate_product_page(self, product):
        return {
            "name": product["name"],
            "ingredients": product["ingredients"],
            "benefits_block": build_benefits_block(product["benefits"]),
            "usage_block": build_usage_block(product["usage"]),
            "safety_block": build_safety_block(product["side_effects"]),
            "price": product["price"]
        }



    
    def generate_faq_page(self, questions, product):
        faqs = []

        for q in questions:
            answer = generate_answer(q, product)
            faqs.append({
                "question": q,
                "answer": answer
            })

        return {"faqs": faqs}
