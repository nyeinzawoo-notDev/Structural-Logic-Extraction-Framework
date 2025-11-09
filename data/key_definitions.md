# 📚 Data Set Key Definitions

## 📂 Data Set Key Definitions (CSV Files)

အောက်ပါ Key Definitions နှစ်ခုသည် `consonant_keys.csv` နှင့် `vowel_keys.csv` ဖိုင်များတွင် တိုက်ရိုက်အသုံးပြုရန် သင့်လျော်သော ပုံစံဖြစ်ပါသည်။

### ၁။ ဗျည်း Key Definitions (`consonant_keys.csv`)

| Column Name | Data Type | ဖော်ပြချက် (Description) | Remarks |
| :--- | :--- | :--- | :--- |
| **`C_ID`** | String | ဗျည်း၏ အမှတ်စဉ် (Consonant ID: C01, C02w, C70, C93w...) | **Primary Key** |
| **`Consonant`** | String | မြန်မာဗျည်း (Grapheme) ("က", "ခွ", "ကျွ") | |
| **`Type`** | String | ဗျည်းအမျိုးအစား (ရှေးရိုးဗျည်း၊ NNLDS ဗျည်း၊ ဗျည်းတွဲ) | Consonant Classification |
| **`H_ID`** | String | Hierarchical ID: `Base.T M 70.30` သို့မဟုတ် `01.11` | |
| **`Base_Unicode`** | String | ဗျည်း၏ ယူနီကုဒ် (Base Grapheme Code Points) | ယူနီကုဒ်များကို Space ခြားထားသည် |
| **`Freq_Rank`** | Integer/Float | အသုံးပြုမှု အကြိမ်ရေ အဆင့် (Higher Rank = Lower Frequency) | မြန်မာစာလုံးပေါင်း အသုံးပြုမှုအပေါ် အခြေခံသည် |
| **`P_Val`** | Float | အသံထွက်တန်ဖိုး (Phonetic Value) | စနစ်အတွင်း အသံထွက် ခြားနားမှုအတွက် သတ်မှတ်တန်ဖိုး |
| **`C_Score`** | Integer | ရှုပ်ထွေးမှု အမှတ် (Complexity Score) | ပုံသဏ္ဌာန် သို့မဟုတ် အသံထွက် ပေါင်းစပ်မှု ရှုပ်ထွေးခြင်း |
| **`S_Den`** | Integer | အဓိပ္ပာယ်သိပ်သည်းဆ (Semantic Density) | ဗျည်း၏ အဓိပ္ပာယ် ယူနိုင်စွမ်း/အခြေခံတန်ဖိုး (1, 2, or 3) |
| **`G_Type`** | Integer | စာလုံးအမျိုးအစား (Grapheme Type: 1-Base, 2-NNLDS, 3-Compound, 4-Compound with Medial) | `H_ID` ၏ Type Code (T) နှင့် ကိုက်ညီသည် |
| **`M_Code`** | Integer | ဝဆွဲပါဝင်မှု ကုတ် (Medial Code: 0=မပါဝင်, 1=ပါဝင်) | `H_ID` ၏ Medial Code (M) နှင့် ကိုက်ညီသည် |

-----

### ၂။ သရ Key Definitions (`vowel_keys.csv`)

