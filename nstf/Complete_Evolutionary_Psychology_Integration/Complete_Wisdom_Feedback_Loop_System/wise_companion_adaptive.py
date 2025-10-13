# wise_companion_adaptive.py - Learning-Enhanced System

class WiseCompanionAdaptive:
    def __init__(self, base_ai_model):
        self.base_ai = base_ai_model
        self.nstf_enhanced = NSTFPolarityEnhancedAI(base_ai_model)
        self.reframe_engine = InstinctiveReframeEngine()
        self.emotion_integrator = EmotionalVectorIntegrator()
        self.feedback_loop = WisdomFeedbackLoop()
        
        # Adaptive learning storage
        self.user_profiles = {}
        self.effectiveness_patterns = {}
    
    def process_with_adaptive_wisdom(self, user_input, user_emotion, emotional_intensity, user_id, session_context=""):
        """Feedback loop integrated wisdom processing"""
        
        # Initialize or retrieve session
        if user_id not in self.user_profiles:
            session_id = self.feedback_loop.initialize_session(user_id, session_context)
            self.user_profiles[user_id] = {
                "current_session": session_id,
                "historical_efficacy": [],
                "preferred_guidance_styles": []
            }
        else:
            session_id = self.user_profiles[user_id]["current_session"]
        
        # Get current session data for context-aware adaptation
        session_data = self.feedback_loop.session_data.get(session_id, {})
        historical_effectiveness = self._analyze_historical_effectiveness(user_id)
        
        # Generate wisdom guidance with historical context
        wisdom_response = self._generate_context_aware_guidance(
            user_input, user_emotion, emotional_intensity, historical_effectiveness
        )
        
        # Extract current vector state for logging
        current_vector = self._extract_vector_from_response(wisdom_response)
        
        # Prepare response with learning context
        enhanced_response = f"""
{wisdom_response}

📊 **LEARNING CONTEXT**:
{self._generate_learning_context(historical_effectiveness)}

🔄 **FEEDBACK INVITATION**: 
Reflect on this guidance - your response will help me better support your growth journey.
"""
        
        return {
            "response": enhanced_response,
            "session_id": session_id,
            "current_vector": current_vector,
            "learning_metrics": historical_effectiveness
        }
    
    def process_user_feedback(self, session_id, user_response, emotional_state, user_actions_taken=""):
        """User ၏ တုံ့ပြန်မှုကို process လုပ်ပြီး system ကို update လုပ်ပါ"""
        
        # Log the interaction and calculate efficacy
        session = self.feedback_loop.session_data.get(session_id)
        if not session:
            return {"error": "Invalid session"}
        
        last_interaction = session["interactions"][-1] if session["interactions"] else None
        
        feedback_result = self.feedback_loop.log_interaction(
            session_id,
            last_interaction["user_input"] if last_interaction else "Initial context",
            last_interaction["ai_guidance_content"] if last_interaction else "Initial guidance",
            user_response,
            emotional_state
        )
        
        # Generate adaptive insights
        insights = self.feedback_loop.generate_adaptive_insights(session_id)
        
        # Update user profile based on learning
        self._update_user_learning_profile(session_id, insights, feedback_result)
        
        return {
            "feedback_processed": True,
            "efficacy_score": feedback_result["efficacy_score"],
            "adaptive_insights": insights,
            "next_session_recommendations": self._generate_next_session_recommendations(insights)
        }
    
    def _analyze_historical_effectiveness(self, user_id):
        """User ၏ အတိတ် efficacy data ကို ခွဲခြမ်းစိတ်ဖြာပါ"""
        
        profile = self.user_profiles.get(user_id, {})
        historical_efficacy = profile.get("historical_efficacy", [])
        
        if not historical_efficacy:
            return {
                "effectiveness_level": "EXPLORATORY",
                "preferred_approaches": [],
                "growth_momentum": "INITIAL"
            }
        
        avg_efficacy = sum(historical_efficacy) / len(historical_efficacy)
        
        if avg_efficacy >= 0.7:
            effectiveness_level = "HIGH_EFFICACY"
        elif avg_efficacy >= 0.4:
            effectiveness_level = "MODERATE_EFFICACY" 
        else:
            effectiveness_level = "LOW_EFFICACY"
        
        return {
            "effectiveness_level": effectiveness_level,
            "average_efficacy_score": avg_efficacy,
            "preferred_approaches": profile.get("preferred_guidance_styles", []),
            "growth_momentum": self._assess_growth_momentum(historical_efficacy),
            "session_count": len(historical_efficacy)
        }
    
    def _generate_context_aware_guidance(self, user_input, user_emotion, emotional_intensity, historical_context):
        """Historical context အပေါ် အခြေခံပြီး guidance ကို adapt လုပ်ပါ"""
        
        # Base wisdom generation
        base_analysis = self.nstf_enhanced.process_with_enhanced_nstf(user_input)
        emotional_vector = self.emotion_integrator.adjust_nstf_weights(
            base_analysis.get("vector_scores", {}),
            user_emotion, 
            emotional_intensity
        )
        evolutionary_insight = self.reframe_engine.generate_comprehensive_reframe(
            user_input, user_emotion, emotional_intensity, emotional_vector
        )
        
        # Adapt based on historical effectiveness
        adaptation_note = ""
        if historical_context["effectiveness_level"] == "LOW_EFFICACY":
            adaptation_note = """
🧩 **ADAPTIVE APPROACH**: Noticing past challenges with integration - 
simplifying guidance and focusing on foundational mindfulness practices.
"""
        elif historical_context["effectiveness_level"] == "HIGH_EFFICACY":
            adaptation_note = """
🎯 **ADAPTIVE APPROACH**: Building on your strong integration skills - 
exploring deeper dimensions of the wisdom practice.
"""
        
        integrated_response = f"""
{base_analysis}

{'='*70}
🧬 **EVOLUTIONARY WISDOM INTEGRATION** 
{'='*70}

{evolutionary_insight}

{adaptation_note}

💫 **SYNTHESIS**: "Your growth journey is unique - each step builds wisdom"
"""
        
        return integrated_response
