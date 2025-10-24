#!/usr/bin/env node
// tokenize_cli.js

// ၁။ အင်ဂျင်ကို (Class ပုံစံခွက်ကို) ခေါ်ယူခြင်း
const NNLDSMyanmarTokenizer = require('./myanmar_tokenizer'); // <-- `NNLDSMyanmarTokenizer` ကို တိုက်ရိုက်ယူသည်

// Global Tokenizer instance
let tokenizer = null;

try {
    // ၂။ Class အသစ်တစ်ခုကို စတင်ခြင်း (new operator ဖြင့်)
    tokenizer = new NNLDSMyanmarTokenizer(); // <-- `new` ကို သုံးထားသည်
    
    // ဒီနေရာမှာ သင့်ရဲ့ မူရင်း Code ထဲက Error ဖြစ်နိုင်တဲ့ စာကြောင်းကို ဖြုတ်ထားလိုက်ပါ
    // console.error("✅ NNLDS Myanmar Tokenizer initialized successfully"); 
    
} catch (e) {
    console.error("❌ Error: Could not initialize the Tokenizer.");
    console.error(e);
    process.exit(1);
}

// ... (အောက်ဖက်ရှိ ကျန် Code များအားလုံး မပြောင်းလဲဘဲ ထားပါ)
// ... runTokenization() function ကို အသုံးပြုပါ

/**
 * Command line arguments မှ စာသားကို ရယူပြီး Tokenization လုပ်ဆောင်သည်
 */
function runTokenization() {
    const args = process.argv.slice(2);
    
    // File input support
    if (args[0] === '-f' || args[0] === '--file') {
        if (!args[1]) {
            showUsage();
            return;
        }
        processFileInput(args[1]);
        return;
    }
    
    // Standard text input
    const textToTokenize = args.join(' ');

    if (!textToTokenize) {
        showUsage();
        return;
    }

    processTextInput(textToTokenize);
}

/**
 * File မှ input ကို လက်ခံပြီး process လုပ်ခြင်း
 */
function processFileInput(filePath) {
    const fs = require('fs');
    const path = require('path');
    
    try {
        const fullPath = path.resolve(filePath);
        if (!fs.existsSync(fullPath)) {
            console.error(`❌ Error: File not found - ${fullPath}`);
            process.exit(1);
        }
        
        const textToTokenize = fs.readFileSync(fullPath, 'utf8');
        processTextInput(textToTokenize.trim(), `file: ${filePath}`);
        
    } catch (error) {
        console.error(`❌ Error reading file: ${error.message}`);
        process.exit(1);
    }
}

/**
 * Text input ကို process လုပ်ခြင်း
 */
function processTextInput(textToTokenize, source = 'command line') {
    try {
        const startTime = process.hrtime.bigint();
        
        // Tokenization စတင်
        const tokens = tokenizer.tokenize(textToTokenize);
        
        const endTime = process.hrtime.bigint();
        const duration = Number(endTime - startTime) / 1000000; // milliseconds

        const output = {
            status: "success",
            source: source,
            original_text: textToTokenize,
            token_count: tokens.length,
            duration_ms: duration.toFixed(2),
            tokens: tokens,
            statistics: {
                myanmar_syllables: tokens.filter(t => t.type === 'MYANMAR_SYLLABLE').length,
                english_words: tokens.filter(t => t.type === 'ENGLISH_WORD').length,
                numbers: tokens.filter(t => t.type === 'NUMBER').length,
                punctuation: tokens.filter(t => t.type === 'PUNCTUATION').length,
                whitespace: tokens.filter(t => t.type === 'WHITESPACE').length
            }
        };
        
        // JSON format ဖြင့် ရလဒ်ကို ထုတ်ပေးခြင်း
        console.log(JSON.stringify(output, null, 2));

    } catch (e) {
        const errorOutput = {
            status: "error",
            message: "Tokenization Failed",
            details: e.message,
            stack: process.env.DEBUG ? e.stack : undefined
        };
        console.log(JSON.stringify(errorOutput, null, 2));
        process.exit(1);
    }
}

/**
 * အသုံးပြုပုံ လမ်းညွှန်ကို ပြသခြင်း
 */
function showUsage() {
    const usage = {
        status: "usage",
        commands: {
            "text_input": "node tokenize_cli.js \"<text to tokenize>\"",
            "file_input": "node tokenize_cli.js -f <filename>",
            "examples": [
                "node tokenize_cli.js \"မင်္ဂလာပါ ကမ္ဘာကြီး\"",
                "node tokenize_cli.js \"Hello မြန်မာပြည် 123!\"",
                "node tokenize_cli.js -f input.txt"
            ]
        },
        description: "NNLDS Myanmar Tokenizer - Command Line Interface"
    };
    
    console.log(JSON.stringify(usage, null, 2));
    process.exit(1);
}

// Script ကို စတင်ခြင်း
if (require.main === module) {
    runTokenization();
}

// Module အဖြစ် export လုပ်ခြင်း
module.exports = { runTokenization };
