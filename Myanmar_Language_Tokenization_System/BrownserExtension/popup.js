// popup.js

document.getElementById('tokenizeButton').addEventListener('click', () => {
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = 'ခွဲခြမ်းစိတ်ဖြာနေသည်...';

    // ၁။ လက်ရှိ Active Tab ကို ရယူခြင်း
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        const activeTab = tabs[0];
        
        // ၂။ စာမျက်နှာပေါ်မှ ရွေးချယ်ထားသော စာသားကို ရယူရန် Script ကို execute လုပ်ခြင်း
        chrome.scripting.executeScript({
            target: { tabId: activeTab.id },
            func: getSelectedText,
        }, (injectionResults) => {
            const selectedText = injectionResults && injectionResults[0] ? injectionResults[0].result : null;
            
            if (!selectedText) {
                resultsDiv.innerHTML = '<div class="error">⚠️ စာသားကို ဦးစွာ ရွေးချယ်ပေးပါ။</div>';
                return;
            }

            // ၃။ Content Script သို့ Tokenization လုပ်ရန် Message ပို့ခြင်း
            chrome.tabs.sendMessage(activeTab.id, {
                action: "tokenize_selection",
                data: selectedText
            }, (response) => {
                if (chrome.runtime.lastError) {
                    resultsDiv.innerHTML = '<div class="error">❌ Extension ချိတ်ဆက်မှု အဆင်မပြေပါ။ (Tab ကို Reload လုပ်ရန် လိုအပ်နိုင်သည်)</div>';
                    return;
                }

                if (response.error) {
                    resultsDiv.innerHTML = `<div class="error">❌ Tokenization Error: ${response.error}</div>`;
                } else {
                    // ၄။ ရလဒ်ကို UI ပေါ်တွင် ပြသခြင်း
                    displayTokens(response.tokens, resultsDiv);
                }
            });
        });
    });
});

// ရွေးချယ်ထားသော စာသားကို DOM မှ ပြန်ယူပေးသည်
function getSelectedText() {
    return window.getSelection().toString().trim();
}

// Token များကို UI ပေါ်တွင် အရောင်များဖြင့် ပြသပေးသော function
function displayTokens(tokens, container) {
    // စုစုပေါင်း Token အရေအတွက်ကို ပြသသည်။
    container.innerHTML = `<div class="info">စုစုပေါင်း: ${tokens.length} tokens</div>`;
    
    tokens.forEach(token => {
        if (token.type !== 'WHITESPACE') {
            const span = document.createElement('span');
            // Token တွင် text, syllable, or original မှ တစ်ခုခုကို ပြသသည်။
            span.textContent = token.text || token.syllable || token.original || 'N/A';
            
            // Token အမျိုးအစားအလိုက် CSS Class သတ်မှတ်ခြင်း
            let typeClass = '';
            if (token.type === 'MYANMAR_SYLLABLE') {
                typeClass = 'myanmar';
            } else if (token.type === 'ENGLISH_WORD') {
                typeClass = 'english';
            } else if (token.type === 'NUMBER') {
                typeClass = 'number';
            } else if (token.type === 'PUNCTUATION') {
                typeClass = 'punctuation';
            }
            
            span.className = `token ${typeClass}`;
            container.appendChild(span);
        } else {
             // Whitespace အတွက် နေရာလပ် ခွဲပေးခြင်း
             container.appendChild(document.createTextNode(' '));
        }
    });
}