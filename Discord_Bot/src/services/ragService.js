import axios from 'axios';
import config from '../config/index.js';
import winston from './loggingService.js';


const baseUrl = config.pythonRagUrl;

async function queryRag(question) {
    try {
        const response = await axios.post(`${baseUrl}/rag-query`, {
            query: question
        });
        return response.data.answer; // or response.data as needed
    } catch (error) {
        winston.error(`Error in queryRag: ${error.message}`);
        throw new Error('Failed to retrieve answer from RAG service.');
    }
}

async function addDocument(documentText) {
    try {
        const response = await axios.post(`${baseUrl}/ingest`, {
            document: documentText
        });
        return response.data.message; // e.g., "Document added successfully!"
    } catch (error) {
        winston.error(`Error in addDocument: ${error.message}`);
        throw new Error('Failed to add document to RAG service.');
    }
}

async function queryYoutubeRag(question) {
    try {
        const response = await axios.post(`${baseUrl}/rag-youtube-query`, {
            query: question
        });
        return response.data.answer; // or response.data as needed
    } catch (error) {
        winston.error(`Error in queryYoutubeRag: ${error.message}`);
        throw new Error('Failed to retrieve answer from YouTube RAG service.');
    }
}

export default { queryRag, addDocument, queryYoutubeRag };
