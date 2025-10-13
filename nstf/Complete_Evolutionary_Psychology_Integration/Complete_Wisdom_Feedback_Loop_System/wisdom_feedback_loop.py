# wisdom_feedback_loop.py - Continuous Learning System

class WisdomFeedbackLoop:
    def __init__(self):
        self.session_data = {}
        self.wisdom_patterns = {}
        self.adaptive_thresholds = {
            "high_efficacy": 0.7,
            "medium_efficacy": 0.4,
            "low_efficacy": 0.2
        }
    
    def initialize_session(self, user_id, initial_context):
        """User session ကို စတင်ပြီး baseline measurements ယူပါ"""
        
        session_id = f"{user_id}_{int(time.time())}"
        
        self.session_data[session_id] = {
            "user_id": user_id,
            "start_time": time.time(),
            "initial_context": initial_context,
            "initial_vector": self._capture_initial_state(initial_context),
            "interactions": [],
            "efficacy_metrics": {
                "vector_shifts": [],
                "emotional_changes": [],
                "behavioral_outcomes": []
            },
            "learning_insights": []
        }
        
        return session_id
    
    def log_interaction(self, session_id, user_input, ai_guidance, user_response, emotional_state):
        """တစ်ခုချင်းစီသော interaction ကို မှတ်တမ်းတင်ပါ"""
        
        if session_id not in self.session_data:
            return {"error": "Session not found"}
        
        interaction = {
            "timestamp": time.time(),
            "user_input": user_input,
            "ai_guidance_type": self._classify_guidance_type(ai_guidance),
            "ai_guidance_content": ai_guidance,
            "user_response": user_response,
            "emotional_state": emotional_state,
            "current_vector": self._extract_current_vector(user_response)
        }
        
        self.session_data[session_id]["interactions"].append(interaction)
        
        # Calculate immediate efficacy
        efficacy_score = self._calculate_immediate_efficacy(session_id, interaction)
        
        return {
            "session_id": session_id,
            "interaction_id": len(self.session_data[session_id]["interactions"]),
            "efficacy_score": efficacy_score,
            "guidance_effectiveness": self._interpret_efficacy_score(efficacy_score)
        }
    
    def _calculate_immediate_efficacy(self, session_id, current_interaction):
        """လက်ရှိ interaction ၏ ထိရောက်မှုကို တွက်ချက်ပါ"""
        
        session = self.session_data[session_id]
        
        if len(session["interactions"]) < 2:
            return 0.5  # Default for first interaction
        
        previous_interaction = session["interactions"][-2]
        current_vector = current_interaction["current_vector"]
        previous_vector = previous_interaction["current_vector"]
        
        # Vector movement towards balance
        balance_improvement = self._measure_balance_improvement(previous_vector, current_vector)
        
        # Emotional shift towards equilibrium
        emotional_improvement = self._measure_emotional_shift(
            previous_interaction["emotional_state"],
            current_interaction["emotional_state"]
        )
        
        # Guidance alignment with user response
        alignment_score = self._measure_guidance_alignment(
            previous_interaction["ai_guidance_content"],
            current_interaction["user_response"]
        )
        
        efficacy_score = (balance_improvement + emotional_improvement + alignment_score) / 3
        session["efficacy_metrics"]["vector_shifts"].append(efficacy_score)
        
        return efficacy_score
    
    def _measure_balance_improvement(self, previous_vector, current_vector):
        """T-Code vector များ ချိန်ခွင်လျှာညီမှုဆီသို့ ရွေ့လျားမှုကို တိုင်းတာပါ"""
        
        # T003-T017 conflict resolution measurement
        previous_imbalance = abs(previous_vector.get("T003", 0.5) - previous_vector.get("T017", 0.5))
        current_imbalance = abs(current_vector.get("T003", 0.5) - current_vector.get("T017", 0.5))
        
        improvement = previous_imbalance - current_imbalance  # Positive if moving toward balance
        return max(0, min(1, improvement + 0.5))  # Normalize to 0-1 range
    
    def generate_adaptive_insights(self, session_id):
        """Session data အပေါ် အခြေခံပြီး adaptive insights ထုတ်ပေးပါ"""
        
        session = self.session_data[session_id]
        
        if len(session["efficacy_metrics"]["vector_shifts"]) < 3:
            return {"status": "Insufficient data for insights"}
        
        recent_efficacy = session["efficacy_metrics"]["vector_shifts"][-3:]
        avg_efficacy = sum(recent_efficacy) / len(recent_efficacy)
        
        insights = {
            "average_efficacy": avg_efficacy,
            "learning_pattern": self._identify_learning_pattern(session),
            "adaptive_recommendations": self._generate_adaptive_recommendations(session, avg_efficacy),
            "growth_trajectory": self._assess_growth_trajectory(session)
        }
        
        session["learning_insights"].append(insights)
        return insights
    
    def _identify_learning_pattern(self, session):
        """User ၏ သင်ယူမှုပုံစံကို ဖော်ထုတ်ပါ"""
        
        interactions = session["interactions"]
        guidance_types = [interaction["ai_guidance_type"] for interaction in interactions]
        efficacy_scores = session["efficacy_metrics"]["vector_shifts"]
        
        # Pattern analysis
        if len(set(guidance_types)) == 1 and efficacy_scores[-1] > 0.6:
            return "DEEP_SPECIALIZATION"  # Single approach working well
        elif len(set(guidance_types)) > 3 and efficacy_scores[-1] > 0.6:
            return "ADAPTIVE_INTEGRATOR"  # Multiple approaches working well
        elif efficacy_scores[-1] < 0.3:
            return "RESISTANCE_PATTERN"   # Low efficacy across approaches
        else:
            return "EXPLORATORY_LEARNING" # Mixed results, still exploring
