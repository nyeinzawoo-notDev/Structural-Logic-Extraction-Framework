အားလုံးကို **GitHub Repository** မှာ တင်နိုင်အောင် **Python Code** အနေနဲ့ စနစ်တကျ ပြန်လည် စုစည်းပေးပါ့မယ်။ ခင်ဗျားရဲ့ **"ငြိမ်း နိရုတ္တိလက္ခဏာစနစ် (NNLDS)"** အတွက် လိုအပ်တဲ့ **Data File** များနှင့် **Adaptive System Engine** ကို **Modular** ပုံစံဖြင့် ခွဲထုတ်ရေးသားပေးထားပါတယ်။

## 🚀 GitHub Repository Structure (အဆိုပြုထားသောဖွဲ့စည်းပုံ)

```
NSTF-NNLDS-Framework/
├── nstf_data/
│   ├── __init__.py
│   ├── special_consonants_data.py   # ကျ/ကြ, ပျ/ပြ ဝဂ်များ နှင့် ဗျည်းတွဲများ
│   └── sandhi_system_data.py        # အသတ်စနစ် (သံရပ်/သံရှိန်ရှိ)
├── nstf_engine/
│   ├── __init__.py
│   ├── adaptive_engine.py           # Self-Learning & Confidence Scoring
│   └── dialect_handler.py           # ဒေသိယစံ (မန္တလေးစံ) နှင့် နှိုင်းယှဉ်ချက်
├── main_system.py                   # Production System (အဓိက အသုံးပြုရန်)
└── README.md                        # စနစ်အကြောင်းအရာနှင့် အသုံးပြုပုံ
```

## 💻 Python Code Files

### ၁။ `nstf_data/special_consonants_data.py` (အတုအယောင်ဗျည်းများနှင့် ဗျည်းတွဲများ)

