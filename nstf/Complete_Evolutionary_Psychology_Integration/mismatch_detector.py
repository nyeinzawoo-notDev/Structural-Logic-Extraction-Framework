# mismatch_detector.py - Modern Problems vs Ancient Wiring

class MismatchDetector:
    def __init__(self):
        self.mismatch_patterns = {
            "information_overload": {
                "ancient_environment": "Limited information from immediate surroundings",
                "modern_reality": "Constant digital stimulation and information abundance", 
                "instinctive_response": "T005 (Water) - Attempt to absorb everything, leading to overwhelm",
                "nstf_conflict": "T005 (Depth) vs T007 (Flexibility) - Drowning in data vs need for selective attention",
                "adaptive_solution": "Conscious information diet with T017 boundaries"
            },
            "social_comparison": {
                "ancient_environment": "Comparison with 50-100 tribe members",
                "modern_reality": "Comparison with thousands on social media",
                "instinctive_response": "T003 (Fire) - Status anxiety and competitive drive amplification",
                "nstf_conflict": "T003 (Expansion) without T017 (Containment) - Unlimited comparison targets",
                "adaptive_solution": "T017 ethical boundaries on social consumption + T009 (Contentment) cultivation"
            },
            "chronic_stress": {
                "ancient_environment": "Acute physical threats with recovery periods",
                "modern_reality": "Chronic psychological stressors without resolution",
                "instinctive_response": "T005 (Water) - Constant vigilance and threat anticipation",
                "nstf_conflict": "T005 (Containment) blocking T007 (Flow) - Stagnation in stress response",
                "adaptive_solution": "T007 mindfulness practices to break stress cycles"
            }
        }
    
    def detect_mismatch(self, user_situation, emotional_intensity):
        """User ၏ ပြဿနာကို mismatch theory အရ ခွဲခြမ်းစိတ်ဖြာပါ"""
        
        detected_mismatches = []
        
        for pattern_name, pattern in self.mismatch_patterns.items():
            if self._pattern_matches_situation(pattern_name, user_situation):
                mismatch_analysis = {
                    "pattern": pattern_name,
                    "ancient_wiring": pattern["instinctive_response"],
                    "modern_challenge": pattern["modern_reality"],
                    "nstf_tension": pattern["nstf_conflict"],
                    "intensity_factor": emotional_intensity,
                    "adaptive_strategy": pattern["adaptive_solution"]
                }
                detected_mismatches.append(mismatch_analysis)
        
        return detected_mismatches
    
    def _pattern_matches_situation(self, pattern_name, user_situation):
        """User situation နှင့် mismatch pattern ကိုက်ညီမှုရှိမရှိ စစ်ဆေးပါ"""
        # Pattern matching logic based on keywords and context
        pattern_keywords = {
            "information_overload": ["overwhelm", "too much information", "digital", "notification"],
            "social_comparison": ["compare", "social media", "better than", "success", "achievement"],
            "chronic_stress": ["always stressed", "can't relax", "constant pressure", "burnout"]
        }
        
        keywords = pattern_keywords.get(pattern_name, [])
        return any(keyword in user_situation.lower() for keyword in keywords)