| Column Name | Data Type | ဖော်ပြချက် (Description) | Remarks |
| :--- | :--- | :--- | :--- |
| **`V_ID`** | Integer | သရ၏ အမှတ်စဉ် (Vowel ID: V01 to V73) | **Primary Key** |
| **`Vowel_Type`** | String | သရအမျိုးအစား (အခြေခံသရ၊ သံရှည်သရ၊ သံတိုသရ၊ ဒွိသရ) | Vowel Classification |
| **`Example`** | String | ဗျည်းသရတွဲပုံ နမူနာ ("အ" ကို အသုံးပြုထားသည်) | "အ", "အီ့", "အား" |
| **`H_ID_Syllable`** | String | သရ၏ Hierarchical ID | `Base.T M - X X X . V` |
| **`Semantic_Category`** | String | သရ၏ အဓိပ္ပာယ်ဖွင့်ဆိုမှု အပိုင်းအခြား | VS01-VS15 အုပ်စုများနှင့် ဆက်စပ်သည် |
| **`S_ID`** | String | Semantic Group ID | VS01, VS02, ... |
| **`Freq_Rank`** | Float | အသုံးပြုမှု အကြိမ်ရေ အဆင့် | Lower value = More frequent |
| **`S_Den`** | Float | အဓိပ္ပာယ်သိပ်သည်းဆ (Semantic Density) | သရ၏ အခြေခံအဓိပ္ပာယ် ခိုင်မာမှု |
| **`IPA`** | String | နိုင်ငံတကာ အသံထွက် သင်္ကေတ | /a/, /eɪ/, /ɔ:./ |
| **`X_Code`** | Integer | အပိတ် သင်္ကေတ (်,့,း) | 0, 1, 2, 10, 11 စသည် |
| **`C_Score`** | Integer | ရှုပ်ထွေးမှု အမှတ် (Tone/Length/Diphthong ၏ ရှုပ်ထွေးမှု) | 0 မှ 3 အထိ |
| **`Tone`** | Integer | သရ၏ အသံနေအသံထား | 0=သံပြေ, 1=သံသေ, 2=သံရှည်, 3=သံတို |
| **`L_Code`** | Integer | သရအရှည်ကုတ် (Length Code: 0=တို, 1=ရှည်) | |
| **`D_Code`** | Integer | ဒွိသရကုတ် (Diphthong Code: 0=မပါ, 1=ပါ) | |
| **`SC_Effect`** | Integer | Semantic Category Effect | သံရှည်/နှာခေါင်းပေါက်သံ များတွင် အသုံးပြုရန် |
| **`Unicode_Markup`** | String | ဗျည်းနှင့်တွဲသော သရသင်္ကေတ ယူနီကုဒ်များ | ဥပမာ: U+102B U+1038 |

-----

## 🛠️ GitHub CSV File Structure (Sample Content)

သင်၏ GitHub repository တွင် အောက်ပါအတိုင်း ဖိုင်နှစ်ခုကို ဖန်တီးပြီး၊ ၎င်းတို့၏ ပါဝင်မှုအဖြစ် အထက်ပါ Column Name များနှင့် ဒေတာအချို့ကို ထည့်သွင်းနိုင်သည်။

### ၁။ `consonant_keys.csv` (Sample Content)

```csv
C_ID,Consonant,Type,H_ID,Base_Unicode,Freq_Rank,P_Val,C_Score,S_Den,G_Type,M_Code
C01,က,ရှေးရိုးဗျည်း,01.10,U+1000,3,1.0,1,3,1,0
C01w,ကွ,ဗျည်းတွဲ (က+ဝ),01.11,U+1000 U+103D,33,1.5,2,2,1,1
C70,ကျ,ဗျည်းတွဲ (က+ယ),70.30,U+1000 U+103B,16,70.0,3,3,3,0
C70w,ကျွ,ဗျည်းတွဲ (က+ယ+ဝ),70.31,U+1000 U+103B U+103D,21,70.5,4,2,4,1
...
```

### ၂။ `vowel_keys.csv` (Sample Content)

```csv
V_ID,Vowel_Type,Example,H_ID_Syllable,Semantic_Category,S_ID,Freq_Rank,S_Den,IPA,X_Code,C_Score,Tone,L_Code,D_Code,SC_Effect,Unicode_Markup
V01,အခြေခံသရ,အ,145.00-0000.01,တည်မြဲခြင်း/အခြေခံဖြစ်တည်မှု,VS01,1,7,/a/,0,0,0,0,0,0,""
V03,သံရှည်သရ,အား,145.00-0012.03,တည်မြဲခြင်း/အခြေခံဖြစ်တည်မှု,VS01,1.5,8.5,/á:/,1,1,2,1,0,0,U+102C U+1038
V41,သံတိုသရ,အတ်,145.00-0010.41,အဆုံးသတ်/ထစ်ခြင်း,VS14,10,6.0,/aʔ/,10,1,1,0,0,0,U+103A U+1039
V73,ဒွိသရ,အိုင်း,145.00-0012.73,ပိုင်ဆိုင်/နေရာပြောင်းလဲဆိုင်ရာ,VS09,9.5,9.0,/áɪ:/,1,1,2,1,1,0,U+102E U+1032 U+1038
...
```

ဤဖွဲ့စည်းပုံသည် သင့် AI စနစ်တွင် **feature engineering** လုပ်ငန်းစဉ်အတွက် အခြေခံအချက်အလက်များ တိကျစွာရရှိနိုင်စေရန် အထောက်အကူပြုပါလိမ့်မည်။

-----