```python
# nstf_data/special_consonants_data.py

# ==================== SPECIAL CONSONANTS (Pseudo-Consonants) ====================
# ဤဗျည်းများသည် ရေးထုံးအရ တွဲထားသော်လည်း Lakkhaṇa ဗီဇအရ သီးခြား အမြစ်ဗီဇ (M1) ရှိသော ဗျည်းများဟု သတ်မှတ်သည်။
SPECIAL_CONSONANTS_DATA = [
    # ကျ/ကြ Series (Lakkhaṇa 146-151)
    {"Character": "ကျ", "Lakkhaṇa_Code": "146", "Fo_Ma": "ဖို", "Meaning_Essence_MM": "ပေါင်းစပ်ထားသော အခြေခံ (Foundation)", "T_Code": "T005", "Status": "Unverified"},
    {"Character": "ကြ", "Lakkhaṇa_Code": "146", "Fo_Ma": "ဖို", "Meaning_Essence_MM": "ထုတ်ဖော်ထားသော အခြေခံ (Foundation)", "T_Code": "T005", "Status": "Unverified"},
    {"Character": "ချ", "Lakkhaṇa_Code": "147", "Fo_Ma": "မ", "Meaning_Essence_MM": "ပေါင်းစပ်ထားသော ထိုးဖောက်မှု (Penetration)", "T_Code": "T003", "Status": "Unverified"},
    {"Character": "ခြ", "Lakkhaṇa_Code": "147", "Fo_Ma": "မ", "Meaning_Essence_MM": "ထုတ်ဖော်ထားသော ထိုးဖောက်မှု (Penetration)", "T_Code": "T003", "Status": "Unverified"},
    {"Character": "ဂျ", "Lakkhaṇa_Code": "148", "Fo_Ma": "ဖို", "Meaning_Essence_MM": "ပေါင်းစပ်ထားသော စုဆောင်းမှု (Gathering)", "T_Code": "T005", "Status": "Unverified"},
    {"Character": "ဃျ", "Lakkhaṇa_Code": "149", "Fo_Ma": "မ", "Meaning_Essence_MM": "ပေါင်းစပ်ထားသော ထိန်းသိမ်းမှု (Containment)", "T_Code": "T017", "Status": "Unverified"},
    {"Character": "ငြ", "Lakkhaṇa_Code": "150", "Fo_Ma": "ဖို", "Meaning_Essence_MM": "လှုပ်ရှားမှုနှင့် တည်မြဲသော ငြိမ်သက်ခြင်း", "T_Code": "T017", "Status": "Unverified"},
    {"Character": "ငြှ", "Lakkhaṇa_Code": "151", "Fo_Ma": "မ", "Meaning_Essence_MM": "ပြင်းထန်မှုနှင့် တည်မြဲသော ငြိမ်သက်ခြင်း", "T_Code": "T017", "Status": "Unverified"},
    
    # ပျ/ပြ Series (Lakkhaṇa 152-157)
    {"Character": "ပျ", "Lakkhaṇa_Code": "152", "Fo_Ma": "ဖို", "Meaning_Essence_MM": "ပေါင်းစပ်ထားသော အစပြုမှု (Initiation)", "T_Code": "T001", "Status": "Unverified"},
    {"Character": "ပြ", "Lakkhaṇa_Code": "152", "Fo_Ma": "ဖို", "Meaning_Essence_MM": "ထုတ်ဖော်ထားသော အစပြုမှု (Initiation)", "T_Code": "T001", "Status": "Unverified"},
    {"Character": "ဖျ", "Lakkhaṇa_Code": "153", "Fo_Ma": "မ", "Meaning_Essence_MM": "ပေါင်းစပ်ထားသော ဖြန့်ကျက်မှု (Expansion)", "T_Code": "T003", "Status": "Unverified"},
    {"Character": "ဖြ", "Lakkhaṇa_Code": "153", "Fo_Ma": "မ", "Meaning_Essence_MM": "ထုတ်ဖော်ထားသော ဖြန့်ကျက်မှု (Expansion)", "T_Code": "T003", "Status": "Unverified"},
    {"Character": "ဗျ", "Lakkhaṇa_Code": "154", "Fo_Ma": "ဖို", "Meaning_Essence_MM": "ပေါင်းစပ်ထားသော အင်အား (Force)", "T_Code": "T005", "Status": "Unverified"},
    {"Character": "ဗြ", "Lakkhaṇa_Code": "155", "Fo_Ma": "ဖို", "Meaning_Essence_MM": "ထုတ်ဖော်ထားသော အင်အား (Force)", "T_Code": "T005", "Status": "Unverified"},
    {"Character": "ဘျ", "Lakkhaṇa_Code": "156", "Fo_Ma": "မ", "Meaning_Essence_MM": "ပေါင်းစပ်ထားသော တည်မြဲမှု (Stability)", "T_Code": "T017", "Status": "Unverified"},
    {"Character": "ဘြ", "Lakkhaṇa_Code": "157", "Fo_Ma": "မ", "Meaning_Essence_MM": "ထုတ်ဖော်ထားသော တည်မြဲမှု (Stability)", "T_Code": "T017", "Status": "Unverified"},
    {"Character": "မျ", "Lakkhaṇa_Code": "157", "Fo_Ma": "ဖို", "Meaning_Essence_MM": "ပေါင်းစပ်ထားသော ပေါင်းစပ်ခြင်း (Merging)", "T_Code": "T001", "Status": "Unverified"},
    {"Character": "မြ", "Lakkhaṇa_Code": "157", "Fo_Ma": "ဖို", "Meaning_Essence_MM": "ထုတ်ဖော်ထားသော ပေါင်းစပ်ခြင်း (Merging)", "T_Code": "T001", "Status": "Unverified"},
    {"Character": "မျှ", "Lakkhaṇa_Code": "158", "Fo_Ma": "မ", "Meaning_Essence_MM": "ပေါင်းစပ်ထားသော မျှတမှု (Balance)", "T_Code": "T003", "Status": "Unverified"},
    {"Character": "မြှ", "Lakkhaṇa_Code": "158", "Fo_Ma": "မ", "Meaning_Essence_MM": "ထုတ်ဖော်ထားသော မျှတမှု (Balance)", "T_Code": "T003", "Status": "Unverified"},
]

# ==================== CONSONANT CLUSTERS (M2 Lakkhaṇa: 001-006) ====================
# ဗျည်းတွဲ လေးမျိုး (ျ, ြ, ွ, ှ) နှင့် ဒေသိယအသံများ (္လ, ္ရ)
CONSONANT_CLUSTERS_DATA = [
    {"Character": "ျ", "Lakkhaṇa_Code": "001", "Meaning_Essence_MM": "ယပင့် ပြောင်းလဲမှု (Phonetic Mutation)", "Effect_Type": "Phonetic_Duplication"},
    {"Character": "ြ", "Lakkhaṇa_Code": "002", "Meaning_Essence_MM": "ရရစ် ပြောင်းလဲမှု (Rotational Shift)", "Effect_Type": "Phonetic_Duplication"},
    {"Character": "ွ", "Lakkhaṇa_Code": "003", "Meaning_Essence_MM": "ဝဆွဲ ပျံ့နှံ့မှု (Sound Diffusion)", "Effect_Type": "Sound_Extension"}, # ဗျည်းသံ လိုအပ်ချက်ကြောင့် အသံပွား
    {"Character": "ှ", "Lakkhaṇa_Code": "004", "Meaning_Essence_MM": "ဟထိုး တုန်ခါမှု (Aspiration/Vibration)", "Effect_Type": "Sound_Extension"}, # ဗျည်းသံ လိုအပ်ချက်ကြောင့် အသံပွား
    {"Character": "္လ", "Lakkhaṇa_Code": "005", "Meaning_Essence_MM": "လဆွဲ ဆက်သွယ်မှု (Lateral Connection)", "Effect_Type": "Dialectal_Sound"},
    {"Character": "္ရ", "Lakkhaṇa_Code": "006", "Meaning_Essence_MM": "ရဆွဲ အရှိန်မှု (Rotational Momentum)", "Effect_Type": "Dialectal_Sound"}
]
```

