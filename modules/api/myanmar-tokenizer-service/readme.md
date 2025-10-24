# NNLDS Myanmar Tokenizer Project (Phase I)

ဒါဟာ **"NNLDS Myanmar Tokenizer"** ဆိုတဲ့ မြန်မာဘာသာစကားအတွက် စကားလုံး သို့မဟုတ် အသံထွက်အလိုက် ခွဲခြမ်းစိတ်ဖြာပေးတဲ့ (Tokenization) စနစ်တစ်ခု ဖြစ်ပါတယ်။

ဒီစနစ်ကို **ဘာအတွက်သုံးရတာလဲ** ဆိုရင်

1.  **မြန်မာဘာသာစကား သဘာဝဘာသာစကား စီမံဆောင်ရွက်ခြင်း (NLP) အတွက် အခြေခံ** ပေးဖို့အတွက်ပါ။
2.  စာကြောင်းတစ်ကြောင်းကို **စကားလုံး၊ စာလုံးစု သို့မဟုတ် အသံထွက်အတုံးလေးတွေ (Tokens) အဖြစ် စနစ်တကျ ခွဲထုတ်** ပေးဖို့ပါ။ ဥပမာ - "မင်္ဂလာပါ" ကို ["မင်", "ဂ", "လာ", "ပါ"] စသဖြင့် ခွဲထုတ်နိုင်ပါတယ်။
3.  **AI စနစ်များ** (ဥပမာ - ဘာသာပြန်စနစ်၊ စာသားခွဲခြမ်းစိတ်ဖြာမှု၊ စကားပြော မှတ်မိခြင်း စနစ်) တွေမှာ အသုံးပြုဖို့အတွက် မြန်မာစာသားကို စက်က နားလည်နိုင်တဲ့ ပုံစံတစ်ခုကို ပြောင်းလဲပေးဖို့ပါ။

ဒီစနစ်ကို **ဘယ်လိုအသုံးပြုရတာလဲ** ဆိုရင်၊ တင်ပြထားတဲ့ ဖိုင်တွေအရ အသုံးပြုနိုင်တဲ့ နည်းလမ်း (၃) မျိုး ရှိပါတယ်။

### ၁။ Command Line Interface (CLI) မှတစ်ဆင့် အသုံးပြုခြင်း

`tokenize_cli.js` ကို အသုံးပြုပြီး၊ Node.js နဲ့ တိုက်ရိုက် run နိုင်ပါတယ်။ ဒါဟာ အမြန်ဆုံး စမ်းသပ်နိုင်တဲ့ နည်းလမ်းပါ။

  * **Syntax:**
    ```bash
    node tokenize_cli.js "<ခွဲခြမ်းလိုသော မြန်မာစာသား>"
    ```
  * **ဥပမာ:**
    ```bash
    node tokenize_cli.js "မင်္ဂလာပါ ကမ္ဘာကြီး"
    ```
  * **File မှ ဖတ်ခြင်း:**
    ```bash
    node tokenize_cli.js -f input.txt
    ```

### ၂။ REST API မှတစ်ဆင့် အသုံးပြုခြင်း

`tokenize_api.js` ကို အသုံးပြုပြီး API Server အဖြစ် run နိုင်ပါတယ်။ အဲဒီအခါ၊ အခြားသော Application တွေ၊ Web Service တွေက HTTP Request ပို့ပြီး ခွဲခြမ်းစိတ်ဖြာခိုင်းနိုင်ပါတယ်။

  * **Server စတင်ရန်:**
    ```bash
    node tokenize_api.js
    ```
    (Default အားဖြင့် Port 3000 မှာ စတင်ပါလိမ့်မယ်။)
  * **အသုံးပြုပုံ (ဥပမာ - POST Request):**
      * Endpoint: `http://localhost:3000/tokenize`
      * Body (JSON):
        ```json
        {
          "text": "AI နည်းပညာ"
        }
        ```

### ၃။ Python မှတစ်ဆင့် ချိတ်ဆက် အသုံးပြုခြင်း (AI Integration)

