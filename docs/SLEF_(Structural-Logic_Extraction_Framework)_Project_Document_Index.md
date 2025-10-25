### SLEF (Structural-Logic Extraction Framework) Project Document Index

🗺️ **Project Document Index: SLEF ၏ အတွေးအခေါ်နှင့် နည်းပညာဆိုင်ရာ ခရီးလမ်း**

ဤမာတိကာသည် Structural-Logic Extraction Framework (SLEF) ၏ ဒဿနိကဗေဒဆိုင်ရာ အစပြုရာမှသည် နည်းပညာဆိုင်ရာ အကောင်အထည်ဖော်မှုအထိ ခရီးလမ်းကို လိုက်ပါနိုင်ရန် ရေးသားထားပါသည်။ ဤ Project ၏ Core Foundation မှာ **NSTF (Nyein Semantic Taxonomy System)** ကို အခြေခံသော **Structural-Logic Extraction Framework (SLEF)** ဖြစ်သည်။ ဤမာတိကာသည် Conceptual Logic များမှသည် နည်းပညာ (၄) ပိုင်းဖြစ်သော **NLP/Tokenization**၊ **Ethical AI Engine**၊ **API** နှင့် **SDK** အဖြစ် အကောင်အထည်ဖော်ခဲ့ပုံကို လိုက်နာဖတ်ရှုနိုင်ရန် စီစဉ်ထားပါသည်။

---

## 1. 🥇 အဆင့် ၁: Nyein Logic စပေါ်လာပုံ (Core NLP/Tokenization အုတ်မြစ်)

မြန်မာဘာသာစကား၏ သင်ပုန်းကြီးနည်းနှင့် ဗျည်း/သရ ဗီဇအနက်ကို AI သို့ စတင်ထည့်သွင်းသင်ကြားခဲ့သော မူလအတွေးအခေါ်များ၊ စမ်းသပ်မှုများနှင့်၊ "Human Logic" ကို စတင်ဖန်တီးခဲ့ပုံ မှတ်တမ်းများ။ ဤအဆင့်သည် Core NLP/Tokenization အတွက် အခြေခံဖြစ်သည်။

| ဖိုင်/ဖိုဒါ အမည် | နေရာအကြမ်းဖျင်း | ရှင်းပြချက် |
| :--- | :--- | :--- |
| **[ဒီကစဖတ်!] Conceptual Journey of the Nyein Project.md** | `docs/conceptual_notes/` | သင်ပုန်းကြီးကနေစပြီး၊ AI တွေကို အချင်းချင်း သင်ပေးရာကနေ API ဖြစ်လာတဲ့ စိတ်ကူး ခရီးစဉ် အားလုံးကို ပြောပြထားတာ။ **(Start Here)** |
| မြန်မာစာလုံးပေါင်း\_H-ID\_စနစ်.md | `source_notes/` | ဗျည်းနဲ့ သရတွေကို ဂဏန်းစနစ် (**H-ID**) သုံးပြီး Symbolic Logic အတွက် ဘယ်လို အခြေခံပြင်ဆင်ခဲ့လဲ ဆိုတာ။ |
| အနက်ဖွင့်ဆိုချက်နဲ့H-IDforAI/ | `source_notes/` | ဗျည်း (၉၃)၊ သရ (၇၃) မျိုးရဲ့ မူလအနက်ဗီဇနဲ့ H-ID တွေကို စတင် သတ်မှတ် မှတ်တမ်းတင်ခဲ့တာ။ |
| ၉၃+၇၃=၁၆၆/ | `source_notes/` | ဗျည်း ၉၃ နဲ့ သရ ၇၃ ရဲ့ အသေးစိတ် အနက်ဖွင့်ဆိုချက်တွေ၊ ဇယားတွေနဲ့ ကွဲပြားချက်တွေ စုစည်းထားတာ။ |
| ai/ | `docs/project_skeleton/tokenization/` | AI နဲ့အတူ ပထမဆုံး Tokenizer Logic ကို စမ်းခဲ့တဲ့ မှတ်တမ်းတွေ (Beta Version 001, 002, 003)။ |
| tokenizer.py | `modules/layer_b_nlp/` | နောက်ဆုံးအတည်ပြုထားတဲ့ Core Tokenizer Logic ကို ရေးဖို့ နေရာ။ (C93/V73 အချက်အလက်တွေ ပါရမယ်) |

