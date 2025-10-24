// content_script.js

// multilingual preset options ကို အသုံးပြုပါ။
const tokenizerOptions = {
    handleForeignScripts: true,
    detectEnglishWords: true,
    detectNumbers: true
};

let myanmarTokenizer = null;

try {
    // NNLDSMyanmarTokenizer Class သည် myanmar_tokenizer.js မှ ရရှိမည်။
    if (typeof NNLDSMyanmarTokenizer !== 'undefined') {
        myanmarTokenizer = new NNLDSMyanmarTokenizer(null, null, tokenizerOptions);
        console.log("✅ NNLDS Tokenizer initialized successfully in Content Script.");
    } else {
        console.error("❌ NNLDSMyanmarTokenizer Class not found. Check myanmar_tokenizer.js loading.");
    }
} catch (e) {
    console.error("❌ Error initializing NNLDSMyanmarTokenizer:", e);
}


// Extension ၏ အခြားအစိတ်အပိုင်းများမှ Message ကို လက်ခံခြင်း
chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse) {
        if (request.action === "tokenize_selection" && myanmarTokenizer) {
            const selectedText = request.data;
            let resultTokens = [];
            let error = null;

            if (!selectedText) {
                error = "No text selected for tokenization.";
            } else {
                try {
                    // Tokenization ကို စတင်လုပ်ဆောင်သည်။
                    resultTokens = myanmarTokenizer.tokenize(selectedText);
                } catch (e) {
                    error = "Tokenization failed: " + e.message;
                    console.error("Tokenization Error:", e);
                }
            }

            // ရလဒ်ကို Popup သို့ Message မှတစ်ဆင့် ပြန်ပို့သည်။
            sendResponse({ 
                tokens: resultTokens, 
                originalText: selectedText,
                error: error
            });
            
            return true; // Asynchronously response ကို ပြန်ပို့ရန်
        }
    }
);
