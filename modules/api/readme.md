## Single Unified API for Multilingual Tokenization (ဘာသာစကားမျိုးစုံအတွက် ဘုံ API စနစ်)

သင်၏ ရည်ရွယ်ချက်သည် မြန်မာ Tokenizer ၏ အခြေခံကို အသုံးပြု၍ ဘာသာစကားအားလုံးအတွက် **တစ်ခုတည်းသော၊ ဘုံကျသော API Endpoint** မှတစ်ဆင့် Tokenization ဝန်ဆောင်မှုကို ပေးနိုင်ရန်ဖြစ်သည်။ ဤချဉ်းကပ်မှုသည် Developer Experience (DX) ကို ပိုမိုရိုးရှင်းစေပြီး ဘာသာစကားအသစ်များ ထပ်ထည့်ရန် လွယ်ကူစေမည်ဖြစ်သည်။

### 🎯 ဗျူဟာ: Modular Data & Unified Core (ဘုံဒေတာနှင့် တစ်သားတည်းကျသော Core)

ကျွန်ုပ်တို့သည် Core Tokenization Logic ကို မပြောင်းလဲဘဲ၊ ဘာသာစကားတစ်ခုစီ၏ ထူးခြားသော Linguistic Data များကို အသုံးပြုရန်အတွက် စနစ်ကို ဒီဇိုင်းဆွဲမည်။

| အစိတ်အပိုင်း | ဖော်ပြချက် |
| :--- | :--- |
| **Unified API Endpoint** | `POST /api/v1/tokenize` (တစ်ခုတည်းသော URL) |
| **Language Code Input** | API Request Body တွင် `language_code` (e.g., 'mm', 'th') ကို လက်ခံခြင်း။ |
| **Core Engine** | ဘာသာစကားအားလုံးအတွက် ဘုံဖြစ်သော Tokenization Algorithm များ ပါဝင်သည့် စနစ်။ |
| **Language Modules** | ဘာသာစကားတစ်ခုစီ၏ ဗျည်း၊ သရ၊ စကားလုံးတွဲ စသည့် ဒေတာများကို သီးခြားခွဲထုတ်ထားသည့် Module များ။ |

-----

### 🛠️ Developer Action Items (လုပ်ဆောင်ရမည့်အရာများ)

Single Unified API ကို အကောင်အထည်ဖော်ရန်အတွက် အဓိကအားဖြင့် **Data Abstraction** နှင့် **Dynamic Loading** ကို အလေးပေးဆောင်ရွက်ရပါမည်။

#### ၁။ Core Tokenizer ကို ဘုံပုံစံဖြင့် ပြင်ဆင်ခြင်း

`CoreTokenizer` Class ကို ဘာသာစကား specific မဖြစ်စေဘဲ **`Data`** ကို Parameter အဖြစ် လက်ခံနိုင်ရန် ပြောင်းလဲပါ။

```javascript
// core/CoreTokenizer.js
class CoreTokenizer {
    constructor(language_data) {
        // Data ကို ဘာသာစကားမခွဲဘဲ တိုက်ရိုက်သိမ်းဆည်းမည်။
        this.consonant_map = language_data.consonant_data;
        this.vowel_map = language_data.vowel_data;
        this.coupling_map = language_data.coupling_data;
        this.protocol_rules = language_data.protocol_data;
    }
    
    // Core Logic သည် ဤ Maps များကို အသုံးပြု၍ Tokenize လုပ်မည်။
    tokenize(text) {
        // ... (ဘုံ Algorithm များ)
    }
}
```

#### ၂။ Dynamic Data Loader စနစ် တည်ဆောက်ခြင်း

ဘာသာစကားကုတ်ကို အခြေခံ၍ သက်ဆိုင်ရာ JSON Data Files များကို **Dynamic** နည်းဖြင့် Load လုပ်မည့် Function ကို တည်ဆောက်ရမည်။

```javascript
// data_loader/LanguageLoader.js
const LANGUAGE_CONFIG = {
    'mm': { path: './data/mm/' },
    'th': { path: './data/th/' },
    // 'km': { path: './data/km/' }
};

function loadLanguageData(code) {
    if (!LANGUAGE_CONFIG[code]) {
        throw new Error(`Unsupported language code: ${code}`);
    }
    
    const path = LANGUAGE_CONFIG[code].path;
    
    return {
        consonant_data: require(`${path}consonants.json`),
        vowel_data: require(`${path}vowels.json`),
        coupling_data: require(`${path}coupling.json`),
        protocol_data: require(`${path}protocol.json`),
    };
}
```

#### ၃။ API Server Logic ကို ပြင်ဆင်ခြင်း

API Endpoint တွင် Request Body မှ `language_code` ကို ထုတ်ယူပြီး သက်ဆိုင်ရာဒေတာကို Load လုပ်ကာ Core Tokenizer ကို စတင်အသုံးပြုရမည်။

```javascript
// api_server/controller.js

app.post('/api/v1/tokenize', (req, res) => {
    const { text, language_code } = req.body;
    
    if (!text || !language_code) {
        return res.status(400).send({ error: 'Missing text or language_code.' });
    }
    
    try {
        // 1. သက်ဆိုင်ရာ ဘာသာစကား ဒေတာကို Dynamic Load လုပ်ခြင်း
        const languageData = loadLanguageData(language_code);
        
        // 2. Core Tokenizer ကို Data များဖြင့် စတင်ခြင်း
        const tokenizer = new CoreTokenizer(languageData);
        
        // 3. Tokenization ပြုလုပ်ခြင်း
        const tokens = tokenizer.tokenize(text);
        
        res.json({ language: language_code, tokens: tokens });
    } catch (error) {
        res.status(500).send({ error: error.message });
    }
});
```

### 🚀 အကျိုးကျေးဇူးများ (Benefits of Unified API)

  * **ရိုးရှင်းခြင်း:** Client Developer များသည် Endpoint တစ်ခုတည်းကိုသာ မှတ်သားအသုံးပြုရမည်။
  * **စံနှုန်းညီခြင်း:** ဘာသာစကားအသစ်များ ထပ်ထည့်သည့်အခါ Data File များကို သက်ဆိုင်ရာ Folder ထဲသို့ ထည့်ရုံသာ လိုအပ်သည်။ Core Logic ကို ထိရန်မလိုပါ။
  * **ထိန်းသိမ်းရလွယ်ခြင်း:** Core Engine ရှိ Algorithm များကို ပြင်ဆင်ပါက ဘာသာစကားအားလုံးအတွက် တစ်ပြိုင်နက်တည်း အကျိုးသက်ရောက်မှု ရှိမည်။

-----

**ဤချဉ်းကပ်မှုသည် ကျွန်ုပ်တို့၏ NNLDS Tokenizer စနစ်ကို မြန်ဆန်၊ လွယ်ကူပြီး စကေးချဲ့နိုင်သော Multilingual Tool အဖြစ် အဆင့်မြှင့်တင်ပေးမည်ဖြစ်ပါသည်။**