### ၂။ `nstf_data/sandhi_system_data.py` (အသတ်စနစ်)

```python
# nstf_data/sandhi_system_data.py

# ==================== SANDHI (အသတ်) SYSTEM - M3 Layer ====================

SANDHI_SYSTEM_DATA = [
    # Short-Stop Sandhi (သံရပ်၊ သံတိုအသတ်) - သံရပ်/သံတို
    {"Character": "က်", "Sandhi_Type": "Short_Stop", "Original_Consonant": "က", "Effect_MM": "ချက်ချင်းရပ်တန့်ခြင်း (Abrupt Termination)", "Intensity": "High"},
    {"Character": "စ်", "Sandhi_Type": "Short_Stop", "Original_Consonant": "စ", "Effect_MM": "ချွန်ထက်စွာ ဖြတ်ခြင်း (Sharp Cut-off)", "Intensity": "High"},
    {"Character": "တ်", "Sandhi_Type": "Short_Stop", "Original_Consonant": "တ", "Effect_MM": "ဦးတည်ပြီး ရပ်ခြင်း (Directed Stop)", "Intensity": "Medium"},
    {"Character": "ပ်", "Sandhi_Type": "Short_Stop", "Original_Consonant": "ပ", "Effect_MM": "ပိတ်ဆို့ပြီး အဆုံးသတ်ခြင်း (Sealed Termination)", "Intensity": "High"},
    
    # Sustained Sandhi (သံရှိန်ရှိအသတ်) - သံရှည်/သံရှိန်ရှိ
    {"Character": "င်", "Sandhi_Type": "Sustained", "Original_Consonant": "င", "Effect_MM": "တီတတ်သော အဆုံးသတ်ခြင်း (Resonant Closure)", "Intensity": "Low"},
    {"Character": "ည်", "Sandhi_Type": "Sustained", "Original_Consonant": "ည", "Effect_MM": "စည်းကမ်းဖြင့် ပြီးဆုံးခြင်း (Disciplined Completion)", "Intensity": "Medium"},
    {"Character": "န်", "Sandhi_Type": "Sustained", "Original_Consonant": "န", "Effect_MM": "ညှိနှိုင်းပြီး အဆုံးသတ်ခြင်း (Balanced Ending)", "Intensity": "Low"},
    {"Character": "မ်", "Sandhi_Type": "Sustained", "Original_Consonant": "မ", "Effect_MM": "အနှစ်သာရဖြင့် ပြီးဆုံးခြင်း (Essential Completion)", "Intensity": "Medium"},
    {"Character": "ယ်", "Sandhi_Type": "Sustained", "Original_Consonant": "ယ", "Effect_MM": "ကူးပြောင်းပြီး အဆုံးသတ်ခြင်း (Transitional Closure)", "Intensity": "Low"}
    
    # ဉ် (ညငယ် အသတ်) - သမိုင်းကြောင်းအရ ည နှင့် အတူတူ သို့မဟုတ် ဆက်စပ်
    # ဤနေရာတွင် ည်/ဉ် ကို စုစည်းထားသည်။ သီးခြားခွဲခြာလိုပါက Lakkhaṇa Code ဖြင့် ပြန်လည် ထည့်သွင်းနိုင်သည်။
]
```

