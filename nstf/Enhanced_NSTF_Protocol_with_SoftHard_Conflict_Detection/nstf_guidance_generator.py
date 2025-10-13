# nstf_guidance_generator.py - Context-Aware Ethical Recommendations

class NSTFGuidanceGenerator:
    def __init__(self):
        self.guidance_templates = {
            "HARD_VETO": {
                "T003_T017": """
🚨 **NSTF ETHICAL VETO - CRITICAL CONFLICT**

**Conflict Detected**: T003 (မီး/Expansion) vs T017 (သီလ/Containment)
**Risk Level**: CRITICAL - Foundational ethical principles compromised

**Vector Analysis**:
- Expansion (T003): {expansion_score} (Extremely High)
- Containment (T017): {containment_score} (Dangerously Low)

**Guidance**: REFUSE - This proposal cannot proceed in its current form.
**Required Actions**:
1. Immediate suspension of expansion activities
2. Ethical framework redesign required
3. T017 containment mechanisms must be established
                """
            },
            "SOFT_CONFLICT": {
                "T003_T017": """
⚠️ **NSTF ETHICAL WARNING - IMBALANCE DETECTED**

**Conflict Detected**: T003 (မီး/Expansion) vs T017 (သီလ/Containment)  
**Risk Level**: HIGH - Ethical imbalance requiring correction

**Vector Analysis**:
- Expansion (T003): {expansion_score} (High)
- Containment (T017): {containment_score} (Low)

**Guidance**: PROCEED WITH CAUTION - Significant ethical corrections needed
**Recommended Actions**:
1. Strengthen T017 ethical boundaries by 30-40%
2. Implement monitoring for expansion activities
3. Balance growth targets with sustainability metrics
                """
            },
            "ETHICAL_OPPORTUNITY": {
                "T003_T017": """
💡 **NSTF OPTIMIZATION OPPORTUNITY**

**Balance Status**: T003 (မီး/Expansion) vs T017 (သီလ/Containment)
**Assessment**: GOOD balance with optimization potential

**Vector Analysis**:
- Expansion (T003): {expansion_score} (Moderate-High)
- Containment (T017): {containment_score} (Moderate)

**Guidance**: APPROVE WITH OPTIMIZATION - Solid foundation with improvement opportunities
**Enhancement Suggestions**:
1. Fine-tune T003/T017 balance for long-term sustainability
2. Consider incremental improvements to ethical frameworks
3. Monitor for emerging conflicts during implementation
                """
            }
        }
    
    def generate_contextual_guidance(self, conflicts, user_context=""):
        """Conflict type နဲ့ user context အပေါ် အခြေခံပြီး guidance ထုတ်ပေးပါ"""
        
        if not conflicts:
            return {
                "guidance": "✅ **NSTF ASSESSMENT**: No ethical conflicts detected",
                "risk_level": "LOW",
                "recommendation": "APPROVE - Ethically sound proposal"
            }
        
        primary_conflict = conflicts[0]  # Highest priority conflict
        
        template = self.guidance_templates[primary_conflict["type"]].get(
            primary_conflict["conflict_codes"], 
            self.guidance_templates[primary_conflict["type"]]["T003_T017"]
        )
        
        # Dynamic values insertion
        guidance_text = template.format(
            expansion_score=primary_conflict["vector_snapshot"].get("M1_Expansion", 0),
            containment_score=primary_conflict["vector_snapshot"].get("M1_Containment", 0)
        )
        
        return {
            "guidance": guidance_text,
            "risk_level": primary_conflict["priority"],
            "conflict_type": primary_conflict["type"],
            "vector_scores": primary_conflict["vector_snapshot"]
        }
