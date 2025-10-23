# 💾 Production-Ready Data Sets (`data/`)

ဤဖိုင်တွဲသည် **NSTF/SLEF Core Engine** မှ **တိုက်ရိုက် အသုံးပြုရန်** စီမံထားသော၊ စစ်ဆေးပြီးသော (Validated) နှင့် နည်းပညာသမားများအတွက် အသုံးတည့်မည့် **Structured Data Sets** များကိုသာ သိမ်းဆည်းထားသော နေရာ ဖြစ်ပါသည်။

## 📝 ဖိုင်တွဲ၏ ရည်ရွယ်ချက် (Purpose)

ဤနေရာရှိ Data များသည် Framework ၏ runtime logic ကို တိုက်ရိုက် မောင်းနှင်ပါသည်။
* **Ontologies:** T-Codes, Philosophical Dimensions ၏ နောက်ဆုံးအတည်ပြုထားသော Data များ။
* **Schemas:** Ethical Engine ၏ Rule Structure များ။
* **Vector Space:** 17D VNyein Vector တွက်ချက်မှုအတွက် လိုအပ်သော Reference Data များ။

## ⚠️ သိမ်းဆည်းရမည့် ဖိုင်အမျိုးအစားများ (File Types)

* **Structured Data (Final):** `.json`, `.yaml`, `.csv` (Code မှ parse လုပ်ရန် အသင့်ဖြစ်ရမည်။)
* **NO CODE:** Python Code (`.py`) သို့မဟုတ် Documentation များ ထားရှိရန် မလိုပါ။

**NOTE:** ဤ Data များသည် `modules/` Folder မှ Code များဖြင့် တိုက်ရိုက်ချိတ်ဆက်ထားပြီး၊ အပြောင်းအလဲတိုင်းသည် Framework ၏ Deterministic Ethical Guidance ကို သက်ရောက်မှု ရှိပါသည်။

# 📊 Core Data Files (`data/`)

This folder is the central repository for all essential, structured data files used by the NSTF/SLEF core engine.

## 📝 Folder Purpose

Data here is used to directly power the framework's logic. Examples include:
* **Ontologies:** T-Codes, Philosophical Dimensions.
* **Schemas:** Ethical Engine rule structures.
* **Static Reference Data:** Large linguistic datasets.

## ⚠️ Important Rules

* **File Types:** `.json`, `.tsv`, `.csv`, `.yaml` (Structured Data only).
* **NO Source Code:** Python files (`.py`) are strictly prohibited here; they belong in the **`modules/`** folder.
* **Data Integrity:** Changes to these files must follow a strict review process as they directly affect the framework's deterministic ethical guidance.
* **Key Files:**
    * `ultimate_ethical_engine.json` (The Core Schema)
    * `t_codes_ontology.json` (T-Code Definitions)
