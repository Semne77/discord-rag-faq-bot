/**
 * Validate if a given string is a non-empty string.
 * @param {string} str
 * @returns {boolean}
 */
export function isNonEmptyString(str) {
    return typeof str === 'string' && str.trim().length > 0;
}

/**
 * Validate RAG query payload.
 * Expected: { query: "<string>" }
 */
export function validateRagQueryPayload(payload) {
    if (!payload || !isNonEmptyString(payload.query)) {
        return { valid: false, message: "Invalid request: 'query' must be a non-empty string." };
    }
    return { valid: true };
}

/**
 * Validate document ingestion payload.
 * Expected: { document: "<string>" }
 */
export function validateIngestPayload(payload) {
    if (!payload || !isNonEmptyString(payload.document)) {
        return { valid: false, message: "Invalid request: 'document' must be a non-empty string." };
    }
    return { valid: true };
}

/**
 * Validate feedback payload.
 * Expected: { userId: "<string>", feedback: "<string>" }
 */
export function validateFeedbackPayload(payload) {
    if (!payload || !isNonEmptyString(payload.userId) || !isNonEmptyString(payload.feedback)) {
        return { valid: false, message: "Invalid request: 'userId' and 'feedback' must be non-empty strings." };
    }
    return { valid: true };
}