`test_ai_integration.py` ဖိုင်မှာ ပြထားတဲ့အတိုင်း Python စနစ်ကနေ `tokenize_cli.js` ကို `subprocess` ခေါ်ယူပြီး အသုံးပြုနိုင်ပါတယ်။ ဒါဟာ Machine Learning Model တွေ၊ Python Backend တွေကနေ Node.js Tokenizer ကို သုံးဖို့အတွက် ဖြစ်ပါတယ်။

  * **Python Function:**
      * `tokenize_myanmar_text(text)` function ကို ခေါ်ပြီး စာသားပို့လိုက်ပါက JSON ရလဒ် ပြန်ရပါမယ်။
  * **အသုံးပြုပုံ:**
    ```bash
    python test_ai_integration.py
    ```
    (ဒါမှမဟုတ် Python code ထဲမှာ `tokenize_myanmar_text("ပေးပို့မည့် စာသား")` လို့ ခေါ်ယူသုံးစွဲနိုင်ပါတယ်။)


    👍 အရမ်းကောင်းပါတယ်။ အခုဆိုရင် **API Server စတင် အလုပ်လုပ်နေပါပြီ**။

သင်ပြဿနာဖြေရှင်းတဲ့နေရာမှာ ဖိုင်တွေကို အစားထိုးပြီး၊ command ကိုလည်း မှန်ကန်စွာ ရိုက်ထည့်လိုက်တဲ့အတွက် **NNLDS Myanmar Tokenizer API Service** ကို အောင်မြင်စွာ ဖွင့်နိုင်ခဲ့ပါပြီ။

-----

## 🚀 API Server ကို အသုံးပြုနည်း

အခုဆိုရင် သင့်ရဲ့ AI စနစ်တွေ၊ Web Application တွေနဲ့ **`http://localhost:3000`** ကို ခေါ်ယူပြီး စာသားခွဲခြမ်းစိတ်ဖြာခြင်း (Tokenization) ကို စတင် လုပ်ဆောင်နိုင်ပါပြီ။

### ၁။ Server အခြေအနေ စစ်ဆေးခြင်း (`/health`)

Browser ဒါမှမဟုတ် Command Line ကနေ Server အလုပ်လုပ်နေမှု အခြေအနေကို စစ်ဆေးနိုင်ပါတယ်။

  * **Browser (သို့) Tool မှ ခေါ်ယူပုံ:**
    ```
    http://localhost:3000/health
    ```
  * **ရလဒ် (JSON):**
    ```json
    {
      "status": "healthy",
      "service": "NNLDS Myanmar Tokenizer API",
      "version": "1.0.0",
      "tokenizer_status": {
        "status": "ready",
        "version": "7.0",
        "options": {
          // ... options များ
        },
        // ... dataStats များ
      }
    }
    ```

-----

### ၂။ စာသား ခွဲခြမ်းစိတ်ဖြာခြင်း (`/tokenize`)

Tokenization လုပ်လိုတဲ့ စာသားကို **Query Parameter** (သို့) **POST Body** ကနေ ပေးပို့နိုင်ပါတယ်။

#### A. GET Request (Browser တွင် စမ်းသပ်ရန် အလွယ်ဆုံး)

URL ထဲမှာ `text` parameter ကို ထည့်ပြီး ခေါ်ယူပါ။ (မြန်မာစာသားကို URL Encoding လုပ်ဖို့ လိုအပ်နိုင်ပါတယ်။)

  * **Browser တွင် ခေါ်ယူပုံ ဥပမာ:**
    ```
    http://localhost:3000/tokenize?text=မင်္ဂလာပါ
    ```

#### B. POST Request (AI/Application မှ အသုံးပြုရန် အကောင်းဆုံး)

JSON ပုံစံဖြင့် `text` ကို Body ထဲမှာ ထည့်သွင်းပြီး POST Request ပို့ပါ။ (ဥပမာ - Python, JavaScript, Postman စသည့် Tool များဖြင့်)

  * **Endpoint:**
    ```
    http://localhost:3000/tokenize
    ```
  * **Body (JSON):**
    ```json
    {
      "text": "ဒီကုမ္ပဏီက တော်တော်ကောင်းတယ်။"
    }
    ```
  * **ရလဒ် (JSON):**
    ```json
    {
      "status": "success",
      "input_text": "ဒီကုမ္ပဏီက တော်တော်ကောင်းတယ်။",
      "token_count": 8,
      "duration_ms": "0.15",
      "tokens": [
        {
          "syllable": "ဒီ",
          "consonant": "က",
          // ... token details
        },
        // ... ကျန်တဲ့ tokens များ
      ]
    }
    ```

