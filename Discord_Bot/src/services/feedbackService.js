import winston from './loggingService.js';

async function storeFeedback(feedback) {
    try {
        winston.info({
            message: 'User feedback',
            feedback,
            timestamp: new Date().toISOString()
        });
        return { status: 'success', message: 'Feedback logged successfully' };
    } catch (error) {
        winston.error(`Error logging feedback: ${error.message}`);
        throw new Error('Failed to store feedback');
    }
}

export default { storeFeedback };