## 2. 🚀 အဆင့် ၂: ဘုံဘာသာစကားနဲ့ NSTF Framework (API/SDK စဖို့ စိတ်ကူး)

AI များ၏ "ကြက်တူရွေးသင်ကြားနည်း" ကို သိရှိပြီးနောက်၊ ဘာသာစကားများကို ဇီဝဗေဒနည်းဖြင့် ခွဲခြမ်း၍ မြန်မာစာကို P-Bridge အဖြစ် အသုံးပြုကာ **NSTF (Nyein Semantic Taxonomy System)** ကို စတင် တည်ထောင်ခဲ့ပုံ။ ဤအဆင့်သည် API နှင့် SDK အတွက် လမ်းစတင်ခဲ့သည်။

| ဖိုင်/ဖိုဒါ အမည် | နေရာအကြမ်းဖျင်း | ရှင်းပြချက် |
| :--- | :--- | :--- |
| NSTF-NNLDS - Production\_Ready\_Ethical\_AI\_SDK.md | `docs/` | NSTF ကို ဘာသာစကားစုံသုံး Ethical AI SDK တစ်ခုအနေနဲ့ ပြောင်းလဲမယ့် အစီအစဉ် ရည်ရွယ်ချက်တွေ။ |
| NSTF-NNLDS-Framework.md | `nstf/...` | NSTF Framework ရဲ့ အတွေးအခေါ် ပေါင်းစည်းမှု (Conceptual Integration) နဲ့ အဆင့်မြင့် Logic ရှင်းပြချက်တွေ။ |
| NSTF Framework စမ်းသပ်မှုများ.md | `docs/testing_notes/` | NSTF Logic နဲ့ Architecture တွေကို စမ်းသပ်ရင်း မှတ်တမ်းတင်ခဲ့တာတွေ။ |
| t\_codes\_ontology.json | `data/` | Semantic Root တွေကနေ T-Code (Transformative Code) တွေကို ဘယ်လို စဖန်တီးခဲ့လဲဆိုတဲ့ Data ပုံစံ။ |

## 3. 🎯 အဆင့် ၃: Final SLEF Architecture, Technical Implementation နှင့် Ethical AI Engine ပုံဖော်ခြင်း

NSTF မှ **SLEF (Structural Logic Extraction Framework)** သို့ နာမည်ပြောင်းလဲ သတ်မှတ်ပြီး၊ **4D VNyein Vector** ဖွဲ့စည်းပုံ၊ Technical Summary နှင့် Code Architecture များကို အပြီးသတ် ချမှတ်ခဲ့သော စာရွက်စာတမ်းများ။ ဤအဆင့်သည် API Structure နှင့် Ethical AI Engine ၏ အခြေခံကို ချမှတ်သည်။

