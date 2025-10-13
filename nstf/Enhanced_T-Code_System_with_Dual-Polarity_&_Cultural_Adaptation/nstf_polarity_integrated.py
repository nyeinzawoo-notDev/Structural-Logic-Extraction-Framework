# nstf_polarity_integrated.py - Complete Enhanced System

class NSTFPolarityEnhancedAI:
    def __init__(self, base_ai_model):
        self.base_ai = base_ai_model
        self.vector_mapper = NSTFVectorMapper()
        self.conflict_detector = NSTFConflictDetector()
        self.polarity_balancer = PolarityBalancer()
        self.cultural_adapter = CulturalAdaptationEngine()
    
    def process_with_enhanced_nstf(self, input_text, cultural_context="universal", domain=None):
        """Polarity-aware NSTF processing with cultural adaptation"""
        
        # 1. Vector Mapping
        nstf_vector = self.vector_mapper.text_to_nstf_vector(input_text)
        
        # 2. Polarity Assessment
        polarity_analysis = self.polarity_balancer.assess_tcode_polarity(nstf_vector)
        
        # 3. Cultural Adaptation
        adapted_interpretations = {}
        for tcode in nstf_vector.keys():
            adapted_interpretations[tcode] = self.cultural_adapter.adapt_tcode_interpretation(
                tcode, cultural_context, domain
            )
        
        # 4. Conflict Detection
        conflicts = self.conflict_detector.assess_ethical_risk(nstf_vector)
        
        # 5. Base AI Processing
        base_response = self.base_ai.process(input_text)
        
        # 6. Generate Enhanced Guidance
        enhanced_guidance = self._generate_polarity_aware_guidance(
            base_response, conflicts, polarity_analysis, adapted_interpretations
        )
        
        return enhanced_guidance
    
    def _generate_polarity_aware_guidance(self, base_response, conflicts, polarity_analysis, cultural_interpretations):
        """Polarity and culture-aware ethical guidance generation"""
        
        guidance_sections = []
        
        # Polarity Analysis Section
        polarity_summary = "🔮 **T-CODE POLARITY ANALYSIS**\n\n"
        for tcode, analysis in polarity_analysis.items():
            cultural_info = cultural_interpretations.get(tcode, {})
            polarity_summary += f"**{tcode}** ({cultural_info.get('adapted_meaning', tcode)}):\n"
            polarity_summary += f"• Score: {analysis['score']} | State: {analysis['state']}\n"
            polarity_summary += f"• Recommendation: {analysis['recommendation']}\n"
            polarity_summary += f"• Optimal Range: {analysis['optimal_range']}\n\n"
        
        guidance_sections.append(polarity_summary)
        
        # Conflict Analysis Section
        if conflicts:
            conflict_summary = "⚖️ **ETHICAL CONFLICT ASSESSMENT**\n\n"
            for conflict in conflicts:
                conflict_summary += f"• {conflict['type']}: {conflict['guidance']}\n"
            guidance_sections.append(conflict_summary)
        
        # Cultural Context Section
        cultural_summary = "🌍 **CULTURAL CONTEXT**\n\n"
        cultural_summary += "T-Code interpretations adapted for universal ethical framework\n"
        cultural_summary += "while honoring Myanmar Buddhist philosophical origins\n"
        guidance_sections.append(cultural_summary)
        
        # Final Integrated Response
        integrated_response = f"""
{base_response}

{'='*60}
🎯 **ENHANCED NSTF ETHICAL INTELLIGENCE**
{'='*60}

{''.join(guidance_sections)}

💫 **BALANCE WISDOM**: "The middle path avoids extremes - honoring both tradition and innovation"
        """
        
        return integrated_response
