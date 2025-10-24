// tokenize_api.js - REST API Service for AI Integration
const http = require('http');
const { URL } = require('url');

// ❌ အရင် Code: const { createMultilingualTokenizer } = require('./myanmar_tokenizer');
// ✅ ပြင်ဆင်ပြီး Code: NNLDSMyanmarTokenizer Class ကို တိုက်ရိုက် ခေါ်ယူခြင်း
const NNLDSMyanmarTokenizer = require('./myanmar_tokenizer');

// ❌ အရင် Code: const tokenizer = createMultilingualTokenizer();
// ✅ ပြင်ဆင်ပြီး Code: Class အသစ် စတင်ပြီး Instance ဖန်တီးခြင်း
let tokenizer = null;
try {
    tokenizer = new NNLDSMyanmarTokenizer();
    console.log("✅ NNLDS Myanmar Tokenizer initialized successfully.");
} catch (e) {
    console.error("❌ Error: Could not initialize the Tokenizer.");
    console.error(e.message);
    process.exit(1);
}

const PORT = process.env.PORT || 3000;

const server = http.createServer(async (req, res) => {
    const { pathname, searchParams } = new URL(req.url, `http://${req.headers.host}`);
    
    // CORS headers
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
    
    if (req.method === 'OPTIONS') {
        res.writeHead(200);
        res.end();
        return;
    }
    
    if (pathname === '/tokenize' && (req.method === 'GET' || req.method === 'POST')) {
        
        const startTime = process.hrtime();
        
        try {
            let text = '';
            
            if (req.method === 'GET') {
                text = searchParams.get('text') || '';
            } else {
                // POST request
                const body = await getRequestBody(req);
                const data = JSON.parse(body);
                text = data.text || '';
            }
            
            if (!text) {
                sendResponse(res, 400, {
                    status: 'error',
                    message: 'Missing "text" parameter in GET or POST body'
                });
                return;
            }
            
            // Tokenization
            const tokens = tokenizer.tokenize(text);
            
            const endTime = process.hrtime(startTime);
            const duration = (endTime[0] * 1000) + (endTime[1] / 1000000);
            
            sendResponse(res, 200, {
                status: 'success',
                input_text: text,
                token_count: tokens.length,
                duration_ms: duration.toFixed(2),
                tokens: tokens
            });
            
        } catch (error) {
            sendResponse(res, 500, {
                status: 'error',
                message: 'Tokenization failed',
                error: error.message
            });
        }
    } else if (pathname === '/health') {
        sendResponse(res, 200, {
            status: 'healthy',
            service: 'NNLDS Myanmar Tokenizer API',
            version: '1.0.0',
            tokenizer_status: tokenizer ? tokenizer.getStatus() : 'uninitialized'
        });
    } else {
        sendResponse(res, 404, {
            status: 'error',
            message: 'Endpoint not found. Use /tokenize or /health'
        });
    }
});

function getRequestBody(req) {
    return new Promise((resolve, reject) => {
        let body = '';
        req.on('data', chunk => {
            body += chunk.toString();
        });
        req.on('end', () => {
            try {
                resolve(body);
            } catch (err) {
                reject(err);
            }
        });
        req.on('error', reject);
    });
}

function sendResponse(res, statusCode, data) {
    res.writeHead(statusCode, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify(data, null, 2));
}

server.listen(PORT, () => {
    console.log(`🚀 Tokenizer API Server running at http://localhost:${PORT}`);
    console.log(`Endpoints: /tokenize (POST/GET), /health (GET)`);
});
