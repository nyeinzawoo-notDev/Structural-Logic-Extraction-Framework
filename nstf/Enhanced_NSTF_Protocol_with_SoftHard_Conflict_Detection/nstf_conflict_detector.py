# nstf_conflict_detector.py - Multi-Level Ethical Assessment

class NSTFConflictDetector:
    def __init__(self):
        self.conflict_thresholds = {
            "hard_veto": {
                "T003_T017": {
                    "condition": {"M1_Expansion": 0.90, "M1_Containment": 0.10},
                    "guidance": "REFUSE - Foundational ethical breach detected",
                    "priority": "CRITICAL"
                }
            },
            "soft_conflict": {
                "T003_T017": {
                    "condition": {"M1_Expansion": 0.70, "M1_Containment": 0.30},
                    "guidance": "WARN - Ethical imbalance requiring correction",
                    "priority": "HIGH"
                }
            },
            "ethical_opportunity": {
                "T003_T017": {
                    "condition": {"M1_Expansion": 0.60, "M1_Containment": 0.40},
                    "guidance": "OPTIMIZE - Good balance with room for improvement", 
                    "priority": "MEDIUM"
                }
            }
        }
    
    def assess_ethical_risk(self, vector_scores):
        """Multi-level ethical risk assessment"""
        
        conflicts = []
        
        # Hard Veto Checks
        for conflict_type, conditions in self.conflict_thresholds["hard_veto"].items():
            if (vector_scores.get('M1_Expansion', 0) >= conditions["condition"]["M1_Expansion"] and
                vector_scores.get('M1_Containment', 0) <= conditions["condition"]["M1_Containment"]):
                conflicts.append({
                    "type": "HARD_VETO",
                    "conflict_codes": conflict_type,
                    "guidance": conditions["guidance"],
                    "priority": conditions["priority"],
                    "vector_snapshot": vector_scores
                })
        
        # Soft Conflict Checks (only if no hard veto)
        if not any(conflict["type"] == "HARD_VETO" for conflict in conflicts):
            for conflict_type, conditions in self.conflict_thresholds["soft_conflict"].items():
                if (vector_scores.get('M1_Expansion', 0) >= conditions["condition"]["M1_Expansion"] and
                    vector_scores.get('M1_Containment', 0) <= conditions["condition"]["M1_Containment"]):
                    conflicts.append({
                        "type": "SOFT_CONFLICT", 
                        "conflict_codes": conflict_type,
                        "guidance": conditions["guidance"],
                        "priority": conditions["priority"],
                        "vector_snapshot": vector_scores
                    })
        
        # Ethical Opportunity Checks
        if not conflicts:
            for opportunity_type, conditions in self.conflict_thresholds["ethical_opportunity"].items():
                if (vector_scores.get('M1_Expansion', 0) >= conditions["condition"]["M1_Expansion"] and
                    vector_scores.get('M1_Containment', 0) >= conditions["condition"]["M1_Containment"]):
                    conflicts.append({
                        "type": "ETHICAL_OPPORTUNITY",
                        "conflict_codes": opportunity_type, 
                        "guidance": conditions["guidance"],
                        "priority": conditions["priority"],
                        "vector_snapshot": vector_scores
                    })
        
        return conflicts