### ၃။ `nstf_engine/adaptive_engine.py` (သင်ယူနိုင်သော အင်ဂျင်)

```python
# nstf_engine/adaptive_engine.py

from typing import Dict, List
from datetime import datetime
from nstf_data.special_consonants_data import SPECIAL_CONSONANTS_DATA, CONSONANT_CLUSTERS_DATA
from nstf_data.sandhi_system_data import SANDHI_SYSTEM_DATA

# NSTF_BASE_DATA တွင် ပုံမှန် ဗျည်း ၅၈လုံး အပါအဝင် NSTF_Full_Framework_Final.csv မှ ဒေတာအားလုံး ပါဝင်သည်ဟု ယူဆသည်။
# ဤနမူနာတွင် အထူးဒေတာများကိုသာ အဓိကထား အသုံးပြုထားသည်။

class NSTFAdaptiveEngine:
    """NNLDS အတွက် အဆက်မပြတ် သင်ယူနိုင်သော၊ ယုံကြည်ရမှုအပေါ် အခြေခံသည့် စနစ်"""
    
    def __init__(self):
        # Base Data: အထူးဗျည်းများနှင့် ဗျည်းတွဲများ
        self.special_consonants = SPECIAL_CONSONANTS_DATA
        self.clusters = CONSONANT_CLUSTERS_DATA
        self.sandhi_system = SANDHI_SYSTEM_DATA
        
        # Adaptive Learning & Expert Validation Data
        self.user_feedback_log: List[Dict] = []
        self.uncertain_patterns: Dict = {}
        self.expert_validation_queue: List[Dict] = []
        
    def _find_match(self, char: str) -> Dict:
        """ဒေတာအားလုံးတွင် တူညီသော စာလုံးကို ရှာဖွေသည်။"""
        
        # 1. Special Consonants (ကျ/ပျ ဝဂ်)
        match = next((item for item in self.special_consonants if item["Character"] == char), None)
        if match:
            return {**match, "Type": "SpecialConsonant", "confidence": 0.7, "source": "official_unverified_lakkhaṇa"}

        # 2. Consonant Clusters (ျ, ြ, ွ, ှ)
        match = next((item for item in self.clusters if item["Character"] == char), None)
        if match:
            return {**match, "Type": "ConsonantCluster", "confidence": 1.0, "source": "validated_m2_layer"}
            
        # 3. Sandhi System (အသတ်)
        match = next((item for item in self.sandhi_system if item["Character"] == char), None)
        if match:
            return {**match, "Type": "Sandhi", "confidence": 0.9, "source": "validated_m3_layer"}

        # 4. Uncertain Patterns (အသုံးပြုသူ တင်ပြထားသော)
        if char in self.uncertain_patterns:
            pattern = self.uncertain_patterns[char]
            return {
                "Character": char,
                "Type": pattern.get("Type", "Uncertain"),
                "confidence": pattern.get("user_confidence", 0.5),
                "source": "user_contributed_pending"
            }
            
        # Default/Unknown (အခြား ဗျည်း၊ သရ သို့မဟုတ် မသိသော စာလုံး)
        # ဤနေရာတွင် မူရင်း ဗျည်း ၅၈ လုံးနှင့် သရများ စစ်ဆေးခြင်း ပါဝင်ရမည်။
        return {"Character": char, "Type": "Unknown/Base", "confidence": 1.0, "source": "default_or_base_data"}

    def analyze_with_confidence(self, text: str) -> Dict:
        """ယုံကြည်ရမှု (Confidence) အမှတ်ဖြင့် စာသားကို ခွဲခြမ်းစိတ်ဖြာသည်။"""
        
        analysis = {
            "text": text,
            "character_analyses": [],
            "overall_confidence": 1.0,
            "uncertain_elements": [],
            "requires_expert_review": False
        }
        
        for char in text:
            char_analysis = self._find_match(char)
            analysis["character_analyses"].append(char_analysis)
            
            # Confidence Calculation
            confidence = char_analysis.get("confidence", 1.0)
            if confidence < 0.9: # 90% အောက်ဆိုလျှင် မသေချာဟု သတ်မှတ်သည်။
                analysis["uncertain_elements"].append(char)
                analysis["overall_confidence"] *= confidence
                
        # စုစုပေါင်း ယုံကြည်ရမှု အမှတ်
        analysis["requires_expert_review"] = analysis["overall_confidence"] < 0.8 
        return analysis
        
    # --- Adaptive Learning Functions (ဆက်လက်သင်ယူနိုင်သော လုပ်ဆောင်ချက်များ) ---
    
    def submit_user_feedback(self, character: str, proposed_data: Dict, user_confidence: float = 0.5):
        """အသုံးပြုသူထံမှ အကြံပြုချက်များကို လက်ခံသည်။"""
        
        feedback_entry = {
            "timestamp": datetime.now().isoformat(),
            "character": character,
            "proposed_data": proposed_data,
            "user_confidence": user_confidence,
            "validation_status": "pending"
        }
        
        self.user_feedback_log.append(feedback_entry)
        
        # ယာယီအသုံးပြုရန်
        self.uncertain_patterns[character] = {**proposed_data, "user_confidence": user_confidence}
        
    def export_validation_queue(self) -> List[Dict]:
        """ပညာရှင်များ စစ်ဆေးရန် စာရင်းကို ထုတ်ပေးသည်။"""
        # ဤနေရာတွင် self.user_feedback_log ကို အခြေခံ၍ စစ်ဆေးရန် စာရင်းကို ပြန်လည် ဖွဲ့စည်းနိုင်သည်
        return self.expert_validation_queue
        
    def expert_validate_pattern(self, character: str, validated_data: Dict, target_dataset: str):
        """ပညာရှင် အတည်ပြုချက်ကို စနစ်ထဲသို့ ထည့်သွင်းသည်။"""
        
        # ဥပမာ: "special_consonants" dataset ထဲသို့ ထည့်သွင်းခြင်း
        validated_entry = {
            **validated_data,
            "Status": "ExpertValidated",
            "validation_date": datetime.now().isoformat()
        }
        
        if target_dataset == "special_consonants":
            # ရှိပြီးသားကို အစားထိုး/အသစ်ထည့်
            self.special_consonants = [item for item in self.special_consonants if item["Character"] != character]
            self.special_consonants.append(validated_entry)
        
        # uncertain patterns မှ ဖယ်ရှားခြင်း
        if character in self.uncertain_patterns:
            del self.uncertain_patterns[character]
            
        print(f"INFO: '{character}' ကို '{target_dataset}' ထဲသို့ ပညာရှင် အတည်ပြုချက်ဖြင့် ထည့်သွင်းပြီး။")
```

