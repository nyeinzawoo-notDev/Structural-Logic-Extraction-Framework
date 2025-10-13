# tcode_polarity_system.py - Dual-Polarity T-Code Framework

TCODE_POLARITY_SPECTRUM = {
    "T003": {
        "name": "မီး (Fire)",
        "original_myanmar": "အပူ၊ အလင်း၊ စွမ်းအင်၊ ပြောင်းလဲမှု",
        "negative_pole": {
            "description": "အလွန်အမင်း လောင်ကျွမ်းခြင်း",
            "characteristics": ["Destructive", "Uncontrolled", "Consuming", "Volatile"],
            "risk_indicators": ["burnout", "aggression", "recklessness", "instability"],
            "vector_threshold": 0.9
        },
        "positive_pole": {
            "description": "အပူအလင်း ပေးခြင်း", 
            "characteristics": ["Energetic", "Transformative", "Illuminating", "Motivating"],
            "benefit_indicators": ["innovation", "warmth", "progress", "inspiration"],
            "vector_threshold": 0.6
        },
        "balanced_zone": {
            "description": "ထိန်းချုပ်ထားသော စွမ်းအင်",
            "characteristics": ["Sustainable", "Focused", "Purposeful", "Renewing"],
            "optimal_range": [0.4, 0.7]
        }
    },
    "T017": {
        "name": "သီလ (Ethical Boundaries)", 
        "original_myanmar": "အနှောင်အဖွဲ့၊ အစဉ်အလာ၊ ကိုယ်ကျင့်တရား",
        "negative_pole": {
            "description": "အလွန်အမင်း ချည်နှောင်ခြင်း",
            "characteristics": ["Rigid", "Restrictive", "Dogmatic", "Stagnant"],
            "risk_indicators": ["bureaucracy", "resistance_to_change", "judgmental", "inflexible"],
            "vector_threshold": 0.9
        },
        "positive_pole": {
            "description": "ကာကွယ်မှု ပေးခြင်း",
            "characteristics": ["Protective", "Stabilizing", "Guiding", "Secure"],
            "benefit_indicators": ["safety", "integrity", "trust", "consistency"],
            "vector_threshold": 0.6
        },
        "balanced_zone": {
            "description": "ဉာဏ်ပညာဖြင့် ထိန်းညှိခြင်း",
            "characteristics": ["Adaptive", "Principle-based", "Context-aware", "Evolutionary"],
            "optimal_range": [0.3, 0.6]
        }
    }
    # ... Other T-Codes with similar polarity definitions
}
