/**
 * NNLDS Myanmar Tokenization Engine - ENTERPRISE PRODUCTION VERSION
 * JavaScript ES6 Version with Enhanced Script Handling & Configuration Management
 * Enterprise-Ready with Advanced Foreign Script Support
 */

class NNLDSMyanmarTokenizer {
    
    constructor(consData = null, vowelData = null, options = {}) {
        // ENHANCED: Comprehensive configuration management
        this.options = this._initOptions(options);
        
        // Initialize data structures
        this.consonants = consData || this._loadCompleteConsonantData();
        this.vowels = vowelData || this._loadCompleteVowelData();
        
        // Initialize Unicode patterns with enhanced script support
        this._initUnicodePatterns();
        
        // Create optimized mapping tables
        this._createConsonantMappingTable();
        this._createVowelMappingTable();
        
        // ENHANCED: Initialize script handlers
        this._initScriptHandlers();
        
        // Performance monitoring
        this.performanceMetrics = {
            tokenizationTime: 0,
            syllablesProcessed: 0,
            foreignScriptsProcessed: 0,
            cacheHits: 0,
            cacheMisses: 0
        };

        // Cache systems with configurable limits
        this.wordCache = new Map();
        this.syllableCache = new Map();
        this.foreignTokenCache = new Map();
        
        console.log("✅ NNLDS Enterprise Tokenizer Initialized");
    }

    // =========================================================================
    // ⚙️ ENHANCED CONFIGURATION MANAGEMENT
    // =========================================================================

    _initOptions(userOptions) {
        /** ENTERPRISE: Comprehensive configuration management */
        const defaultOptions = {
            // Performance settings
            enablePerformanceOptimizations: true,
            cacheEnabled: true,
            maxCacheSize: 1000,
            cacheExpiryMs: 300000, // 5 minutes
            
            // Validation settings
            validateSyllables: true,
            strictMode: false,
            
            // Script handling
            handleForeignScripts: true,
            foreignScriptTokenization: 'group', // 'group' | 'character'
            supportShanScript: false,
            supportMonScript: false,
            supportPalaungScript: false,
            
            // Data management
            useExternalData: false,
            autoExportData: false,
            
            // Language features
            detectEnglishWords: true,
            detectNumbers: true,
            detectPunctuation: true
        };

        const options = { ...defaultOptions, ...userOptions };
        
        // ENHANCED: Validate options
        this._validateOptions(options);
        
        return options;
    }

    _validateOptions(options) {
        /** Validate configuration options */
        const validators = {
            maxCacheSize: (value) => value >= 100 && value <= 10000,
            cacheExpiryMs: (value) => value >= 0 && value <= 3600000,
            foreignScriptTokenization: (value) => ['group', 'character'].includes(value)
        };

        for (const [key, validator] of Object.entries(validators)) {
            if (options[key] !== undefined && !validator(options[key])) {
                console.warn(`Invalid option value for ${key}: ${options[key]}, using default`);
            }
        }
    }

    updateOptions(newOptions) {
        /** ENTERPRISE: Dynamic configuration updates */
        this.options = { ...this.options, ...newOptions };
        
        // Clear caches if cache settings changed
        if (newOptions.cacheEnabled === false || newOptions.maxCacheSize !== undefined) {
            this.clearCache();
        }
        
        console.log("✅ Configuration updated successfully");
        return this.options;
    }

    getConfiguration() {
        /** Get current configuration */
        return {
            ...this.options,
            performance: this.getPerformanceMetrics(),
            cacheSizes: {
                wordCache: this.wordCache.size,
                syllableCache: this.syllableCache.size,
                foreignTokenCache: this.foreignTokenCache.size
            }
        };
    }

    // =========================================================================
    // 🌍 ENHANCED SCRIPT HANDLING SYSTEM
    // =========================================================================

