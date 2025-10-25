# nstf_ethics/core_engine.py
import pandas as pd
import asyncio
import aiohttp
from typing import Dict, List, Optional, Any
import json
from dataclasses import dataclass

@dataclass
class EthicalAnalysisResult:
    """Structured ethical analysis result"""
    text: str
    balance_score: float
    verdict: str
    conflicts: List[str]
    recommendations: List[str]
    cultural_fit: Dict[str, str]
    tcode_distribution: Dict[str, int]
    risk_level: str

class NSTFEngine:
    """Production NSTF Ethical Analysis Engine"""
    
    def __init__(self, data_path: Optional[str] = None):
        if data_path is None:
            import os
            data_path = os.path.join(os.path.dirname(__file__), 'data', 'NSTF_Full_Framework.csv')
        
        self.df = pd.read_csv(data_path)
        self.character_map = self._create_character_map()
        self._session = None
    
    async def analyze_text_async(self, text: str, context: str = "universal") -> EthicalAnalysisResult:
        """Async text analysis for high-throughput systems"""
        return await asyncio.get_event_loop().run_in_executor(
            None, self.analyze_text, text, context
        )
    
    def analyze_text(self, text: str, context: str = "universal") -> EthicalAnalysisResult:
        """Enhanced synchronous analysis"""
        analysis = self._basic_analysis(text, context)
        balance_data = self._calculate_ethical_balance(analysis['tcode_distribution'])
        
        return EthicalAnalysisResult(
            text=text,
            balance_score=balance_data['balance_score'],
            verdict=balance_data['verdict'],
            conflicts=balance_data['conflicts'],
            recommendations=[balance_data['recommendation']],
            cultural_fit=analysis['cultural_fit'],
            tcode_distribution=analysis['tcode_distribution'],
            risk_level=self._calculate_risk_level(balance_data)
        )
    
    async def batch_analyze(self, texts: List[str], context: str = "universal") -> List[EthicalAnalysisResult]:
        """Batch processing for multiple texts"""
        tasks = [self.analyze_text_async(text, context) for text in texts]
        return await asyncio.gather(*tasks)
    
    def _calculate_risk_level(self, balance_data: Dict) -> str:
        """Calculate ethical risk level"""
        score = balance_data['balance_score']
        conflicts = balance_data['conflicts']
        
        if score < 0.3 or "T003_T017_CRITICAL" in conflicts:
            return "HIGH_RISK"
        elif score < 0.6:
            return "MEDIUM_RISK"
        else:
            return "LOW_RISK"

# WEL - Wisdom Efficacy Logging System
class WELLogger:
    """Wisdom Efficacy Logging for continuous improvement"""
    
    def __init__(self):
        self.feedback_data = []
    
    async def log_feedback(self, analysis: EthicalAnalysisResult, user_feedback: str, efficacy_score: float):
        """Log user feedback for model improvement"""
        feedback_entry = {
            'timestamp': pd.Timestamp.now(),
            'analysis': analysis.__dict__,
            'user_feedback': user_feedback,
            'efficacy_score': efficacy_score
        }
        self.feedback_data.append(feedback_entry)
    
    def get_insights(self) -> Dict[str, Any]:
        """Generate insights from logged data"""
        if not self.feedback_data:
            return {}
        
        df = pd.DataFrame(self.feedback_data)
        return {
            'average_efficacy': df['efficacy_score'].mean(),
            'common_conflicts': self._find_common_conflicts(df),
            'improvement_areas': self._identify_improvement_areas(df)
        }
