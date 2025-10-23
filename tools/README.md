# 🛠️ Tools and Utility Scripts (အထောက်အကူပြု Script များ)

ဤ `tools/` ဖိုဒါတွင် Project ၏ အဓိက လုပ်ငန်းဆောင်တာ (Core Functionality) မဟုတ်ဘဲ၊ Development၊ စီမံခန့်ခွဲမှုနှင့် ပြင်ဆင်မှုများအတွက် အသုံးပြုသည့် Utility Scripts များ ပါဝင်ပါသည်။ 

ဤ Scripts များကို အသုံးပြုခြင်းဖြင့် Project ၏ လုပ်ငန်းစဉ်များ (Workflow) ကို ပိုမိုမြန်ဆန် စနစ်ကျစေပြီး၊ အဓိက Source Code (modules/) များကို ရှုပ်ထွေးမှု လျှော့ချနိုင်မည် ဖြစ်သည်။

---

## ၁။ အဓိက ရည်ရွယ်ချက်များ (Purpose)

ဤဖိုဒါတွင် အောက်ပါ ရည်ရွယ်ချက်များအတွက် ရေးသားထားသော Scripts များကို ထားရှိပါသည်။

| အခန်းကဏ္ဍ | ဖော်ပြချက် | ဥပမာ Script အမျိုးအစား |
| :--- | :--- | :--- |
| **Data Preprocessing** | Core Logic Modules များအတွက် လိုအပ်သော Raw Data များကို စီမံပြင်ဆင်ခြင်း၊ သန့်စင်ခြင်းနှင့် Format ပြောင်းလဲခြင်း။ | `preprocess_lexicon.py`, `convert_ontology_to_db.py` |
| **Testing & Evaluation** | အဓိက Code တွင် မပါဝင်သော လက်တွေ့ စမ်းသပ်မှုများ (Proof of Concept) နှင့် စွမ်းဆောင်ရည် စစ်ဆေးမှုများ။ | `run_benchmark.py`, `NSTFPriceAdjuster.py` (လက်တွေ့စမ်းသပ်မှု) |
| **Configuration Management** | API Server များ (သို့) Environment များကို စီမံခန့်ခွဲရာတွင် အသုံးပြုသော Utility များ။ | `setup_env.sh`, `generate_api_keys.py` |
| **Deployment / Maintenance** | Application ကို စတင်ခြင်း၊ အဆင့်မြှင့်တင်ခြင်း သို့မဟုတ် အခြား System Maintenance များ။ | `start_server.sh`, `database_backup.py` |

---

## ၂။ ပါဝင်သော Scripts များ

### 🔹 `NSTFPriceAdjuster.py`

* **ရည်ရွယ်ချက်:** ဤ Script သည် **AI Ethics Engine (NALM/Balance-First Protocol)** ၏ စွမ်းဆောင်ရည်ကို လက်တွေ့ကျကျ စမ်းသပ်ရန်နှင့် အကဲဖြတ်ရန်အတွက် ရေးသားထားပါသည်။ ၎င်းသည် Core Logic ကို အသုံးပြု၍ သတ်မှတ်ထားသော စျေးနှုန်းညှိနှိုင်းမှု အခြေအနေတစ်ခုအား စစ်ဆေးတွက်ချက်မည် ဖြစ်သည်။
* **အသုံးပြုပုံ:** ဤ Script သည် Project ၏ အဓိကဝန်ဆောင်မှု မဟုတ်ဘဲ၊ Logic ကို သီးခြား စမ်းသပ်ရန် Utility အဖြစ် ဆောင်ရွက်ပါသည်။

---

## 💡 မှတ်ချက်

`tools/` ဖိုဒါရှိ Scripts များသည် Core Logic Modules များပေါ်တွင် မှီခိုနိုင်သော်လည်း၊ ၎င်းတို့ကိုယ်တိုင်သည် Core API ၏ အစိတ်အပိုင်းများအဖြစ် သတ်မှတ်ခြင်းမရှိပါ။ Core Logic ကို အသုံးပြုလိုပါက `modules/` ဖိုဒါရှိ သက်ဆိုင်ရာ Modules များကို Import လုပ်၍ အသုံးပြုနိုင်ပါသည်။
