# cultural_adaptation_engine.py - Universal T-Code Interpretation

class CulturalAdaptationEngine:
    def __init__(self):
        self.cultural_contexts = {
            "myanmar_buddhist": {
                "T003": {"primary_meaning": "မီးတရား - တဏှာ၊ ဒေါသ၊ မောဟ"},
                "T017": {"primary_meaning": "သီလ - ကိုယ်ကျင့်တရား အခြေခံ"},
                "interpretation_style": "holistic_spiritual"
            },
            "western_corporate": {
                "T003": {"primary_meaning": "Innovation Drive & Growth Energy"},
                "T017": {"primary_meaning": "Compliance Framework & Ethical Governance"}, 
                "interpretation_style": "practical_operational"
            },
            "eastern_philosophical": {
                "T003": {"primary_meaning": "Yang Energy - Active, Creative, Expanding"},
                "T017": {"primary_meaning": "Yin Structure - Receptive, Stabilizing, Containing"},
                "interpretation_style": "balance_harmony"
            }
        }
        
        self.domain_mappings = {
            "business_ethics": {
                "T003": "Market Expansion & Profit Motive",
                "T017": "Regulatory Compliance & Corporate Responsibility"
            },
            "personal_development": {
                "T003": "Ambition & Personal Growth", 
                "T017": "Self-Discipline & Moral Principles"
            },
            "environmental_sustainability": {
                "T003": "Economic Development",
                "T017": "Ecological Preservation"
            }
        }
    
    def adapt_tcode_interpretation(self, tcode, cultural_context="universal", domain=None):
        """T-Code ၏ အဓိပ္ပာယ်ကို ယဉ်ကျေးမှုနှင့် နယ်ပယ်အလိုက် ညှိပေးပါ"""
        
        base_definition = TCODE_POLARITY_SPECTRUM.get(tcode, {})
        if not base_definition:
            return base_definition
        
        # Cultural Adaptation
        cultural_meaning = self.cultural_contexts.get(cultural_context, {})
        if cultural_meaning and tcode in cultural_meaning:
            adapted_meaning = cultural_meaning[tcode]["primary_meaning"]
        else:
            adapted_meaning = base_definition["name"]
        
        # Domain-Specific Mapping
        domain_meaning = ""
        if domain and domain in self.domain_mappings and tcode in self.domain_mappings[domain]:
            domain_meaning = self.domain_mappings[domain][tcode]
        
        return {
            "original_myanmar": base_definition.get("original_myanmar", ""),
            "adapted_meaning": adapted_meaning,
            "domain_specific": domain_meaning,
            "polarity_spectrum": {
                "negative_pole": base_definition["negative_pole"],
                "positive_pole": base_definition["positive_pole"], 
                "balanced_zone": base_definition["balanced_zone"]
            }
        }