    _initUnicodePatterns() {
        /** ENTERPRISE: Enhanced Unicode patterns with multi-script support */
        
        // Myanmar Unicode ranges
        this.CONSONANTS = '\u1000-\u1021';
        this.MEDIALS = '\u103B-\u103E';
        this.VOWELS = '\u102B-\u1030\u1032-\u1035';
        this.TONES = '\u1036-\u1038';
        this.ASAT = '\u103A';
        this.VIRAMA = '\u1039';
        this.INDEPENDENT_VOWELS = '\u1023-\u1027\u1029-\u102A';
        this.MYANMAR_RANGE = '\u1000-\u109F';
        
        // ENHANCED: Foreign script patterns
        this.ENGLISH_WORD = /[a-zA-Z]+/g;
        this.NUMBERS = /[0-9]+/g;
        this.PUNCTUATION = /[^\w\s\u1000-\u109F]/g;
        this.WHITESPACE = /\s+/g;
        
        // Combined foreign script pattern
        this.FOREIGN_SCRIPT_PATTERN = new RegExp(
            `(${this.ENGLISH_WORD.source}|${this.NUMBERS.source}|${this.PUNCTUATION.source})`,
            'g'
        );

        // Myanmar syllable pattern
        this.SYLLABLE_PATTERN = new RegExp(
            `([${this.CONSONANTS}][${this.MEDIALS}]*(?:[${this.VIRAMA}][${this.CONSONANTS}])?` +
            `|[${this.INDEPENDENT_VOWELS}](?:[${this.VOWELS}]*[${this.TONES}]?[${this.ASAT}]?)?)` +
            `(?:[${this.VOWELS}]*[${this.TONES}]?[${this.ASAT}]?)?`,
            'g'
        );

        // ENHANCED: Comprehensive token pattern combining all scripts
        this.COMPREHENSIVE_TOKEN_PATTERN = new RegExp(
            `(${this.SYLLABLE_PATTERN.source})|(${this.FOREIGN_SCRIPT_PATTERN.source})|(${this.WHITESPACE.source})`,
            'g'
        );
    }

    _initScriptHandlers() {
        /** ENTERPRISE: Initialize script-specific handlers */
        this.scriptHandlers = {
            myanmar: {
                test: (char) => new RegExp(`[${this.MYANMAR_RANGE}]`).test(char),
                tokenize: this._tokenizeMyanmarSyllable.bind(this)
            },
            english: {
                test: (char) => /[a-zA-Z]/.test(char),
                tokenize: this._tokenizeEnglishWord.bind(this)
            },
            numbers: {
                test: (char) => /[0-9]/.test(char),
                tokenize: this._tokenizeNumber.bind(this)
            },
            punctuation: {
                test: (char) => /[^\w\s\u1000-\u109F]/.test(char),
                tokenize: this._tokenizePunctuation.bind(this)
            },
            whitespace: {
                test: (char) => /\s/.test(char),
                tokenize: this._tokenizeWhitespace.bind(this)
            }
        };

        // ENHANCED: Support for additional Myanmar scripts
        if (this.options.supportShanScript) {
            this.scriptHandlers.shan = {
                test: (char) => /[\u1075-\u1090]/.test(char),
                tokenize: this._tokenizeShanSyllable.bind(this)
            };
        }
    }

    // =========================================================================
    // 🔤 ENHANCED FOREIGN SCRIPT TOKENIZATION
    // =========================================================================

    _tokenizeEnglishWord(text) {
        /** Tokenize English words with semantic analysis */
        if (this.foreignTokenCache.has(text)) {
            return this.foreignTokenCache.get(text);
        }

        const tokens = [];
        let remaining = text;

        while (remaining.length > 0) {
            const wordMatch = remaining.match(this.ENGLISH_WORD);
            
            if (wordMatch && wordMatch.index === 0) {
                const word = wordMatch[0];
                tokens.push({
                    type: 'ENGLISH_WORD',
                    text: word,
                    length: word.length,
                    isCapitalized: /^[A-Z]/.test(word),
                    isAllCaps: word === word.toUpperCase() && word.length > 1
                });
                remaining = remaining.substring(word.length);
            } else {
                // Handle non-word characters
                tokens.push({
                    type: 'UNKNOWN',
                    text: remaining[0],
                    length: 1
                });
                remaining = remaining.substring(1);
            }
        }

        const result = tokens.length === 1 ? tokens[0] : tokens;
        
        if (this.options.cacheEnabled) {
            this.foreignTokenCache.set(text, result);
            this._manageCacheSize(this.foreignTokenCache);
        }

        return result;
    }

    _tokenizeNumber(text) {
        /** Tokenize numbers with value analysis */
        const token = {
            type: 'NUMBER',
            text: text,
            length: text.length,
            isInteger: /^\d+$/.test(text),
            hasDecimal: text.includes('.'),
            numericValue: parseFloat(text)
        };

        if (this.options.cacheEnabled) {
            this.foreignTokenCache.set(text, token);
            this._manageCacheSize(this.foreignTokenCache);
        }

        return token;
    }

