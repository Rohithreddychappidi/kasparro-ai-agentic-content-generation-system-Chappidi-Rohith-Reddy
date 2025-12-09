from agents.parser_agent import ParserAgent
from agents.question_generator_agent import QuestionGeneratorAgent
from agents.template_agent import TemplateAgent
from agents.page_assembly_agent import PageAssemblyAgent
from agents.comparison_agent import ComparisonAgent

class Orchestrator:
    def run(self):
        raw_data = {
            "Product Name": "GlowBoost Vitamin C Serum",
            "Concentration": "10% Vitamin C",
            "Skin Type": "Oily, Combination",
            "Key Ingredients": ["Vitamin C", "Hyaluronic Acid"],
            "Benefits": ["Brightening", "Fades dark spots"],
            "How to Use": "Apply 2–3 drops in the morning before sunscreen",
            "Side Effects": "Mild tingling for sensitive skin",
            "Price": "₹699"
        }

        # Product B
        product_b = {
            "name": "DermaShine Brightening Serum",
            "concentration": "8% Vitamin C",
            "skin_type": "Normal, Dry",
            "ingredients": ["Vitamin C", "Aloe Vera"],
            "benefits": ["Hydration", "Mild brightening"],
            "usage": "Apply once daily",
            "side_effects": "None",
            "price": "₹599"
        }

        # Agents
        parser = ParserAgent(raw_data)
        question_agent = QuestionGeneratorAgent()
        template_agent = TemplateAgent()
        saver = PageAssemblyAgent()
        comparison_agent = ComparisonAgent()

        product = parser.parse()

        qs = question_agent.generate(product)
        faq_page = template_agent.generate_faq_page(qs, product)

        product_page = template_agent.generate_product_page(product)
        comparison_page = comparison_agent.generate(product, product_b)

        
        saver.save(faq_page, "output/faq.json")
        saver.save(product_page, "output/product_page.json")
        saver.save(comparison_page, "output/comparison_page.json")