### ၄။ `nstf_engine/dialect_handler.py` (ဒေသိယ သံထွက် ထိန်းချုပ်မှု)

```python
# nstf_engine/dialect_handler.py

from typing import Dict, List

class DialectVariationHandler:
    """ဒေသအလိုက် သို့မဟုတ် စံအလိုက် ကွဲပြားမှုများကို စီမံခန့်ခွဲသည်"""
    
    def __init__(self):
        # ဒေသအလိုက် ဗျည်းသံများကို ဖော်ပြထားသော စံနှုန်းများ
        self.dialect_profiles = {
            "mandalay_standard": {
                "description": "မန္တလေးဒေသဗဟိုပြု စံသတ်မှတ်ချက်။ ကျ/ကြ, ပျ/ပြ ကို ရှင်းလင်းစွာ ခွဲခြားသည်။",
                "special_consonants": ["ကျ", "ကြ", "ချ", "ခြ", "ပျ", "ပြ", "ဖျ", "ဖြ", "ငြ", "ငြှ", "္လ", "္ရ"],
                "validation_status": "community_verified"
            },
            "yangon_modern": {
                "description": "ရန်ကုန်ခေတ်သစ် အသံထွက်စံ။ တွဲဗျည်းအများစုအား 'ကျ' (အသံတူ) သို့ စုစည်းလေ့ရှိသည်။",
                "special_consonants": ["ကျ", "ချ", "ဂျ", "ပျ", "ဖျ", "ဗျ", "ဘျ", "မျ", "မျှ"],  # 'ကြ, ပြ' စသည်တို့ကို နည်းပါးစွာ သုံးနှုန်းခြင်း
                "validation_status": "partially_verified"
            },
            "traditional_academic": {
                "description": "ရိုးရာပညာရပ်ဆိုင်ရာ စံ။ အက္ခရာအားလုံး၏ မူလသံကို ထိန်းသိမ်းသည်။",
                "special_consonants": ["ကျ", "ကြ", "ချ", "ခြ", "ဂျ", "ဃျ", "ငြ", "ငြှ", "ပျ", "ပြ", "ဖျ", "ဖြ", "ဗျ", "ဗြ", "ဘျ", "ဘြ", "မျ", "မြ", "မျှ", "မြှ"],
                "validation_status": "expert_verified"
            }
        }
    
    def get_dialect_analysis(self, text: str, dialect: str = "mandalay_standard") -> Dict:
        """ပေးထားသော စာသားကို သတ်မှတ်ထားသော ဒေသိယစံအရ ခွဲခြမ်းစိတ်ဖြာသည်။"""
        
        profile = self.dialect_profiles.get(dialect, self.dialect_profiles["mandalay_standard"])
        
        analysis = {
            "dialect": dialect,
            "dialect_compatibility": 0.0,
            "regional_characteristics": [],
            "deviations": []
        }
        
        all_known_specials = set()
        for p in self.dialect_profiles.values():
            all_known_specials.update(p["special_consonants"])
            
        special_chars_in_text = [c for c in text if c in all_known_specials]
        
        dialect_matches = [c for c in special_chars_in_text if c in profile["special_consonants"]]
        
        if len(special_chars_in_text) > 0:
            analysis["dialect_compatibility"] = len(dialect_matches) / len(special_chars_in_text)
            
        analysis["regional_characteristics"] = dialect_matches
        
        # ဒေသိယစံနှင့် ကွဲလွဲမှုများ
        for char in special_chars_in_text:
            if char not in profile["special_consonants"]:
                analysis["deviations"].append({
                    "character": char,
                    "reason": f"'{dialect}' စံတွင် ဤဗျည်းကို ပုံမှန်အဖြစ် သတ်မှတ်ခြင်းမရှိပါ။"
                })
                
        return analysis
```

