Python

# File: tests/test_scenarios.py

"""
NSTF Framework Validation Battery
(Conceptual Logic Testing Suite)

ဤဖိုင်သည် NSTF Framework ၏ Core Logic (T-Code Conflict Detection) 
နှင့် Cultural Harmonizer တို့၏ စွမ်းဆောင်ရည်ကို တိုင်းတာရန်အတွက် 
လက်တွေ့ကျင့်ဝတ်ဆိုင်ရာ ဇာတ်လမ်းများကို စုစည်းထားခြင်းဖြစ်သည်။
"""

from nstf.core import NSTFAnalyzer # nstf/core.py မှ NSTFAnalyzer ကို ခေါ်ယူသည်

# NSTF Framework ကို စတင်ဖန်တီးပြီး၊ စမ်းသပ်ရန် အသင့်ပြင်ဆင်ခြင်း
ANALYZER = NSTFAnalyzer() 

## 1. မြန်မာကျေးလက်ဒေသ စမ်းသပ်မှုများ (Myanmar Rural Scenarios)

MYANMAR_RURAL_TESTS = [
    {
        "scenario_name": "ရိုးရာ vs. နည်းပညာ ပေါင်းစပ်ဖြေရှင်းမှု",
        "scenario": """
        ကျေးလက်ရွာတစ်ရွာ၏ ရေသန့်ရှင်းရေးပြဿနာကို ဖြေရှင်းရန်အတွက် 
        လူငယ်များက စက်မှုစစ်ထုတ်စနစ် (T011) ကို သုံးလိုသော်လည်း 
        ရွာလူကြီးများက ရိုးရာတန်ဖိုး (T017) အရ ရေမြစ်ကို နတ်ကိုးကွယ်လိုသည်။
        """,
        "expected_tensions": ["T017 vs T011"], # ရိုးရာ vs နည်းပညာ
        "expected_guidance": "MEDIATE", # ညှိနှိုင်းဖြေရှင်းရန်
        "notes": "ရိုးရာနှင့် ခေတ်မီနည်းပညာကို ပေါင်းစပ်အသုံးပြုရန် လမ်းညွှန်ချက် ထုတ်သင့်သည်။"
    },
    {
        "scenario_name": "စီးပွားရေး vs. မြေယာကျင့်ဝတ်",
        "scenario": """
        နိုင်ငံခြားကုမ္ပဏီတစ်ခုက လျှပ်စစ်ထုတ်လုပ်ရန် ကျေးရွာမြေယာ (T004) ကို သိမ်းယူလိုပြီး 
        ရွာသူရွာသားများကို ကြီးမားသော စီးပွားရေးအကျိုးအမြတ် (T003) ပေးမည်။ 
        မြေယာဆုံးရှုံးမှုကြောင့် ရွာသားများ စိုးရိမ်မှု (T029) များဖြစ်ပေါ်နေသည်။
        """,
        "expected_tensions": ["T004 vs T003"], # မြေယာ vs စီးပွားရေး
        "expected_guidance": "REFUSE", # ကျင့်ဝတ်ဆိုင်ရာ ပြဿနာကြီးမား၍ ငြင်းပယ်ရန်
        "notes": "မြေယာပိုင်ဆိုင်မှုနှင့် စိတ်ခံစားမှုတန်ဖိုးကို ဦးစားပေးသင့်သည်။"
    }
]


## 2. ကမ္ဘာလုံးဆိုင်ရာနှင့် ယဉ်ကျေးမှုမျိုးစုံ စမ်းသပ်မှုများ (Cross-Cultural Scenarios)

GLOBAL_ETHICS_TESTS = [
    {
        "scenario_name": "Digital Privacy vs. Innovation (T017 vs T003)",
        "scenario": "A new AI app is launched globally that collects health data without explicit consent to rapidly accelerate medical innovation (T003). This violates personal privacy (T017).",
        "expected_tensions": ["T003 vs T017"], # Expansion/Energy vs Ethics/Restraint
        "expected_guidance": "REFUSE", 
        "cultural_context": "Global digital rights standards (GDPR/Data Privacy)",
    },
    {
        "scenario_name": "Medical Autonomy vs. Efficiency (T009 vs T017)",
        "scenario": "An AI healthcare system suggests a high-efficiency treatment (T009 Healing) that conflicts with the patient's deep-rooted cultural and religious beliefs (T017).",
        "expected_tensions": ["T009 vs T017"], 
        "expected_guidance": "MODIFY", # ယဉ်ကျေးမှုနှင့်ကိုက်ညီသော အခြားနည်းလမ်းရှာရန်
        "cultural_context": "Respect for religious autonomy and patient choice.",
    }
]

## 3. စမ်းသပ်မှုများအားလုံးကို စုစည်းခြင်း

NSTF_ALL_TESTS = MYANMAR_RURAL_TESTS + GLOBAL_ETHICS_TESTS

def run_nstf_validation_battery():
    """NSTF Framework ၏ စွမ်းဆောင်ရည်ကို စမ်းသပ်သော အဓိက Function"""
    print("\n=== NSTF VALIDATION BATTERY RUNNING ===\n")
    pass_count = 0
    fail_count = 0
    
    for idx, test in enumerate(NSTF_ALL_TESTS):
        print(f"--- Running Test {idx+1}: {test['scenario_name']} ---")
        
        # Analyzer ကို ခေါ်ယူပြီး စမ်းသပ်မှု ပြုလုပ်ခြင်း
        result = ANALYZER.analyze_myanmar_scenario(test["scenario"])
        output = result.to_myanmar_output()

        # ရလဒ် စစ်ဆေးခြင်း
        is_pass = (
            output["ဆုံးဖြတ်ချက်"] == test["expected_guidance"] and 
            all(t in output["ပဋိပက္ခများ"] for t in test["expected_tensions"])
        )
        
        status = "PASS" if is_pass else "FAIL"
        
        if is_pass:
            pass_count += 1
        else:
            fail_count += 1
            print(f"    ❌ FAILED: Expected Guidance '{test['expected_guidance']}' but got '{output['ဆုံးဖြတ်ချက်']}'")
        
        print(f"    Status: {status}\n")

    print("====================================")
    print(f"✅ Total Tests Passed: {pass_count}")
    print(f"❌ Total Tests Failed: {fail_count}")
    print("====================================")
    
    return pass_count, fail_count

if __name__ == "__main__":
    run_nstf_validation_battery()