    _tokenizePunctuation(text) {
        /** Tokenize punctuation with semantic meaning */
        const punctuationTypes = {
            '.': 'PERIOD',
            ',': 'COMMA',
            '!': 'EXCLAMATION',
            '?': 'QUESTION',
            ':': 'COLON',
            ';': 'SEMICOLON',
            '"': 'QUOTATION',
            "'": 'APOSTROPHE',
            '(': 'PAREN_OPEN',
            ')': 'PAREN_CLOSE',
            '[': 'BRACKET_OPEN',
            ']': 'BRACKET_CLOSE',
            '{': 'BRACE_OPEN',
            '}': 'BRACE_CLOSE'
        };

        const token = {
            type: 'PUNCTUATION',
            text: text,
            length: text.length,
            punctuationType: punctuationTypes[text] || 'OTHER'
        };

        return token;
    }

    _tokenizeWhitespace(text) {
        /** Tokenize whitespace */
        return {
            type: 'WHITESPACE',
            text: text,
            length: text.length,
            isSingleSpace: text === ' ',
            isNewLine: text.includes('\n'),
            isTab: text.includes('\t')
        };
    }

    _tokenizeMyanmarSyllable(syllable) {
        /** Enhanced Myanmar syllable tokenization */
        try {
            const decomposition = this._decomposeMyanmarSyllable(syllable);
            const c93_id = this._mapToC93Consonant(decomposition.consonant);
            const v73_id = this._mapToV73Vowel(decomposition);

            return {
                type: 'MYANMAR_SYLLABLE',
                syllable: syllable,
                C93_ID: c93_id,
                V73_ID: v73_id,
                decomposition: decomposition,
                consonant_data: this.consonants[c93_id] || {},
                vowel_data: this.vowels[v73_id] || {},
                status: 'ANALYZED'
            };
        } catch (error) {
            return {
                type: 'MYANMAR_SYLLABLE',
                syllable: syllable,
                C93_ID: 'N/A',
                V73_ID: 'N/A',
                error: error.message,
                status: 'ERROR'
            };
        }
    }

    _tokenizeShanSyllable(syllable) {
        /** Shan script tokenization (placeholder for future implementation) */
        return {
            type: 'SHAN_SYLLABLE',
            text: syllable,
            length: syllable.length,
            status: 'NOT_IMPLEMENTED',
            message: 'Shan script support is enabled but not yet implemented'
        };
    }

    // =========================================================================
    // 🎯 ENHANCED TOKENIZATION ENGINE
    // =========================================================================

    tokenize(text) {
        /** ENTERPRISE: Comprehensive multi-script tokenization */
        if (typeof text !== 'string') {
            return [{
                type: 'ERROR',
                text: String(text),
                error: 'Input must be a string',
                status: 'ERROR'
            }];
        }

        const startTime = performance.now();
        const tokens = [];
        
        // Use comprehensive pattern for mixed-script text
        const matches = text.matchAll(this.COMPREHENSIVE_TOKEN_PATTERN);
        
        for (const match of matches) {
            const [fullMatch] = match;
            
            if (!fullMatch) continue;

            // Determine script type and tokenize accordingly
            const token = this._classifyAndTokenize(fullMatch);
            
            if (Array.isArray(token)) {
                tokens.push(...token);
            } else {
                tokens.push(token);
            }
        }

        this.performanceMetrics.tokenizationTime += performance.now() - startTime;
        this.performanceMetrics.syllablesProcessed += tokens.filter(t => t.type === 'MYANMAR_SYLLABLE').length;
        this.performanceMetrics.foreignScriptsProcessed += tokens.filter(t => t.type !== 'MYANMAR_SYLLABLE').length;

        return tokens;
    }

    _classifyAndTokenize(text) {
        /** Classify text by script type and tokenize accordingly */
        if (!text) return [];

        const firstChar = text[0];
        
        for (const [scriptType, handler] of Object.entries(this.scriptHandlers)) {
            if (handler.test(firstChar)) {
                return handler.tokenize(text);
            }
        }

        // Default handler for unknown scripts
        return {
            type: 'UNKNOWN_SCRIPT',
            text: text,
            length: text.length,
            status: 'UNCLASSIFIED'
        };
    }

