# emotional_vector_integration.py - Dynamic Weighting System

class EmotionalVectorIntegrator:
    def __init__(self):
        self.emotion_tcode_correlations = {
            "fear_anxiety": {
                "primary_effect": "Amplifies T017 (Containment) by 0.3",
                "secondary_effect": "Reduces T007 (Flexibility) by 0.2",
                "adaptive_response": "Mindfulness to balance T005-T007 polarity"
            },
            "anger_frustration": {
                "primary_effect": "Amplifies T003 (Expansion) by 0.4", 
                "secondary_effect": "Reduces T017 (Containment) by 0.3",
                "adaptive_response": "Metta practice to integrate T003 with T017"
            },
            "sadness_grief": {
                "primary_effect": "Amplifies T005 (Water) by 0.3",
                "secondary_effect": "Reduces T003 (Expansion) by 0.2",
                "adaptive_response": "Compassionate acceptance to transform T005"
            },
            "joy_excitement": {
                "primary_effect": "Amplifies T007 (Air) by 0.3",
                "secondary_effect": "Reduces T017 (Containment) by 0.1", 
                "adaptive_response": "Grounded celebration to maintain balance"
            }
        }
    
    def adjust_nstf_weights(self, base_vector, primary_emotion, emotional_intensity):
        """Emotional state အပေါ် အခြေခံပြီး NSTF vector weights ကို ညှိပေးပါ"""
        
        adjusted_vector = base_vector.copy()
        emotion_correlation = self.emotion_tcode_correlations.get(primary_emotion, {})
        
        if not emotion_correlation:
            return adjusted_vector
        
        # Calculate adjustment based on emotional intensity (0-10 scale)
        intensity_factor = emotional_intensity / 10.0
        
        # Apply primary effect
        primary_effect = emotion_correlation["primary_effect"]
        tcode, effect = self._parse_effect(primary_effect)
        if tcode in adjusted_vector:
            adjusted_vector[tcode] = self._apply_adjustment(
                adjusted_vector[tcode], effect, intensity_factor
            )
        
        # Apply secondary effect  
        secondary_effect = emotion_correlation["secondary_effect"]
        tcode, effect = self._parse_effect(secondary_effect)
        if tcode in adjusted_vector:
            adjusted_vector[tcode] = self._apply_adjustment(
                adjusted_vector[tcode], effect, intensity_factor
            )
        
        return adjusted_vector
    
    def _parse_effect(self, effect_string):
        """Effect description မှ T-Code နှင့် adjustment value ကို ခွဲထုတ်ပါ"""
        # "Amplifies T017 (Containment) by 0.3" -> ("T017", 0.3)
        # "Reduces T007 (Flexibility) by 0.2" -> ("T007", -0.2)
        parts = effect_string.split()
        tcode = parts[1] if "Amplifies" in effect_string or "Reduces" in effect_string else None
        value = float(parts[-1])
        
        if "Reduces" in effect_string:
            value = -value
            
        return tcode, value
    
    def _apply_adjustment(self, current_value, adjustment, intensity_factor):
        """Adjustment value ကို intensity factor ဖြင့် apply လုပ်ပါ"""
        new_value = current_value + (adjustment * intensity_factor)
        return max(0.0, min(1.0, new_value))  # Clamp between 0-1
