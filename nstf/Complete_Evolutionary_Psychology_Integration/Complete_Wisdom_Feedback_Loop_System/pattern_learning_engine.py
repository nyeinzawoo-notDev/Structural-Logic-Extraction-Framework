# pattern_learning_engine.py - Longitudinal Growth Tracking

class PatternLearningEngine:
    def __init__(self):
        self.cross_user_patterns = {}
        self.effectiveness_correlations = {}
        self.adaptive_strategies = {}
    
    def analyze_cross_session_patterns(self, user_sessions):
        """မတူညီသော user sessions များမှ pattern များကို ခွဲခြမ်းစိတ်ဖြာပါ"""
        
        patterns = {
            "high_effectiveness_scenarios": [],
            "resistance_patterns": [], 
            "breakthrough_moments": [],
            "optimal_guidance_sequences": []
        }
        
        for session_id, session_data in user_sessions.items():
            insights = self._extract_session_insights(session_data)
            
            if insights["avg_efficacy"] > 0.7:
                patterns["high_effectiveness_scenarios"].append({
                    "session_id": session_id,
                    "key_factors": insights["success_factors"],
                    "guidance_approach": insights["primary_approach"]
                })
            
            if insights["resistance_detected"]:
                patterns["resistance_patterns"].append({
                    "session_id": session_id, 
                    "resistance_type": insights["resistance_type"],
                    "resolution_attempted": insights["resolution_method"]
                })
        
        self._update_adaptive_strategies(patterns)
        return patterns
    
    def _extract_session_insights(self, session_data):
        """တစ်ခုချင်းစီသော session မှ insights များကို ထုတ်ယူပါ"""
        
        interactions = session_data.get("interactions", [])
        efficacy_scores = session_data.get("efficacy_metrics", {}).get("vector_shifts", [])
        
        if not efficacy_scores:
            return {"avg_efficacy": 0, "resistance_detected": False}
        
        avg_efficacy = sum(efficacy_scores) / len(efficacy_scores)
        
        # Analyze guidance approaches
        guidance_types = [interaction["ai_guidance_type"] for interaction in interactions]
        primary_approach = max(set(guidance_types), key=guidance_types.count) if guidance_types else "UNKNOWN"
        
        # Detect resistance patterns
        resistance_detected = any(score < 0.3 for score in efficacy_scores[-3:]) if len(efficacy_scores) >= 3 else False
        
        return {
            "avg_efficacy": avg_efficacy,
            "primary_approach": primary_approach,
            "success_factors": self._identify_success_factors(interactions, efficacy_scores),
            "resistance_detected": resistance_detected,
            "resistance_type": self._classify_resistance(interactions, efficacy_scores) if resistance_detected else None,
            "resolution_method": self._identify_resolution_attempts(interactions) if resistance_detected else None
        }
    
    def generate_system_evolution_insights(self):
        """System-wide learning insights ကို generate လုပ်ပါ"""
        
        evolution_insights = {
            "most_effective_guidance_types": self._rank_guidance_effectiveness(),
            "common_resolution_patterns": self._identify_common_resolutions(),
            "adaptive_threshold_adjustments": self._calculate_threshold_adjustments(),
            "emerging_wisdom_patterns": self._detect_emerging_patterns()
        }
        
        return evolution_insights
