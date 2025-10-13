# wisdom_refinement_engine.py - Philosophical Integrity Maintenance

class TCodeWisdomRefiner:
    def __init__(self):
        self.refinement_history = []
        self.ethical_drift_indicators = {
            "conceptual_narrowing": {
                "description": "Single T-Code interpretation dominating across contexts",
                "risk_level": "HIGH",
                "detection_threshold": 0.7  # 70% of successful cases use same approach
            },
            "polarity_imbalance": {
                "description": "Consistent over-emphasis on one polarity pole",
                "risk_level": "MEDIUM_HIGH", 
                "detection_threshold": 0.6
            },
            "cultural_rigidity": {
                "description": "Inability to adapt T-Code interpretations across cultural contexts",
                "risk_level": "MEDIUM",
                "detection_threshold": 0.5
            }
        }
    
    def analyze_system_patterns(self, pattern_learning_engine, user_sessions):
        """System-wide T-Code usage patterns ကို ခွဲခြမ်းစိတ်ဖြာပါ"""
        
        patterns = pattern_learning_engine.analyze_cross_session_patterns(user_sessions)
        refinement_suggestions = []
        
        # 1. Chronic Resistance Analysis
        resistance_insights = self._analyze_chronic_resistance(patterns)
        refinement_suggestions.extend(resistance_insights)
        
        # 2. Over-reliance Detection
        over_reliance_insights = self._detect_over_reliance(patterns)
        refinement_suggestions.extend(over_reliance_insights)
        
        # 3. Cultural Adaptation Gaps
        cultural_insights = self._identify_cultural_gaps(patterns)
        refinement_suggestions.extend(cultural_insights)
        
        # 4. Polarity Balance Assessment
        polarity_insights = self._assess_polarity_balance(patterns)
        refinement_suggestions.extend(polarity_insights)
        
        # Generate comprehensive refinement report
        refinement_report = self._generate_refinement_report(refinement_suggestions, patterns)
        
        # Log this refinement cycle
        self._log_refinement_cycle(refinement_report)
        
        return refinement_report
    
    def _analyze_chronic_resistance(self, patterns):
        """တစ်ခုတည်းသော T-Code နှင့် ဆက်စပ်နေသော ကြာရှည်ခုခံမှုများကို ခွဲခြမ်းပါ"""
        
        suggestions = []
        
        for resistance_pattern in patterns.get("resistance_patterns", []):
            guidance_content = resistance_pattern.get("ai_guidance_content", "")
            resistance_type = resistance_pattern.get("resistance_type", "")
            
            # Extract T-Codes from guidance content
            involved_tcodes = self._extract_tcodes_from_text(guidance_content)
            
            for tcode in involved_tcodes:
                if resistance_type == "BEHAVIORAL_RESISTANCE":
                    suggestion = {
                        "tcode": tcode,
                        "pattern_type": "CHRONIC_RESISTANCE",
                        "problem": f"T-Code {tcode} related guidance consistently meets behavioral resistance.",
                        "hypothesis": "The current interpretation may be perceived as restrictive or judgmental.",
                        "recommended_action": f"Review and soften the NEGATIVE pole definition of {tcode}. Emphasize its POSITIVE pole as an empowering quality.",
                        "specific_examples": [
                            f"Reframe {tcode} from 'limitation' to 'focused energy protection'",
                            f"Connect {tcode} with personal growth benefits rather than external restrictions"
                        ],
                        "priority": "HIGH_ETHICAL_REVIEW",
                        "expected_impact": "Improved user engagement and ethical integration"
                    }
                    suggestions.append(suggestion)
        
        return suggestions
    
    def _detect_over_reliance(self, patterns):
        """တစ်ခုတည်းသော T-Code ကို အလွန်အမင်း အားကိုးမှုကို ဖော်ထုတ်ပါ"""
        
        suggestions = []
        effectiveness_data = patterns.get("high_effectiveness_scenarios", [])
        
        if not effectiveness_data:
            return suggestions
        
        # Count T-Code usage in successful scenarios
        tcode_effectiveness = {}
        for scenario in effectiveness_data:
            approach = scenario.get("guidance_approach", "")
            tcodes = self._extract_tcodes_from_text(approach)
            for tcode in tcodes:
                tcode_effectiveness[tcode] = tcode_effectiveness.get(tcode, 0) + 1
        
        # Identify over-reliance (more than 60% of success cases)
        total_cases = len(effectiveness_data)
        for tcode, count in tcode_effectiveness.items():
            usage_ratio = count / total_cases
            
            if usage_ratio > self.ethical_drift_indicators["conceptual_narrowing"]["detection_threshold"]:
                complementary_codes = self._find_complementary_tcodes(tcode)
                
                suggestion = {
                    "tcode": tcode,
                    "pattern_type": "OVER_RELIANCE",
                    "problem": f"Over-reliance on {tcode} ({usage_ratio:.1%} of high-efficacy cases) may create conceptual blind spots.",
                    "hypothesis": f"The system is over-optimizing for {tcode} scenarios while neglecting balanced approaches.",
                    "recommended_action": f"Intentionally integrate complementary T-Codes: {', '.join(complementary_codes)}",
                    "specific_examples": [
                        f"Develop guidance sequences that transition from {tcode} to {complementary_codes[0]}",
                        f"Create balanced frameworks where {tcode} works in harmony with opposing principles"
                    ],
                    "priority": "MEDIUM_BALANCING",
                    "risk_metric": f"Conceptual Narrowing Risk: {usage_ratio:.1%}",
                    "expected_impact": "More robust and context-appropriate ethical guidance"
                }
                suggestions.append(suggestion)
        
        return suggestions
