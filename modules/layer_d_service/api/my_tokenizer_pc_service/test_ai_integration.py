# test_ai_integration.py - Unicode Error ဖြေရှင်းပြီးသော ဗားရှင်း

import subprocess
import json
import os
import sys # Warning များကို ဖော်ပြရန် လိုအပ်ပါက

# --- ၁။ Tokenizer ကို ခေါ်သုံးမည့် Function ---
def tokenize_myanmar_text(text):
    """Python မှ Node.js tokenizer (tokenize_cli.js) ကို ခေါ်ယူအသုံးပြုခြင်း"""
    
    # Node.js command ကို သတ်မှတ်ခြင်း
    command = ['node', 'tokenize_cli.js', text]
    
    try:
        # Command ကို run ခြင်း
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=10, 
            # UnicodeDecodeError ကို ဖြေရှင်းရန်အတွက် ဤနေရာတွင် 'utf8' ကို သတ်မှတ်သည်
            encoding='utf8', 
            errors='ignore'
        )
        
        # Error မရှိဘဲ ပြီးဆုံးခြင်းရှိမရှိ စစ်ဆေးခြင်း
        if result.returncode == 0:
            # Node.js က Error တွေကို stderr မှာ ထုတ်ပေးခြင်း ရှိမရှိ စစ်ဆေးခြင်း
            if result.stderr:
                 # console.error() မှ Warning များကို ထုတ်ပြခြင်း
                 print(f"\n--- Node.js Warning/Error Output ---\n{result.stderr.strip()}", file=sys.stderr)

            # JSON.loads (result.stdout) ကို မဖတ်မီ စစ်ဆေးပါ
            if not result.stdout.strip():
                 return {'status': 'error', 'message': 'Node.js did not return any JSON output.'}

            return json.loads(result.stdout)
        else:
            # Node.js Script ထဲက Error ဖြစ်ခဲ့ရင်
            return {
                'status': 'error', 
                'message': 'Tokenizer Script Failed', 
                'details': result.stderr.strip()
            }
            
    except Exception as e:
        # Python စနစ်ကိုယ်တိုင် Error ဖြစ်ခဲ့ရင်
        return {'status': 'error', 'message': str(e)}

# --- ၂။ AI စနစ်တွင် အသုံးပြုခြင်း ဥပမာ ---
if __name__ == "__main__":
    print("--- Myanmar Tokenizer ကို စမ်းသပ်ခြင်း (Python Integration) ---")

    myanmar_text = "AI နည်းပညာသည် မြန်မာစာကို ခွဲခြမ်းစိတ်ဖြာနိုင်ပါပြီ။"
    print(f"ပေးပို့မည့် စာသား: \"{myanmar_text}\"")

    # Tokenizer ကို ခေါ်သုံးခြင်း
    tokens = tokenize_myanmar_text(myanmar_text)

    # ရလဒ်ကို ဖော်ပြခြင်း
    print("\n--- ရလဒ် (JSON Output) ---")
    print(json.dumps(tokens, indent=2, ensure_ascii=False)) 
    print("----------------------------")

    # ရလဒ်ထဲက tokens တွေကိုပဲ ထုတ်ကြည့်ခြင်း
    if tokens and tokens.get('status') == 'success':
        print("\nခွဲခြမ်းထားသော စကားလုံးများ:")
        # ယာယီ tokenize logic ကြောင့် spaces များ ပါလာနိုင်သည်
        print([t['token'] for t in tokens['tokens'] if t['token'].strip() != ''])
