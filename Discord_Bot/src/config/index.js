import dotenv from 'dotenv';
dotenv.config();

export default {
    discordToken: process.env.TOKEN,
    pythonRagUrl: process.env.PYTHON_RAG_URL || 'http://localhost:8000',
    port: process.env.PORT || 3000,
    environment: process.env.NODE_ENV || 'development',
    logLevel: process.env.LOG_LEVEL || 'info',
};
