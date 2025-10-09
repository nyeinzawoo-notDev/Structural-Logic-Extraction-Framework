Python

# File: nstf/core.py

import json
import os

class NSTFAnalyzer:
    """
    NSTF Framework ၏ အဓိက Logic Class ဖြစ်ပြီး၊ JSON ဖိုင်မှ T-Code Ontology 
    ကို တင်ကာ Input Scenario များ၏ ကျင့်ဝတ်ဆိုင်ရာ ပဋိပက္ခများကို ရှာဖွေသည်။
    """

    def __init__(self):
        # Data ဖိုင်၏ လမ်းကြောင်းကို တိကျစွာ သတ်မှတ်ခြင်း (core.py မှ data ဖိုဒါသို့)
        base_dir = os.path.dirname(os.path.abspath(__file__))
        data_path = os.path.join(base_dir, '..', 'data', 't_codes_ontology.json')
        
        self.ontology = self._load_ontology(data_path)

    def _load_ontology(self, file_path: str) -> dict:
        """JSON ဖိုင်မှ T-Code Ontology Data ကို တင်ခြင်း"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error: Ontology file not found at {file_path}. Using empty ontology.")
            return {}

    def _extract_t_codes_from_text(self, text: str) -> list:
        """
        Input Text မှ NSTF T-Code များကို ထုတ်ယူခြင်း။
        (လက်တွေ့တွင် NLP Model ဖြင့် လုပ်ဆောင်သော်လည်း၊ ယခုမူ စာသားဖြင့် ရှာဖွေခြင်းဖြင့် ကိုယ်စားပြုသည်။)
        """
        text_lower = text.lower()
        found_codes = set()
        
        # Scenario များမှ T-Code ၏ အနှစ်သာရ စာလုံးများကို ရှာဖွေခြင်း
        if any(word in text_lower for word in ["innovation", "growth", "profit", "စီးပွားရေး"]):
            found_codes.add("T003") 
        if any(word in text_lower for word in ["ethics", "privacy", "boundary", "သီလ"]):
            found_codes.add("T017")
        if any(word in text_lower for word in ["land", "stability", "မြေယာ"]):
            found_codes.add("T004")
        if any(word in text_lower for word in ["healing", "solution", "ကုသ"]):
            found_codes.add("T009")
        if any(word in text_lower for word in ["culture", "religious beliefs", "ယဉ်ကျေးမှု"]):
             found_codes.add("T017") 
        
        return list(found_codes)

    def detect_t_code_tensions(self, t_codes: list) -> list:
        """
        ပေးထားသော T-Code များအနက် ပဋိပက္ခ ဖြစ်နိုင်ချေရှိသော T-Code အတွဲများကို ရှာဖွေသည်။
        """
        tensions = set()
        
        for i in range(len(t_codes)):
            for j in range(i + 1, len(t_codes)):
                code_a = t_codes[i]
                code_b = t_codes[j]
                
                # Ontology ထဲက potential_tension စာရင်းဖြင့် စစ်ဆေးခြင်း
                if code_a in self.ontology and code_b in self.ontology:
                    if code_b in self.ontology[code_a]['potential_tension'] or \
                       code_a in self.ontology[code_b]['potential_tension']:
                        tensions.add(tuple(sorted((code_a, code_b))))

        # Tension List ကို နာမည်များဖြင့် ပြန်ထုတ်ခြင်း
        tension_list = [
            f"{a} ({self.ontology[a]['essence']}) vs {b} ({self.ontology[b]['essence']})"
            for a, b in tensions
        ]
        
        return tension_list

    def generate_guidance(self, tensions: list) -> str:
        """
        တွေ့ရှိထားသော ပဋိပက္ခများအပေါ် အခြေခံ၍ ကျင့်ဝတ်ဆိုင်ရာ လမ်းညွှန်ချက် ထုတ်ပေးသည်။
        """
        if not tensions:
            return "ACCEPT (သဘောတူပါ) - ကျင့်ဝတ်ဆိုင်ရာ ပဋိပက္ခမရှိပါ။"
        
        # T003 vs T017 (Innovation vs Ethics) လိုမျိုး အရေးကြီးတဲ့ ပဋိပက္ခများ
        if any("T017" in t and "T003" in t for t in tensions):
            return "REFUSE (ငြင်းပယ်ပါ) - လူသားတန်ဖိုး (T017) ကို အဓိကခြိမ်းခြောက်နေပါသည်။"
            
        # T009 vs T017 (Healing vs Culture) လိုမျိုး ညှိနှိုင်းရမည့် ပဋိပက္ခများ
        if any("T009" in t and "T017" in t for t in tensions):
            return "MODIFY (ပြုပြင်ပါ) - ယဉ်ကျေးမှုနှင့် လိုက်လျောညီထွေဖြစ်အောင် ပြုပြင်ပါ။"

        # အခြား ပဋိပက္ခများ
        return "MEDIATE (ညှိနှိုင်းပါ) - ဟန်ချက်ညီစေရန် အလျှော့အတင်း ပြုလုပ်ပါ။"
        
    def analyze_scenario(self, input_text: str) -> dict:
        """Scenario တစ်ခုလုံးကို NSTF Logic ဖြင့် ခွဲခြမ်းစိတ်ဖြာသည်။"""
        
        t_codes = self._extract_t_codes_from_text(input_text)
        tensions = self.detect_t_code_tensions(t_codes)
        guidance = self.generate_guidance(tensions)
        
        return {
            "input_scenario": input_text,
            "detected_t_codes": t_codes,
            "detected_tensions": tensions,
            "ethical_guidance": guidance
        }

if __name__ == "__main__":
    analyzer = NSTFAnalyzer()
    
    # JSON ဖိုင် မတွေ့ရင် Error ပြပါလိမ့်မယ်။
    if not analyzer.ontology:
        print("Cannot run analysis without T-Code Ontology data.")
    else:
        # စမ်းသပ်မှု နမူနာ (Global Ethics)
        scenario_1 = "A tech company collects user data without explicit consent to rapidly accelerate medical innovation."
        result_1 = analyzer.analyze_scenario(scenario_1)
        
        print("--- Scenario 1 Analysis ---")
        print(f"T-Codes: {result_1['detected_t_codes']}")
        print(f"Guidance: {result_1['ethical_guidance']}") 

        print("\n" + "="*30 + "\n")

        # စမ်းသပ်မှု နမူနာ (Cultural Conflict)
        scenario_2 = "Medical AI suggests a treatment that conflicts with the patient's religious beliefs and culture."
        result_2 = analyzer.analyze_scenario(scenario_2)
        
        print("--- Scenario 2 Analysis ---")
        print(f"T-Codes: {result_2['detected_t_codes']}")
        print(f"Guidance: {result_2['ethical_guidance']}") 