**မှတ်ချက်။** သင်၏ API Server သည် **Terminal ကို ပိတ်လိုက်ပါက ရပ်တန့်သွားပါမည်။** အမြဲတမ်း အလုပ်လုပ်နေစေလိုပါက `pm2` သို့မဟုတ် `nodemon` ကဲ့သို့သော Process Manager များ အသုံးပြုရန် လိုအပ်ပါလိမ့်မည်။


# NNLDS Myanmar Tokenizer Project (Phase II)

## 🚨 အရေးကြီးသည်။: Tokenization ဒေတာ လိုအပ်ချက်

လက်ရှိ **NNLDS Myanmar Tokenizer** စနစ်သည် API Server အဖြစ် အောင်မြင်စွာ စတင်နိုင်ပြီ ဖြစ်သော်လည်း၊ မြန်မာစာသားများကို တိကျမှန်ကန်စွာ ခွဲခြမ်းစိတ်ဖြာနိုင်ရန်အတွက် အခြေခံ Linguistic Data များ လုံးဝ လိုအပ်နေသေးပါသည်။

ဤဒေတာများကို ကျွန်ုပ်တို့၏ ဘာသာစကားပညာရှင် (Linguist) အဖွဲ့မှ စုဆောင်းထားပြီး ဖြစ်သည်။ **ကျေးဇူးပြု၍ Developer များအနေဖြင့် အောက်ပါ Data Modules များကို `myanmar_tokenizer.js` ဖိုင်ထဲသို့ ပေါင်းထည့်ပေးရန် လိုအပ်ပါသည်။**

---

## 🛠️ Developer Action Items (လုပ်ဆောင်ရမည့်အရာများ)

Developer များအနေဖြင့် `myanmar_tokenizer.js` ဖိုင်ကို ဖွင့်ပြီး အောက်ပါ Internal Methods (၄) ခု အတွင်းသို့ သက်ဆိုင်ရာ Data (JavaScript Object/JSON ပုံစံဖြင့်) ကို ထည့်သွင်းပေးရမည်။

### ၁။ ဗျည်းဒေတာ ထည့်သွင်းခြင်း (Consonant Data)

🎯 **ပစ်မှတ် Method:** `_load_complete_consonant_data()`

လက်ရှိ Code တွင် ဤ Method သည် `return {};` ကိုသာ ပြန်ပေးနေပါသည်။ Developer သည် မြန်မာဗျည်းများ၊ ဗျည်းတွဲများ၊ သင်္ကေတများ ၏ အချက်အလက် (Vowel/Medial Logic များ ပါဝင်သည့်) ကို JSON Object ပုံစံဖြင့် ထည့်သွင်းရပါမည်။