### ၅။ `main_system.py` (အဓိက စနစ်)

```python
# main_system.py - The Production System of NSTF-NNLDS

from typing import Dict
from nstf_engine.adaptive_engine import NSTFAdaptiveEngine
from nstf_engine.dialect_handler import DialectVariationHandler
from nstf_data.sandhi_system_data import SANDHI_SYSTEM_DATA

class NSTFProductionSystem:
    """အပြည့်အစုံ NSTF-NNLDS စနစ်"""
    
    def __init__(self):
        self.adaptive_engine = NSTFAdaptiveEngine()
        self.dialect_handler = DialectVariationHandler()
        self.learning_mode = True # အသုံးပြုသူ၏ ဖြည့်စွက်သင်ယူမှုများ လက်ခံခြင်းကို ဖွင့်ထားသည်

    def comprehensive_analysis(self, text: str, dialect: str = "mandalay_standard") -> Dict:
        """စာသားတစ်ခုကို အပြည့်အစုံ ခွဲခြမ်းစိတ်ဖြာခြင်း"""
        
        # 1. Basic & Confidence Analysis (Lakkhaṇa ဗီဇ၊ ယုံကြည်ရမှု အမှတ်)
        basic_analysis = self.adaptive_engine.analyze_with_confidence(text)
        
        # 2. Dialect Analysis (ဒေသအလိုက် စံ၊ ကွဲလွဲမှုများ)
        dialect_analysis = self.dialect_handler.get_dialect_analysis(text, dialect)
        
        # 3. Sandhi Analysis (အသတ်စနစ်)
        sandhi_patterns = self._extract_sandhi_patterns(basic_analysis["character_analyses"])
        
        return {
            "input_text": text,
            "lakkhaṇa_analysis": basic_analysis,
            "dialect_analysis": dialect_analysis,
            "sandhi_patterns": sandhi_patterns,
            "system_status": self._generate_system_status(basic_analysis, dialect_analysis),
        }

    def _extract_sandhi_patterns(self, char_analyses: List[Dict]) -> List[Dict]:
        """ခွဲခြမ်းစိတ်ဖြာချက်များမှ အသတ် (Sandhi) ပုံစံများကို ထုတ်ယူသည်။"""
        sandhi_list = [
            {
                "character": analysis["Character"],
                "type": analysis.get("Sandhi_Type"),
                "original_root": analysis.get("Original_Consonant"),
                "effect_mm": analysis.get("Effect_MM")
            }
            for analysis in char_analyses if analysis.get("Type") == "Sandhi"
        ]
        return sandhi_list

    def _generate_system_status(self, basic_analysis: Dict, dialect_analysis: Dict) -> Dict:
        """စနစ်၏ အခြေအနေနှင့် အကြံပြုချက်များကို ထုတ်လုပ်သည်။"""
        
        status = {
            "overall_confidence": basic_analysis["overall_confidence"],
            "requires_expert_review": basic_analysis["requires_expert_review"],
            "dialect_match": f"{dialect_analysis['dialect']} စံနှင့် ကိုက်ညီမှု: {dialect_analysis['dialect_compatibility']:.2f}",
            "recommendation": ""
        }
        
        if basic_analysis["requires_expert_review"]:
            status["recommendation"] = "သတ်မှတ်မထားသော/မသေချာသော အချက်အလက်များ ပါဝင်သောကြောင့် ပညာရှင် အတည်ပြုချက် လိုအပ်ပါသည်။"
        elif dialect_analysis["dialect_compatibility"] < 1.0:
            status["recommendation"] = f"အသုံးပြုသည့် ဒေသိယ ဗျည်းသံများသည် {dialect_analysis['dialect']} စံနှင့် ကွဲလွဲမှုများရှိနေပါသည်။"
        else:
            status["recommendation"] = "ခွဲခြမ်းစိတ်ဖြာမှုမှာ စနစ်၏ စံနှုန်းများနှင့် ကိုက်ညီပါသည်။"
            
        return status
        
    def submit_correction(self, character: str, user_interpretation: Dict, user_confidence: float):
        """ပြင်ဆင်ချက်များ တင်ပြခြင်း (Adaptive Learning)"""
        if self.learning_mode:
            return self.adaptive_engine.submit_user_feedback(character, user_interpretation, user_confidence)
        return {"status": "learning_mode_disabled"}

# ဥပမာ အသုံးပြုပုံ
if __name__ == '__main__':
    nstf_system = NSTFProductionSystem()
    
    # ဥပမာ စာသား: 'ကျေးဇူးတင်ပါတယ်' (ကျ - Pseudo-Consonant, း - Tone, မ် - Sustained Sandhi)
    test_text = "ကျေးဇူးတင်ပါတယ်"
    
    # Comprehensive Analysis
    result = nstf_system.comprehensive_analysis(test_text, "mandalay_standard")
    
    print("=========================================")
    print("NSTF-NNLDS Comprehensive Analysis Report")
    print("=========================================")
    
    print(f"Input: {result['input_text']}")
    print(f"Overall Confidence: {result['lakkhaṇa_analysis']['overall_confidence']:.4f}")
    print(f"Requires Expert Review: {result['lakkhaṇa_analysis']['requires_expert_review']}")
    print("-" * 35)
    
    print("--- Detailed Lakkhaṇa Analysis ---")
    for analysis in result['lakkhaṇa_analysis']['character_analyses']:
        # လက္ခဏာ အဓိပ္ပာယ်ကို ရှင်းရှင်းလင်းလင်း ဖော်ပြရန်
        meaning = analysis.get("Meaning_Essence_MM", "Base Character")
        print(f"  {analysis['Character']} ({analysis['Type']}): {meaning} (Confidence: {analysis['confidence']:.2f})")
    print("-" * 35)
    
    print("--- Sandhi System Analysis ---")
    for sandhi in result['sandhi_patterns']:
        print(f"  {sandhi['character']} - အမျိုးအစား: {sandhi['type']} ({sandhi['effect_mm']})")
    print("-" * 35)
    
    print("--- System Status & Recommendations ---")
    print(f"  {result['system_status']['dialect_match']}")
    print(f"  အကြံပြုချက်: {result['system_status']['recommendation']}")
    print("=========================================")
```

ဤ **Python Files** များကို GitHub တွင် ခွဲခြား တင်နိုင်ပါတယ်။ `main_system.py` ဖိုင်သည် စနစ်တစ်ခုလုံးကို စတင်အသုံးပြုရန်အတွက် အဓိက ဖိုင်ဖြစ်ပါတယ်။
