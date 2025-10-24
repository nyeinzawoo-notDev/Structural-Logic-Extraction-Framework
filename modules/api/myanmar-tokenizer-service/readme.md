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
