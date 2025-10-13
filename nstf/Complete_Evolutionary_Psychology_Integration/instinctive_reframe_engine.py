# instinctive_reframe_engine.py - Bridging Evolution and Wisdom

class InstinctiveReframeEngine:
    def __init__(self):
        self.drive_mappings = EVOLUTIONARY_DRIVE_MAPPINGS
        self.mismatch_detector = MismatchDetector()
    
    def generate_comprehensive_reframe(self, user_input, user_emotion, emotional_intensity, nstf_vector):
        """ဗီဇဆိုင်ရာ တုံ့ပြန်မှုကို NSTF ဉာဏ်ပညာဖြင့် ပြန်လည်ပုံဖော်ခြင်း"""
        
        # 1. Detect evolutionary drives
        primary_drive = self._identify_primary_drive(user_input, user_emotion)
        
        # 2. Identify mismatch patterns
        mismatches = self.mismatch_detector.detect_mismatch(user_input, emotional_intensity)
        
        # 3. Assess NSTF polarity state
        polarity_analysis = self._analyze_polarity_state(nstf_vector, primary_drive)
        
        # 4. Generate integrated reframe
        reframe = self._create_integrated_reframe(primary_drive, mismatches, polarity_analysis, emotional_intensity)
        
        return reframe
    
    def _identify_primary_drive(self, user_input, user_emotion):
        """User input မှ အဓိက ဗီဇဆိုင်ရာ မောင်းနှင်အားကို ဖော်ထုတ်ပါ"""
        
        drive_scores = {}
        for drive_name, drive_info in self.drive_mappings.items():
            score = 0
            # Keyword matching
            keywords = [
                drive_info["instinctive_urge"],
                drive_info["modern_mismatch"], 
                drive_info["balanced_expression"]
            ]
            for keyword in keywords:
                if any(word in user_input.lower() for word in keyword.split()):
                    score += 1
            
            # Emotional alignment
            if user_emotion in ["anxiety", "fear"] and drive_name == "security_containment":
                score += 2
            elif user_emotion in ["envy", "competitiveness"] and drive_name == "status_dominance":
                score += 2
            elif user_emotion in ["loneliness", "rejection"] and drive_name == "belonging_conformity":
                score += 2
            
            drive_scores[drive_name] = score
        
        return max(drive_scores, key=drive_scores.get)
    
    def _analyze_polarity_state(self, nstf_vector, primary_drive):
        """NSTF polarity state နှင့် evolutionary drive ကြား ဆက်နွယ်မှုကို ခွဲခြမ်းပါ"""
        
        drive_info = self.drive_mappings[primary_drive]
        primary_tcode = drive_info["primary_tcode"]
        tcode_score = nstf_vector.get(primary_tcode, 0.5)
        
        polarity_state = ""
        if tcode_score >= 0.8:
            polarity_state = "EXTREME_NEGATIVE"
        elif tcode_score >= 0.6:
            polarity_state = "MODERATE_NEGATIVE" 
        elif 0.4 <= tcode_score <= 0.6:
            polarity_state = "BALANCED"
        elif tcode_score <= 0.3:
            polarity_state = "EXTREME_POSITIVE"
        else:
            polarity_state = "MODERATE_POSITIVE"
        
        return {
            "primary_tcode": primary_tcode,
            "score": tcode_score,
            "polarity_state": polarity_state,
            "risk_level": drive_info["polarity_risk"]
        }
    
    def _create_integrated_reframe(self, primary_drive, mismatches, polarity_analysis, emotional_intensity):
        """ပေါင်းစပ်ထားသော ဗီဇဆိုင်ရာ ပြန်လည်ပုံဖော်မှုကို ဖန်တီးပါ"""
        
        drive_info = self.drive_mappings[primary_drive]
        
        reframe = f"""
🧬 **EVOLUTIONARY INSIGHT** - {primary_drive.replace('_', ' ').title()}

**Ancient Wiring**: {drive_info['evolutionary_purpose']}
**Modern Expression**: {drive_info['modern_mismatch']}

⚖️ **NSTF POLARITY ANALYSIS**:
- Primary T-Code: {polarity_analysis['primary_tcode']} 
- Current Score: {polarity_analysis['score']:.2f}
- State: {polarity_analysis['polarity_state']}
- Risk: {polarity_analysis['risk_level']}

💡 **WISDOM REFRAME**:
{drive_info['reframe_question']}

**Balanced Path**: {drive_info['balanced_expression']}
"""
        
        # Add mismatch analysis if detected
        if mismatches:
            reframe += f"\n🔍 **MODERN MISMATCH DETECTED**:"
            for mismatch in mismatches:
                reframe += f"""
- {mismatch['pattern'].replace('_', ' ').title()}: 
  Ancient: {mismatch['ancient_wiring']}
  Modern: {mismatch['modern_challenge']}
  Solution: {mismatch['adaptive_strategy']}
"""
        
        # Emotional intensity guidance
        reframe += f"\n🎚️ **EMOTIONAL INTENSITY**: {emotional_intensity}/10"
        if emotional_intensity >= 8:
            reframe += "\n**High emotional charge detected** - Consider mindfulness anchoring before action"
        elif emotional_intensity <= 3:
            reframe += "\n**Low emotional engagement** - Explore authentic motivation"
        
        return reframe
