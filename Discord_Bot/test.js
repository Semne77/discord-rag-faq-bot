import dotenv from "dotenv";
dotenv.config();

import { Client, GatewayIntentBits } from 'discord.js';

// Initialize Discord client
const client = new Client({
    intents: [
        GatewayIntentBits.Guilds,
        GatewayIntentBits.GuildMessages,
        GatewayIntentBits.MessageContent,
    ],
});

client.on("ready", () => {
    console.log(`Logged in as ${client.user.tag}`);
});

// Login to Discord
client.login(process.env.TOKEN);