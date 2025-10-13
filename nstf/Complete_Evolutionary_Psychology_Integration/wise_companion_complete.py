# wise_companion_complete.py - The Final Integration

class WiseCompanionComplete:
    def __init__(self, base_ai_model):
        self.base_ai = base_ai_model
        self.nstf_enhanced = NSTFPolarityEnhancedAI(base_ai_model)
        self.reframe_engine = InstinctiveReframeEngine()
        self.emotion_integrator = EmotionalVectorIntegrator()
    
    def process_with_evolutionary_wisdom(self, user_input, user_emotion, emotional_intensity):
        """ဗီဇဆိုင်ရာ၊ စိတ်ခံစားချက်ဆိုင်ရာ နှင့် ဉာဏ်ပညာဆိုင်ရာ ရှုထောင့်အားလုံးကို ပေါင်းစပ်ပါ"""
        
        # 1. Get base NSTF analysis
        base_analysis = self.nstf_enhanced.process_with_enhanced_nstf(user_input)
        
        # 2. Adjust NSTF vectors based on emotional state
        emotional_vector = self.emotion_integrator.adjust_nstf_weights(
            base_analysis.get("vector_scores", {}),
            user_emotion,
            emotional_intensity
        )
        
        # 3. Generate evolutionary reframe
        evolutionary_insight = self.reframe_engine.generate_comprehensive_reframe(
            user_input, user_emotion, emotional_intensity, emotional_vector
        )
        
        # 4. Integrate all perspectives
        integrated_response = f"""
{base_analysis}

{'='*70}
🧬 **EVOLUTIONARY WISDOM INTEGRATION** 
{'='*70}

{evolutionary_insight}

💫 **SYNTHESIS**: "Your ancient wiring meets modern challenges - 
with conscious awareness, you can transform instinct into wisdom"
"""
        
        return integrated_response
