# polarity_balancer.py - Intelligent T-Code Equilibrium System

class PolarityBalancer:
    def __init__(self):
        self.polarity_thresholds = {
            "extreme_negative": 0.85,
            "moderate_negative": 0.70, 
            "balanced_range": [0.35, 0.65],
            "moderate_positive": 0.70,
            "extreme_positive": 0.85
        }
    
    def assess_tcode_polarity(self, vector_scores):
        """T-Code များ၏ polarity အခြေအနေကို အကဲဖြတ်ပါ"""
        
        polarity_assessment = {}
        
        for tcode, score in vector_scores.items():
            polarity_info = TCODE_POLARITY_SPECTRUM.get(tcode, {})
            if not polarity_info:
                continue
            
            # Determine polarity state
            if score >= self.polarity_thresholds["extreme_negative"]:
                polarity_state = "EXTREME_NEGATIVE"
                recommendation = self._generate_correction_recommendation(tcode, "extreme_negative")
            elif score >= self.polarity_thresholds["moderate_negative"]:
                polarity_state = "MODERATE_NEGATIVE" 
                recommendation = self._generate_correction_recommendation(tcode, "moderate_negative")
            elif self.polarity_thresholds["balanced_range"][0] <= score <= self.polarity_thresholds["balanced_range"][1]:
                polarity_state = "BALANCED"
                recommendation = "Maintain current balance"
            elif score >= self.polarity_thresholds["moderate_positive"]:
                polarity_state = "MODERATE_POSITIVE"
                recommendation = self._generate_optimization_recommendation(tcode, "moderate_positive")
            else:
                polarity_state = "EXTREME_POSITIVE"
                recommendation = self._generate_optimization_recommendation(tcode, "extreme_positive")
            
            polarity_assessment[tcode] = {
                "score": score,
                "state": polarity_state,
                "recommendation": recommendation,
                "optimal_range": polarity_info["balanced_zone"]["optimal_range"]
            }
        
        return polarity_assessment
    
    def _generate_correction_recommendation(self, tcode, polarity_level):
        """Negative polarity အတွက် ညှိပေးရန် အကြံပြုချက်များ"""
        
        correction_strategies = {
            "T003": {
                "extreme_negative": "Immediate intervention required: Introduce T017 containment and mindfulness practices",
                "moderate_negative": "Moderate correction: Balance with meditation, ethical reflection, and sustainable planning"
            },
            "T017": {
                "extreme_negative": "Immediate intervention: Introduce T003 creative energy and flexibility exercises", 
                "moderate_negative": "Moderate correction: Balance with innovation sessions and adaptive thinking"
            }
        }
        
        return correction_strategies.get(tcode, {}).get(polarity_level, "Consult ethical framework")
    
    def _generate_optimization_recommendation(self, tcode, polarity_level):
        """Positive polarity အတွက် ပိုမိုကောင်းမွန်စေရန် အကြံပြုချက်များ"""
        
        optimization_strategies = {
            "T003": {
                "extreme_positive": "Harness energy for transformative leadership and innovation",
                "moderate_positive": "Channel energy into focused growth and inspired action"
            },
            "T017": {
                "extreme_positive": "Leverage stability for long-term foundation building",
                "moderate_positive": "Use ethical framework for consistent quality and trust-building"
            }
        }
        
        return optimization_strategies.get(tcode, {}).get(polarity_level, "Continue current approach")
