# Stage 1: Install dependencies
FROM node:18-slim AS deps
WORKDIR /The_blues_brothers
COPY package*.json ./
RUN npm ci --omit=dev

# Stage 2: Build the application
FROM deps AS build
COPY . .
RUN npm run build

# Stage 3: Production image
FROM node:18-slim
WORKDIR /The_blues_brothers
COPY --from=deps /The_blues_brothers/node_modules ./node_modules
COPY --from=build /The_blues_brothers .
ENV NODE_ENV=production
CMD ["node", "index.py"]