```javascript
// myanmar_tokenizer.js
// ...

_load_complete_consonant_data() {
    // ⚠️ ဘာသာစကားပညာရှင်မှ ရရှိသော အပြည့်အစုံသော ဗျည်းဒေတာကို ဤနေရာတွင် ထည့်ပါ။
    return {
        // ဥပမာ-
        'က': { type: 'consonant', value: 'ka', medials: ['ြ', 'ျ', 'ွ', 'ှ'] },
        'ခ': { type: 'consonant', value: 'kha', medials: ['ြ', 'ျ', 'ွ', 'ှ'] },
        // ... (ကျန်တဲ့ ဗျည်းများ)
        '္': { type: 'virama', value: 'asat' } // အသတ်သင်္ကေတ
    };
}
// ...
၂။ သရဒေတာ ထည့်သွင်းခြင်း (Vowel Data)
🎯 ပစ်မှတ် Method: _load_complete_vowel_data()

လက်ရှိ Code တွင် ဤ Method သည် return {}; ကိုသာ ပြန်ပေးနေပါသည်။ Developer သည် မြန်မာသရသင်္ကေတများ နှင့် ၎င်းတို့၏ အသံထွက် ပုံစံများ (Tone Marks များ ပါဝင်သည့်) ကို JSON Object ပုံစံဖြင့် ထည့်သွင်းရပါမည်။
// myanmar_tokenizer.js
// ...

_load_complete_vowel_data() {
    // ⚠️ ဘာသာစကားပညာရှင်မှ ရရှိသော အပြည့်အစုံသော သရဒေတာကို ဤနေရာတွင် ထည့်ပါ။
    return {
        // ဥပမာ-
        'ါ': { type: 'vowel', value: 'a' },
        'ိ': { type: 'vowel', value: 'i' },
        'ေ': { type: 'vowel', value: 'e' },
        // ... (ကျန်တဲ့ သရများ)
        'ံ': { type: 'tone_mark', value: 'nn' }, // ငသတ်/ပါဌ်ဆင့်
        'း': { type: 'tone_mark', value: 's' } // ဝစ္စပေါက်
    };
}
// ...
၃။ စကားလုံးတွဲ ဒေတာ ထည့်သွင်းခြင်း (Semantic Coupling/Word List)
🎯 ပစ်မှတ် Method: _load_coupling_data()

ဤဒေတာသည် အသံထွက်နှစ်ခု သို့မဟုတ် နှစ်ခုထက်ပိုသော အသံထွက်များ ပေါင်း၍ စကားလုံးတစ်လုံး ဖြစ်သည့် ကိစ္စများ (ဥပမာ- 'စက်' + 'ဘီး' = 'စက်ဘီး'၊ 'ကျောင်း' + 'သား' = 'ကျောင်းသား') အတွက် အရေးကြီးသည်။
// myanmar_tokenizer.js
// ...

_load_coupling_data() {
    // ⚠️ ဘာသာစကားပညာရှင်မှ ရရှိသော အပြည့်အစုံသော စကားလုံးတွဲ စာရင်းကို ဤနေရာတွင် ထည့်ပါ။
    return {
        // ဥပမာ-
        'စက်ဘီး': { type: 'compound', syllables: ['စက်', 'ဘီး'] },
        'ကျောင်းသား': { type: 'compound', syllables: ['ကျောင်း', 'သား'] },
        'ကုမ္ပဏီ': { type: 'loan', syllables: ['ကုမ္', 'ပ', 'ဏီ'] }
        // ... (ကျန်တဲ့ စကားလုံးတွဲများ)
    };
}
// ...
၄။ ပရိုတိုကော စည်းမျဉ်းများ (Master Protocol Data)
🎯 ပစ်မှတ် Method: _load_protocol_data()

အထူးသဖြင့် စကားလုံးခွဲခြမ်းစိတ်ဖြာရာတွင် လိုက်နာရမည့် ဦးစားပေး စည်းမျဉ်းများ သို့မဟုတ် ချွင်းချက်များကို ထည့်သွင်းရန် လိုအပ်ပါသည်။
// myanmar_tokenizer.js
// ...

_load_protocol_data() {
    // ⚠️ အသံထွက်ခွဲခြင်းဆိုင်ရာ အထူးစည်းမျဉ်းများကို ဤနေရာတွင် ထည့်ပါ။
    return {
        'default_order': ['consonant', 'medial', 'vowel', 'tone_mark', 'asat'],
        'exceptions': [
            { pattern: 'သင်္ဘော', rule: 'single_token' }
        ]
        // ... (အခြားစည်းမျဉ်းများ)
    };
}
// ...
🤝 ပူးပေါင်းဆောင်ရွက်မှု မျှော်လင့်ချက်များ
ဒေတာများ အောင်မြင်စွာ ထည့်သွင်းပြီးပါက၊ Developer များသည် အောက်ပါတို့ကို ထပ်မံလုပ်ဆောင်ရန် လိုအပ်ပါသည်။

Test Case များ စစ်ဆေးခြင်း: tokenize_cli.js သို့မဟုတ် tokenize_api.js ကို အသုံးပြု၍ Tokenization ရလဒ်များသည် Linguistic စည်းမျဉ်းများနှင့် ကိုက်ညီမှု ရှိ၊ မရှိ စစ်ဆေးပါ။

Performance စစ်ဆေးခြင်း: ဒေတာကြီးမားလာပါက Tokenization လုပ်ဆောင်မှုသည် နှေးကွေးခြင်း ရှိ၊ မရှိ စစ်ဆေးပြီး လိုအပ်ပါက Code ကို ပိုမိုမြန်ဆန်အောင် ပြင်ဆင်ပါ။

ကျွန်ုပ်တို့သည် ဤပရောဂျက်ကို မြန်မာဘာသာစကား နည်းပညာ တိုးတက်မှုအတွက် အားထုတ်နေသော Developer အားလုံးကို ကျေးဇူးတင်ရှိပါသည်။