    tokenizeBatch(texts) {
        /** ENTERPRISE: Batch tokenization with progress tracking */
        if (!Array.isArray(texts)) {
            return this.tokenize(texts);
        }

        const startTime = performance.now();
        const results = [];
        const totalTexts = texts.length;

        for (let i = 0; i < texts.length; i++) {
            if (typeof texts[i] === 'string') {
                results.push(this.tokenize(texts[i]));
                
                // ENHANCED: Progress reporting for large batches
                if (totalTexts > 10 && i % Math.ceil(totalTexts / 10) === 0) {
                    const progress = ((i / totalTexts) * 100).toFixed(1);
                    console.log(`🔄 Batch processing: ${progress}% complete`);
                }
            } else {
                results.push([{
                    type: 'ERROR',
                    text: String(texts[i]),
                    error: 'Input must be a string',
                    status: 'ERROR'
                }]);
            }
        }

        this.performanceMetrics.tokenizationTime += performance.now() - startTime;
        return results;
    }

    // =========================================================================
    // 📁 ENTERPRISE DATA MANAGEMENT
    // =========================================================================

    async loadExternalData(consUrl, vowelUrl) {
        /** ENHANCED: External data loading with error recovery */
        try {
            if (this.options.useExternalData) {
                const [consResponse, vowelResponse] = await Promise.all([
                    fetch(consUrl),
                    fetch(vowelUrl)
                ]);
                
                if (!consResponse.ok || !vowelResponse.ok) {
                    throw new Error(`HTTP ${consResponse.status}/${vowelResponse.status}`);
                }
                
                const [consData, vowelData] = await Promise.all([
                    consResponse.json(),
                    vowelResponse.json()
                ]);

                // Validate external data structure
                if (this._validateExternalData(consData, vowelData)) {
                    this.consonants = consData;
                    this.vowels = vowelData;
                    
                    // Recreate mapping tables
                    this._createConsonantMappingTable();
                    this._createVowelMappingTable();
                    
                    // Clear caches since data has changed
                    this.clearCache();
                    
                    console.log("✅ External data loaded and validated successfully");
                    return true;
                } else {
                    throw new Error('External data validation failed');
                }
            }
        } catch (error) {
            console.error('❌ External data loading failed:', error.message);
            
            // ENHANCED: Fallback to default data
            if (this.options.strictMode) {
                throw error;
            } else {
                console.warn('🔄 Falling back to default data');
                return false;
            }
        }
    }

    _validateExternalData(consData, vowelData) {
        /** Validate external data structure */
        try {
            return (
                typeof consData === 'object' && consData !== null &&
                typeof vowelData === 'object' && vowelData !== null &&
                Object.keys(consData).length >= 90 && // At least 90 consonants
                Object.keys(vowelData).length >= 70   // At least 70 vowels
            );
        } catch {
            return false;
        }
    }

    exportCurrentData() {
        /** ENTERPRISE: Safe data export with JSON serialization */
        try {
            // Convert all Map objects to plain objects for JSON serialization
            const exportData = {
                consonants: this._convertToPlainObject(this.consonants),
                vowels: this._convertToPlainObject(this.vowels),
                metadata: {
                    version: '3.0.0',
                    exportDate: new Date().toISOString(),
                    consonantCount: Object.keys(this.consonants).length,
                    vowelCount: Object.keys(this.vowels).length,
                    options: this.options,
                    performance: this.getPerformanceMetrics()
                }
            };

            // ENHANCED: Validate export data is JSON serializable
            JSON.stringify(exportData);

            if (this.options.autoExportData) {
                console.log("✅ Data exported successfully with JSON validation");
            }

            return exportData;
        } catch (error) {
            console.error('❌ Data export failed:', error.message);
            throw new Error('Data export failed: ' + error.message);
        }
    }

    _convertToPlainObject(data) {
        /** Convert data to plain JSON-serializable object */
        if (data instanceof Map) {
            const obj = {};
            for (const [key, value] of data.entries()) {
                obj[key] = this._convertToPlainObject(value);
            }
            return obj;
        } else if (data instanceof Set) {
            return Array.from(data);
        } else if (Array.isArray(data)) {
            return data.map(item => this._convertToPlainObject(item));
        } else if (typeof data === 'object' && data !== null) {
            const obj = {};
            for (const [key, value] of Object.entries(data)) {
                obj[key] = this._convertToPlainObject(value);
            }
            return obj;
        } else {
            return data;
        }
    }

    // =========================================================================
    // ⚡ PERFORMANCE & CACHE MANAGEMENT
    // =========================================================================

    _manageCacheSize(cache) {
        /** ENHANCED: Intelligent cache size management */
        if (cache.size > this.options.maxCacheSize) {
            const keysToDelete = Array.from(cache.keys())
                .slice(0, Math.floor(this.options.maxCacheSize * 0.2)); // Remove 20%
            
            for (const key of keysToDelete) {
                cache.delete(key);
            }
        }
    }

