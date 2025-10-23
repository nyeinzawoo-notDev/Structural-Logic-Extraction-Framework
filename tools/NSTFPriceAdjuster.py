import json

class NSTFPriceAdjuster:
    """
    NSTF Framework ကို အသုံးပြု၍ လုပ်အားခနှင့် ကုန်ဈေးနှုန်း မျှတမှုကို တွက်ချက်သော စနစ်။
    T-Codes များကို Vector တန်ဖိုး (0.0 မှ 1.0) အဖြစ် အသုံးပြုပြီး ကျင့်ဝတ်ဆိုင်ရာ ဆုံးဖြတ်ချက်ချသည်။
    """

    # T-Code Value Definitions (Simplified for demonstration)
    # Production / Input T-Codes
    T003_EXPANSION = 0.85  # စီးပွားရေး တိုးတက်မှု (ဈေးကွက်လွတ်လပ်ခွင့်)
    T011_GREED = 0.70      # အမြတ်ခေါင်းပုံဖြတ်မှု (လက်ရှိဈေးကွက်မှာ လိုဘရဲ့လွှမ်းမိုးမှု)
    T020_SUSTAINING = 0.60 # လက်ရှိ လုပ်အားခဖြင့် အသက်မွေးဝမ်းကျောင်းနိုင်စွမ်း (ဝင်ငွေ/ဝယ်နိုင်စွမ်း)
    T017_CONTAINMENT = 0.50 # ဥပဒေစည်းကမ်းနှင့် ထိန်းချုပ်မှု

    # Ethical / Output T-Codes
    T024_JUSTICE = 0.95    # တရားမျှတမှု (Target)
    T028_UNITY = 0.75      # ညီညွတ်ခြင်း/လူမှုတည်ငြိမ်မှု

    # ဈေးကွက်ဒေတာ
    WAGE_CURRENT = 6000     # လက်ရှိ အခြေခံ လုပ်အားခ (ကျပ်)
    RICE_PRICE_CURRENT = 3000 # ဆန်တစ်ပြည် လက်ရှိဈေးနှုန်း (ကျပ်)
    BASIC_COST_OF_LIVING = 8500 # လူတစ်ဦး အခြေခံနေထိုင်မှုစရိတ် (T024 မျှတမှုရရန် လိုအပ်သော ဝင်ငွေ)

    def __init__(self, t_codes_data):
        """T-Code တန်ဖိုးများဖြင့် စနစ်ကို စတင်ခြင်း။"""
        self.t_codes = t_codes_data

    def _check_negative_extremes(self):
        """
        T-Code ဝင်ရိုးစွန်းများကို စစ်ဆေးခြင်း: T011 (လိုဘ) သည် T024 (တရားမျှတမှု) ကို ချိုးဖောက်ခြင်း ရှိ/မရှိ။
        """
        # Rule: T011 (လိုဘ) သည် T024 (တရားမျှတမှု) ထက် လွှမ်းမိုးနေပါက Negative Extreme (မတရားမှု) ဖြစ်သည်။
        if self.t_codes['T011_GREED'] > self.t_codes['T024_JUSTICE'] * 0.7:  # 70% threshold
            return True, "CRITICAL: T011 (လိုဘ) သည် T024 (တရားမျှတမှု) ၏ မျှတမှုကို လွန်ကဲစွာ ကျော်လွန်နေသည်။"
        return False, "NSTF မျှတမှု အဆင့်တွင် ရှိနေသည်။"

    def calculate_ideal_wage(self):
        """
        T024 (တရားမျှတမှု) ကို အခြေခံ၍ ဖြစ်သင့်သော လုပ်အားခကို တွက်ချက်သည်။
        """
        # T024 Positive Extreme (တရားမျှတသော မျှော်မှန်းချက်) ကို ရောက်ရှိစေမည့် ဝင်ငွေ။
        # တွက်ချက်မှု: လိုအပ်သော ဝင်ငွေ (8500) ကို T020 လက်ရှိ အားနည်းချက်နဲ့ ချိန်ညှိသည်။
        if self.t_codes['T020_SUSTAINING'] < 0.8: # T020 မှာ အားနည်းချက်ရှိနေရင် ချိန်ညှိဖို့လိုသည်။
            # (Basic Cost) / (T020 ရဲ့ လိုအပ်ချက်) ဖြင့် Ideal Wage ကို တွက်ချက်သည်။
            ideal_wage = self.BASIC_COST_OF_LIVING / self.t_codes['T024_JUSTICE'] 
            
            # T028 (ညီညွတ်ခြင်း) ကိုပါ ထည့်တွက်ခြင်း: T028 မြင့်လေ၊ ကူးပြောင်းမှုမြန်လေ ဖြစ်သောကြောင့် ဝင်ငွေကို မြှင့်ပေးသည်။
            ideal_wage *= (1 + (1 - self.t_codes['T028_UNITY']) * 0.1) 
            
            return round(ideal_wage, -2) # အနီးစပ်ဆုံး ရာဂဏန်းသို့ ပြန်ညှိခြင်း

    def calculate_ethical_price(self, ideal_wage):
        """
        T011 (လိုဘ) ကို ဖယ်ရှားပြီး T024 မျှတမှုရရှိစေမည့် ဖြစ်သင့်သော ဆန်ဈေးနှုန်းကို တွက်ချက်သည်။
        """
        # လက်ရှိ ဈေးနှုန်းတွင် T011 (လိုဘ) ပါဝင်မှုကို ဖယ်ရှားခြင်း။
        # ဈေးနှုန်း = (ကုန်ကျစရိတ် + မျှတသော အမြတ်)
        
        # ဥပမာ: လက်ရှိဈေးနှုန်းမှာ T011 က 30% လောက် လွှမ်းမိုးနေတယ်လို့ သတ်မှတ်ကြပါစို့ (T011_GREED = 0.7)။
        # T011_FACTOR = 1 - (1 - T011_GREED) ၏ အချိုး
        T011_FACTOR = 1 - (self.t_codes['T011_GREED'] / 2) # လိုဘရဲ့ တစ်ဝက်ကို ဖယ်ရှားခြင်း

        # မျှတသော ဈေးနှုန်း = လက်ရှိဈေးနှုန်း * T011 လျှော့ချသည့်အချိုး * (Ideal Wage/Current Wage)
        ethical_price = self.RICE_PRICE_CURRENT * T011_FACTOR * (ideal_wage / self.WAGE_CURRENT)
        
        # T003 (Expansion) ကို ထိန်းချုပ်ရန် T017 (စည်းကမ်း) ကို အသုံးပြုခြင်း
        # T017 မြင့်လေ၊ ဈေးနှုန်းကို ပိုမို တင်းကျပ်စွာ ထိန်းချုပ်လေ ဖြစ်သည်။
        ethical_price *= (1 - (self.t_codes['T017_CONTAINMENT'] * 0.1))
        
        return round(ethical_price, -1)

    def generate_nstf_guidance(self):
        """NSTF Final Guidance ကို ထုတ်ပေးခြင်း။"""
        is_negative_extreme, warning = self._check_negative_extremes()
        ideal_wage = self.calculate_ideal_wage()
        ethical_price = self.calculate_ethical_price(ideal_wage)
        
        guidance = {
            "NSTF_STATUS": "APPROVE with STRICT CONDITIONS",
            "WARNING": warning,
            "T_CODE_FOCUS": "T024 (တရားမျှတမှု) နှင့် T020 (ဥစ္စာ) ၏ မျှတမှုကို ပြန်လည်တည်ဆောက်ရန် လိုအပ်သည်။",
            "ACTIONABLE_GUIDANCE": {
                "WAGE_ADJUSTMENT_T020": f"လက်ရှိ {self.WAGE_CURRENT:,} ကျပ်မှ Ideal Wage {ideal_wage:,} ကျပ်သို့ မြှင့်တင်ရန်။",
                "PRICE_ADJUSTMENT_T011_T024": f"ဆန်တစ်ပြည်၏ ဈေးနှုန်းကို {self.RICE_PRICE_CURRENT:,} ကျပ်မှ {ethical_price:,} ကျပ်သို့ ချိန်ညှိရန်။",
                "CONTAINMENT_STRATEGY_T017": f"ဈေးနှုန်းကို တိုက်ရိုက်ထိန်းချုပ်မည့်အစား T011 (လိုဘ) ကို တားဆီးရန် ကုန်စည်ပို့ဆောင်ရေး (Logistics) စည်းမျဉ်း (T017) ကို မြှင့်တင်ပါ။",
                "RISK_MITIGATION_T003": "T003 (ဈေးကွက်လွတ်လပ်ခွင့်) ကို လုံးဝပိတ်ပင်ခြင်း မပြုရ၊ သို့သော် ဈေးနှုန်းတိုးမြှင့်ခြင်းကို T024 ၏ အောက်တွင်သာ ခွင့်ပြုရမည်။"
            },
            "T_CODE_BALANCE_SUMMARY": {
                "T011_GREED_LEVEL": f"{self.t_codes['T011_GREED']*100:.1f}%",
                "T024_JUSTICE_REQUIRED": f"{self.t_codes['T024_JUSTICE']*100:.1f}%"
            }
        }
        
        # Negative Extreme ရှိပါက NSTF Status ကို ပြောင်းလဲခြင်း။
        if is_negative_extreme:
            guidance["NSTF_STATUS"] = "CRITICAL REFUSE (ချက်ချင်း ပြုပြင်ရမည်)"
        
        return json.dumps(guidance, indent=4, ensure_ascii=False)

# --- စမ်းသပ်မှု လုပ်ဆောင်ခြင်း ---
# လက်ရှိ T-Code များကို အခြေအနေ (Scenario) တစ်ခုအရ သတ်မှတ်ခြင်း။
t_codes_vector_data = {
    'T003_EXPANSION': NSTFPriceAdjuster.T003_EXPANSION,
    'T011_GREED': NSTFPriceAdjuster.T011_GREED,
    'T020_SUSTAINING': NSTFPriceAdjuster.T020_SUSTAINING,
    'T017_CONTAINMENT': NSTFPriceAdjuster.T017_CONTAINMENT,
    'T024_JUSTICE': NSTFPriceAdjuster.T024_JUSTICE,
    'T028_UNITY': NSTFPriceAdjuster.T028_UNITY,
    # T010 (မေတ္တာ) စသည်တို့ကိုလည်း ဤနေရာတွင် ထည့်သွင်း ချိန်ညှိနိုင်ပါသည်။
}

adjuster = NSTFPriceAdjuster(t_codes_vector_data)
result = adjuster.generate_nstf_guidance()
print(result)
