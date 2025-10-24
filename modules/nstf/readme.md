# 📂 modules/nstf/ Directory

ဤ Directory သည် NSTF (Nyein Structural T-Code Framework) ၏ အဓိက လုပ်ငန်းဆောင်တာများ (Core Logic) ကို တာဝန်ယူသည့် Python Package ဖြစ်ပါသည်။ ၎င်းသည် Framework ၏ နှလုံးသားဖြစ်သော Logic Component များကို စနစ်တကျ ခွဲခြားစုစည်းထားသော နေရာဖြစ်သည်။

## 🎯 ရည်ရွယ်ချက်

Core Framework မှ ခေါ်ယူ အသုံးပြုမည့် **NSTF-specific Logic** များနှင့် **T-Code Analysis** စနစ်များကို သိမ်းဆည်းရန်။

## 📋 ပါဝင်ရမည့် အချက်များ

* **`core.py`**: NSTFAnalyzer အတန်း (Class) ကဲ့သို့သော Framework ၏ အဓိက စတင်အသုံးပြုနိုင်သည့် Logic များ။
* **`t_code_processor.py`**: T-Code ထုတ်ယူခြင်း၊ ပဋိပက္ခ ရှာဖွေခြင်း စသည့် လုပ်ငန်းစဉ်များကို ခွဲထုတ်ထားသည့် Utility/Helper Logic များ။
* **`ethical_resolver.py`**: လမ်းညွှန်ချက် (Guidance) ထုတ်ပေးသည့် Logic များ။
* **`__init__.py`**: ဤဖိုဒါကို Python Package အဖြစ် သတ်မှတ်ရန်နှင့် အခြား module များသို့ လိုအပ်သည့် function များကို ထုတ်ပေးရန်။

## ⚠️ လိုက်နာရမည့် စည်းမျဉ်းများ

* **Code Only:** Python Code (`.py`) များသာ ပါဝင်ရပါမည်။
* **No Data/Docs:** `data/` ဖိုဒါထဲမှ JSON/YAML ဖိုင်များ သို့မဟုတ် `docs/` ဖိုဒါထဲမှ Documentation များ လုံးဝမပါဝင်ရပါ။
* **Dependency Management:** Data ကို ခေါ်ယူရန် လိုအပ်ပါက (ဥပမာ- `core.py` တွင်)၊ Data ဖိုဒါသို့ လမ်းကြောင်းမှန်ကန်စွာ သတ်မှတ်ပေးရပါမည်။ (e.g., `'..', '..', 'data', ...`)
