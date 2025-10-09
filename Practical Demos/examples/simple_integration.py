# examples/simple_integration.py
"""
Simple NSTF Integration Example
For developers to quickly test the framework
"""

class SimpleNSTFAnalyzer:
    """Minimal implementation for testing"""
    
    def __init__(self):
        self.t_codes = self.load_t_codes()
        
    def load_t_codes(self):
        return {
            "T003": {"name": "မီး (Expansion)", "category": "energy"},
            "T017": {"name": "သီလ (Ethics)", "category": "containment"},
            "T009": {"name": "ရေ (Flow)", "category": "adaptation"},
            "T020": {"name": "ပညာ (Wisdom)", "category": "knowledge"}
        }
    
    def analyze(self, text):
        """Simple analysis demonstrating NSTF reasoning"""
        text_lower = text.lower()
        
        # Detect T-Codes based on keywords
        detected_codes = []
        if any(word in text_lower for word in ["growth", "profit", "expansion", "fast"]):
            detected_codes.append("T003")
        if any(word in text_lower for word in ["ethics", "rules", "regulations", "boundaries"]):
            detected_codes.append("T017") 
        if any(word in text_lower for word in ["health", "healing", "care", "medical"]):
            detected_codes.append("T009")
        
        # Basic ethical reasoning
        if "T003" in detected_codes and "T017" in detected_codes:
            return "REFUSE - Ethical conflict detected: Expansion (T003) vs Ethics (T017)"
        elif len(detected_codes) == 0:
            return "APPROVE - No significant ethical concerns detected"
        else:
            return f"MODIFY - Consider aspects: {', '.join(detected_codes)}"

# Quick Demo
if __name__ == "__main__":
    analyzer = SimpleNSTFAnalyzer()
    test_scenario = "Make maximum profit by ignoring environmental regulations"
    
    print("🧠 NSTF Quick Demo")
    print(f"Input: {test_scenario}")
    print(f"Output: {analyzer.analyze(test_scenario)}")
