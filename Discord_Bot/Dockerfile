# Use Node LTS base image
FROM node:20-alpine

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the code
COPY . .

# Set environment variable if needed
ENV NODE_ENV=production

# Expose a port if your bot uses one (optional, Discord bot does not need it)
# EXPOSE 3000

# Start the bot
CMD ["node", "src/bot/index.js"]
