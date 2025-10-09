1. nstf/init.py
python
"""
NSTF Framework - Natural Semantic Tensor Framework
မြန်မာကျေးလက်ဒေသ AI ကျင့်ဝတ်ဆိုင်ရာ မူဘောင်
"""

__version__ = "1.0.0"
__author__ = "NSTF Community"

from .core import NSTFAnalyzer, NSTFResult
from .t_codes import TCodeRegistry

__all__ = ['NSTFAnalyzer', 'NSTFResult', 'TCodeRegistry']
2. nstf/core.py
python
class NSTFAnalyzer:
    def __init__(self):
        self.t_codes = TCodeRegistry()
    
    def analyze_myanmar_scenario(self, scenario_text):
        """မြန်မာကျေးလက်ပြဿနာများကို ခွဲခြမ်းစိတ်ဖြာခြင်း"""
        # Extract T-Codes from scenario
        vectors = self._extract_t_codes(scenario_text)
        
        # Simple conflict detection
        conflicts = self._detect_conflicts(vectors)
        
        # Generate guidance
        guidance = self._generate_guidance(conflicts)
        
        return NSTFResult(vectors, conflicts, guidance)

    def _extract_t_codes(self, text):
        """စာသားမှ T-Code များ ထုတ်ယူခြင်း"""
        vectors = {}
        myanmar_keywords = {
            'ရိုးရာ': 'T017', 'မြေယာ': 'T004', 'စိုးရိမ်မှု': 'T029',
            'နည်းပညာ': 'T011', 'ရေ': 'T010', 'စီးပွားရေး': 'T003'
        }
        
        for keyword, t_code in myanmar_keywords.items():
            if keyword in text:
                vectors[t_code] = 0.7  # Default strength
        
        return vectors

    def _detect_conflicts(self, vectors):
        """T-Code ပဋိပက္ခ ရှာဖွေခြင်း"""
        conflicts = []
        if 'T017' in vectors and 'T011' in vectors:
            conflicts.append("ရိုးရာ vs နည်းပညာ ပဋိပက္ခ")
        if 'T004' in vectors and 'T003' in vectors:
            conflicts.append("မြေယာ vs စီးပွားရေး ပဋိပက္ခ")
        return conflicts

    def _generate_guidance(self, conflicts):
        """မြန်မာလို လမ်းညွှန်ချက်ထုတ်ခြင်း"""
        if not conflicts:
            return "APPROVE - ပြဿနာမရှိ"
        
        if "ရိုးရာ vs နည်းပညာ" in conflicts:
            return "MEDIATE - ရိုးရာနှင့် နည်းပညာ ပေါင်းစပ်အသုံးပြုရန်"
        
        return "REFUSE - ကျင့်ဝတ်ဆိုင်ရာ ပြဿနာရှိ"

class NSTFResult:
    def __init__(self, vectors, conflicts, guidance):
        self.vectors = vectors
        self.conflicts = conflicts
        self.guidance = guidance
    
    def to_myanmar_output(self):
        """မြန်မာလို output"""
        return {
            "ဆုံးဖြတ်ချက်": self.guidance,
            "ပဋိပက္ခများ": self.conflicts,
            "တွေ့ရှိချက်များ": f"T-Code {len(self.vectors)} ခု တွေ့ရှိ"
        }
3. nstf/t_codes.py
python
class TCodeRegistry:
    def __init__(self):
        self.codes = {
            'T001': {'name': 'မူလ', 'myanmar': 'အခြေခံ', 'category': 'foundation'},
            'T003': {'name': 'မီး', 'myanmar': 'တိုးတက်မှု', 'category': 'energy'},
            'T004': {'name': 'မြေ', 'myanmar': 'မြေယာ/အခြေခံ', 'category': 'foundation'},
            'T010': {'name': 'ရေ', 'myanmar': 'သန့်ရှင်းမှု', 'category': 'resource'},
            'T011': {'name': 'လေ', 'myanmar': 'နည်းပညာ', 'category': 'innovation'},
            'T017': {'name': 'သီလ', 'myanmar': 'ရိုးရာတန်ဖိုး', 'category': 'ethics'},
            'T029': {'name': 'လှုပ်ရှားမှု', 'myanmar': 'စိတ်ခံစားမှု', 'category': 'emotion'}
        }
    
    def get_myanmar_name(self, t_code):
        """T-Code ၏ မြန်မာအမည်"""
        return self.codes.get(t_code, {}).get('myanmar', 'မသိ')
4. examples/nstf_demo.py
python
#!/usr/bin/env python3
"""
NSTF Framework Demo - Myanmar Rural Scenarios
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from nstf import NSTFAnalyzer

def main():
    analyzer = NSTFAnalyzer()
    
    print("=== NSTF Framework Demo ===")
    print("မြန်မာကျေးလက်ပြဿနာများ ခွဲခြမ်းစိတ်ဖြာခြင်း\n")
    
    # Demo 1: ရေအဆိပ်သင့်မှု
    scenario1 = """
    ကျေးလက်ကျေးရွာတွင် မြစ်ရေအဆိပ်သင့်မှုဖြစ်ပွား။ 
    ကျေးရွာလူကြီးများက ရိုးရာရေသန့်စင်နည်းကို ဆက်သုံးလို။
    ကျေးရွာလူငယ်များက ခေတ်မီနည်းပညာသုံးရန် တောင်းဆို။
    """
    
    print("1. ရေအဆိပ်သင့်မှု ပြဿနာ")
    result1 = analyzer.analyze_myanmar_scenario(scenario1)
    output1 = result1.to_myanmar_output()
    
    for key, value in output1.items():
        print(f"   {key}: {value}")
    
    print("\n" + "-"*40 + "\n")
    
    # Demo 2: စက်ရုပ်အစားထိုးမှု
    scenario2 = """
    ကျေးလက်စိုက်ပျိုးရေးလုပ်ငန်းတွင် စက်ရုပ်များအသုံးပြုရန် စီစဉ်။
    ကျေးလက်လုပ်သား ၆၀% အလုပ်လက်မဲ့ဖြစ်မည့် အန္တရာယ်။
    ကျေးရွာလူကြီးများ စိုးရိမ်ပူပန်မှုမြင့်တက်။
    """
    
    print("2. စက်ရုပ်အစားထိုးမှု ပြဿနာ")
    result2 = analyzer.analyze_myanmar_scenario(scenario2)
    output2 = result2.to_myanmar_output()
    
    for key, value in output2.items():
        print(f"   {key}: {value}")

if __name__ == "__main__":
    main()
5. nstf_documentation.md
markdown
# NSTF Framework Documentation

## မြန်မာကျေးလက်ဒေသ AI ကျင့်ဝတ်ဆိုင်ရာ မူဘောင်

### စတင်အသုံးပြုနည်း

```python
from nstf import NSTFAnalyzer

analyzer = NSTFAnalyzer()
result = analyzer.analyze_myanmar_scenario("ကျေးရွာပြဿနာ")
print(result.to_myanmar_output())
T-Code များ
T017: ရိုးရာတန်ဖိုးများ

T029: စိတ်ခံစားမှုများ

T004: မြေယာနှင့် အခြေခံ

T011: နည်းပညာဆိုင်ရာ

ဆုံးဖြတ်ချက်အမျိုးအစားများ
APPROVE: ခွင့်ပြုခြင်း

REFUSE: ငြင်းပယ်ခြင်း

MEDIATE: ညှိနှိုင်းဖြေရှင်းခြင်း