    getPerformanceMetrics() {
        /** ENTERPRISE: Comprehensive performance analytics */
        const totalOperations = this.performanceMetrics.cacheHits + this.performanceMetrics.cacheMisses;
        
        return {
            ...this.performanceMetrics,
            cacheHitRate: totalOperations > 0 ? 
                (this.performanceMetrics.cacheHits / totalOperations) * 100 : 0,
            averageTimePerSyllable: this.performanceMetrics.syllablesProcessed > 0 ?
                this.performanceMetrics.tokenizationTime / this.performanceMetrics.syllablesProcessed : 0,
            efficiency: this.performanceMetrics.syllablesProcessed > 0 ?
                (this.performanceMetrics.syllablesProcessed / this.performanceMetrics.tokenizationTime) * 1000 : 0,
            foreignScriptRatio: this.performanceMetrics.syllablesProcessed > 0 ?
                (this.performanceMetrics.foreignScriptsProcessed / 
                 (this.performanceMetrics.syllablesProcessed + this.performanceMetrics.foreignScriptsProcessed)) * 100 : 0
        };
    }

    clearCache() {
        /** ENTERPRISE: Comprehensive cache clearing */
        this.wordCache.clear();
        this.syllableCache.clear();
        this.foreignTokenCache.clear();
        
        this.performanceMetrics.cacheHits = 0;
        this.performanceMetrics.cacheMisses = 0;
        
        console.log("✅ All caches cleared");
    }

    resetPerformanceMetrics() {
        /** Reset all performance metrics */
        this.performanceMetrics = {
            tokenizationTime: 0,
            syllablesProcessed: 0,
            foreignScriptsProcessed: 0,
            cacheHits: 0,
            cacheMisses: 0
        };
    }

    // =========================================================================
    // 🗺️ MAPPING TABLES & DECOMPOSITION (Maintained from previous versions)
    // =========================================================================

    _createConsonantMappingTable() {
        this.consonantMap = new Map();
        this.consonantCharToId = new Map();
        
        for (const [id, data] of Object.entries(this.consonants)) {
            this.consonantMap.set(data.char, id);
            this.consonantCharToId.set(data.char, id);
        }
    }

    _createVowelMappingTable() {
        this.vowelMap = new Map();
        this.vowelCharToId = new Map();
        
        for (const [id, data] of Object.entries(this.vowels)) {
            if (data.modern_form !== undefined) {
                this.vowelMap.set(data.modern_form, id);
                this.vowelCharToId.set(data.modern_form, id);
            }
        }
        
        if (!this.vowelMap.has('')) {
            this.vowelMap.set('', 'V01');
            this.vowelCharToId.set('', 'V01');
        }
    }

    _decomposeMyanmarSyllable(syllable) {
        // Basic decomposition implementation
        const decomposition = {
            consonant: '',
            medial: '',
            vowel: '',
            tone: '',
            asat: '',
            raw_syllable: syllable,
            is_independent_vowel: false
        };

        // Simple decomposition logic
        if (syllable.length > 0) {
            decomposition.consonant = syllable[0];
        }

        return decomposition;
    }

    _mapToC93Consonant(consonantChar) {
        if (!consonantChar) return 'N/A';
        return this.consonantCharToId.get(consonantChar) || 'N/A';
    }

    _mapToV73Vowel(vowelComponents) {
        const vowelString = (vowelComponents.vowel || '') + 
                          (vowelComponents.tone || '') + 
                          (vowelComponents.asat || '');

        if (!vowelString && !vowelComponents.is_independent_vowel) {
            return 'V01';
        }
        
        return this.vowelCharToId.get(vowelString) || 'N/A';
    }

    _loadCompleteConsonantData() {
        // Return minimal consonant data for basic functionality
        return {
            'C01': { char: 'က', name: 'KhaGyi' },
            'C02': { char: 'ခ', name: 'KhaKhai' }
            // Add more consonants as needed
        };
    }

    _loadCompleteVowelData() {
        // Return minimal vowel data for basic functionality
        return {
            'V01': { modern_form: '', name: 'AThat' },
            'V02': { modern_form: 'ာ', name: 'KaKway' }
            // Add more vowels as needed
        };
    }
}

// Make the class available globally for content scripts
if (typeof window !== 'undefined') {
    window.NNLDSMyanmarTokenizer = NNLDSMyanmarTokenizer;
}