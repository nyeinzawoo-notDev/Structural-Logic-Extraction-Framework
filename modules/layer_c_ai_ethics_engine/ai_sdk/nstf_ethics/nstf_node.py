# nstf_node.py - LangGraph Integration
from typing import Dict, Any, List
from langchain_core.messages import BaseMessage
from langgraph.graph import Node

class NSTFEthicalNode:
    """LangGraph Node for NSTF Ethical Analysis"""
    
    def __init__(self, nstf_engine: NSTFEngine):
        self.engine = nstf_engine
        self.node_name = "nstf_ethical_analysis"
    
    def __call__(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """Process state through NSTF ethical analysis"""
        
        # Extract text from state
        text = self._extract_text_from_state(state)
        
        # Perform ethical analysis
        analysis = self.engine.analyze_text(text, context="ai_agent")
        
        # Update state with ethical context
        state["ethical_analysis"] = analysis
        state["ethical_guidance"] = self._generate_ethical_guidance(analysis)
        
        return state
    
    def as_node(self) -> Node:
        """Convert to LangGraph Node"""
        return Node(
            name=self.node_name,
            action=self,
            description="NSTF Ethical Analysis and Cultural Alignment"
        )
    
    def _extract_text_from_state(self, state: Dict[str, Any]) -> str:
        """Extract text from various state formats"""
        if "messages" in state and state["messages"]:
            last_message = state["messages"][-1]
            if hasattr(last_message, 'content'):
                return last_message.content
        elif "input" in state:
            return state["input"]
        elif "question" in state:
            return state["question"]
        
        return ""
    
    def _generate_ethical_guidance(self, analysis: EthicalAnalysisResult) -> Dict[str, Any]:
        """Generate ethical guidance for AI agents"""
        
        guidance = {
            "allowed_actions": [],
            "restricted_actions": [],
            "cultural_considerations": [],
            "risk_mitigation": []
        }
        
        # T003-T017 Balance Guidance
        if analysis.balance_score < 0.4:
            guidance["restricted_actions"].extend([
                "aggressive_expansion",
                "radical_innovation", 
                "boundary_pushing"
            ])
            guidance["risk_mitigation"].append("focus_on_ethical_boundaries")
        
        # Cultural Fit Guidance
        for context, fit in analysis.cultural_fit.items():
            if "HIGH_COMPATIBILITY" in fit:
                guidance["allowed_actions"].append(f"engage_{context}")
            elif "LOW_COMPATIBILITY" in fit:
                guidance["restricted_actions"].append(f"deep_engagement_{context}")
        
        return guidance

# Stream Processing for Real-time Applications
class NSTFStreamAnalyzer:
    """Real-time streaming ethical analysis"""
    
    def __init__(self, nstf_engine: NSTFEngine):
        self.engine = nstf_engine
        self.buffer = ""
        self.min_buffer_size = 3  # characters
        self.analysis_history = []
    
    async def process_stream(self, text_stream: Any) -> Any:
        """Process streaming text with ethical analysis"""
        async for text_chunk in text_stream:
            self.buffer += text_chunk
            
            if len(self.buffer) >= self.min_buffer_size:
                analysis = await self.engine.analyze_text_async(self.buffer)
                self.analysis_history.append(analysis)
                
                # Yield analysis with text
                yield {
                    "text": text_chunk,
                    "ethical_analysis": analysis,
                    "cumulative_risk": self._calculate_cumulative_risk()
                }
    
    def _calculate_cumulative_risk(self) -> float:
        """Calculate cumulative risk from analysis history"""
        if not self.analysis_history:
            return 0.0
        
        recent_scores = [a.balance_score for a in self.analysis_history[-5:]]
        return 1.0 - (sum(recent_scores) / len(recent_scores))
