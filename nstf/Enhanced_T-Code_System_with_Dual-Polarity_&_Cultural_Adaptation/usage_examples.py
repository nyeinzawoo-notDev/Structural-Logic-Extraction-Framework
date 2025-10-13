# usage_examples.py - Real-World Application Scenarios

def demonstrate_cultural_adaptation():
    """မတူညီသော ယဉ်ကျေးမှုများတွင် T-Code များ၏ အဓိပ္ပာယ် ပြောင်းလဲပုံ"""
    
    adapter = CulturalAdaptationEngine()
    
    # Western Business Context
    western_t003 = adapter.adapt_tcode_interpretation("T003", "western_corporate", "business_ethics")
    print("T003 in Western Business:", western_t003["adapted_meaning"])
    
    # Eastern Philosophical Context  
    eastern_t017 = adapter.adapt_tcode_interpretation("T017", "eastern_philosophical", "personal_development")
    print("T017 in Eastern Philosophy:", eastern_t017["adapted_meaning"])
    
    # Original Myanmar Context
    myanmar_t003 = adapter.adapt_tcode_interpretation("T003", "myanmar_buddhist")
    print("T003 in Myanmar Buddhist:", myanmar_t003["original_myanmar"])

def demonstrate_polarity_balancing():
    """Polarity-based balancing ၏ လက်တွေ့အသုံးချမှုများ"""
    
    balancer = PolarityBalancer()
    
    # Scenario 1: Overly aggressive business expansion
    aggressive_vector = {"T003": 0.92, "T017": 0.15}  # Extreme T003 negative polarity
    assessment = balancer.assess_tcode_polarity(aggressive_vector)
    
    print("Aggressive Expansion Analysis:")
    for tcode, analysis in assessment.items():
        print(f"{tcode}: {analysis['state']} - {analysis['recommendation']}")
    
    # Scenario 2: Balanced sustainable approach  
    balanced_vector = {"T003": 0.55, "T017": 0.45}  # Both in balanced range
    assessment = balancer.assess_tcode_polarity(balanced_vector)
    
    print("\nBalanced Approach Analysis:")
    for tcode, analysis in assessment.items():
        print(f"{tcode}: {analysis['state']} - {analysis['recommendation']}")