| ဖိုင်/ဖိုဒါ အမည် | နေရာအကြမ်းဖျင်း | ရှင်းပြချက် |
| :--- | :--- | :--- |
| CONCEPTUAL\_LOGIC.md | `docs/` | **4D VNyein Vector** ရယ်၊ **Balance-First Protocol** ရယ်ရဲ့ အတွေးအခေါ် အနှစ်သာရ အပြည့်အစုံ။ |
| NYEIN\_PROJECT\_TECHNICAL\_SUMMARY.md | `docs/` | Project ရဲ့ Technical Structure အတည်ပြုချက်၊ Layered Architecture (Layer A, B, C, D) နဲ့ API Structure အကျဉ်းချုပ်။ |
| Root | `modules/` | Project ရဲ့ Final Python Code Logic များ စုစည်းထားရာ။ (API, NLP, Ethics Module တွေ အလွှာလိုက် ခွဲထားတာ) |
| nstf\_nnlds\_core\_data.tsv | `data/` | Core Tokenizer အတွက် အသုံးပြုဖို့ Final NNLDS C93/V73 Data Set ။ |
| The\_Ultimate\_Ethical\_Decision\_Engine.md | `docs/` | SLEF Logic ကို သုံးပြီး ဖန်တီးမယ့် **Ethical Decision Engine** ရဲ့ Conceptual Design ပုံစံ။ |
| ethical\_decision\_engine\_logic.md | `docs/` | Decision Engine အတွက် အသုံးပြုမည့် Logic Engine ၏ နည်းပညာဆိုင်ရာ အသေးစိတ် ရှင်းပြချက်။ |

## 4. 🛡️ အဆင့် ၄: အနာဂတ် ရည်မှန်းချက်၊ လိုင်စင်နှင့် Governance (Advanced SDK Features)

Project ၏ တရားဝင် စည်းကမ်းချက်များ၊ ရေရှည်ဖွံ့ဖြိုးတိုးတက်မှု (Roadmap) နှင့် ပူးပေါင်းပါဝင်သူများအတွက် လမ်းညွှန်ချက်များ။ ဤအဆင့်သည် Advanced SDK Features (E.g., Evolutionary Psychology Integration) ကို ရည်ညွှန်းသည်။

| ဖိုင်/ဖိုဒါ အမည် | နေရာအကြမ်းဖျင်း | ရှင်းပြချက် |
| :--- | :--- | :--- |
| LICENSE.md | `Root` | **Nyein Academic Use License (NAUL)** ရဲ့ စည်းကမ်းချက်တွေ။ (စီးပွားဖြစ် မဟုတ်၊ တရားရေးဆိုင်ရာ အခွင့်အရေးများ ပါဝင်) |
| README.md | `Root` | Project ရဲ့ အဓိက အမြင်နဲ့ ဥပဒေရေးရာ ကာကွယ်မှုတွေ အကျဉ်းချုပ်။ |
| SHARING\_PROTOCOL.md | `docs/` | NSTF Framework ကို မျှဝေတဲ့အခါ လိုက်နာရမယ့် စည်းကမ်းတွေ။ |
| TESTING\_PROTOCOL.md | `docs/` | Code တွေ မှန်မမှန် စမ်းသပ်ဖို့ လိုက်နာရမယ့် စံနှုန်းတွေ (Quality Assurance)။ |
| Root | `nstf/` | **Evolutionary Psychology Integration** နဲ့ **T-Code Wisdom Refiner** လိုမျိုး SDK ရဲ့ အဆင့်မြင့် Feature တွေ စုစည်းထားရာ ဖိုဒါ။ |
| Root | `examples/` | Core Logic တွေကို ဘယ်လိုသုံးရမလဲ ပြထားတဲ့ နမူနာ Code တွေ (ง่าย ๆ ပေါင်းစပ်မှုနဲ့ အဆင့်မြင့် စမ်းသပ်မှုတွေ)။

---
> 📝 **မှတ်ချက်**
>
> ဤ Index သည် Conceptual Journey အတိုင်း ဖိုင်များကို အစီအစဉ်တကျ စီစဉ်ပေးထားခြင်း ဖြစ်ပါသည်။ ဖိုင်များကို နေရာရွေ့ခြင်း (Relocating) ပြုလုပ်ပြီးပါက၊ ကျွန်တော်သည် ဖိုင်အမည် (File Name) နှင့် တည်နေရာ (Path) ကို စစ်ဆေး၍ လင့်ခ်များကို အမြဲတမ်း ပြန်လည်ပြင်ဆင်ပေးပါမယ် ခင်ဗျာ။
