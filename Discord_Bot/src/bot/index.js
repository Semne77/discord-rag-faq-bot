import config from '../config/index.js';
import { Client, GatewayIntentBits } from 'discord.js';
import ragService from '../services/ragService.js'; // to call Python RAG API
import winston from '../services/loggingService.js'; // for structured logs


// Initialize Discord client
const client = new Client({
    intents: [
        GatewayIntentBits.Guilds,
        GatewayIntentBits.GuildMessages,
        GatewayIntentBits.MessageContent,
    ],
});

client.on("ready", () => {
    winston.info(`Logged in as ${client.user.tag}`);
});

// Message handler
client.on("messageCreate", async (msg) => {
    try {
        // Ignore bot messages
        if (msg.author.bot) return;

        // #ask <question>
        if (msg.content.startsWith("#ask ")) {
            const question = msg.content.replace("#ask ", "").trim();
            if (!question) {
                msg.reply("Please provide a question to ask.");
                return;
            }

            winston.info(`Received #ask: ${question} from ${msg.author.username}`);

            try {
                await msg.channel.sendTyping();
                const response = await ragService.queryRag(question);
                console.log("this is the responce",response)
                msg.reply(response);
            } catch (error) {
                winston.error(`Error in RAG query: ${error.message}`);
                msg.reply("Sorry, I couldn't get an answer right now.");
            }
            return;
        }

        // #add <document>
        if (msg.content.startsWith("#add ")) {
            const documentText = msg.content.replace("#add ", "").trim();
            if (!documentText) {
                msg.reply("Please provide the document text to add.");
                return;
            }

            winston.info(`Received #add from ${msg.author.username}`);

            try {
                await msg.channel.sendTyping();
                await ragService.addDocument(documentText);
                msg.reply("Document added successfully!");
            } catch (error) {
                winston.error(`Error in document ingestion: ${error.message}`);
                msg.reply("Sorry, I couldn't add the document right now.");
            }
            return;
        }

        if (msg.content.startsWith("#res")){
            const resource = msg.content.replace("#res ", "").trim();
            if (!resource) {
                msg.reply("Please specify the desired resource");
                return;
            }

            winston.info(`Received #res ${resource} from ${msg.author.username}`);


            try {
                await msg.channel.sendTyping();
                const response = await ragService.queryYoutubeRag(resource);
                msg.reply(response);
            } catch (error) {
                winston.error(`Error in YouTube RAG query: ${error.message}`);
                msg.reply("Sorry, I couldn't find relatable links");
            }
            return;
        }

        // (Optional) Add other commands here if needed

    } catch (error) {
        winston.error(`Unhandled error: ${error.stack}`);
        msg.reply("An unexpected error occurred.");
    }
});

// Login to Discord
client.login(config.discordToken);
