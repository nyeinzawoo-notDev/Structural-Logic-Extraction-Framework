import pandas as pd

# Load NSTF-NNLDS Core Data
data = pd.read_csv("NSTF_NNLDS_Core_Data.tsv")

# ဗျည်းနဲ့ သရ meaning ကို AI logic ထဲသို့ သုံးခြင်း
def get_essence(char):
    row = data[data["Character"] == char]
    if not row.empty:
        return {
            "english": row.iloc[0]["Meaning_Essence_EN"],
            "myanmar": row.iloc[0]["Meaning_Essence_MM"],
            "t_code": row.iloc[0]["T_Code"]
        }
    return None

print(get_essence("င"))
# Output => {'english': 'Contain / Silence', 'myanmar': 'အတွင်းသို့ သိမ်းခြင်း၊ တိတ်ဆိတ်ခြင်း', 't_code': 'T017'}
