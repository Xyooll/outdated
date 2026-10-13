# Xyool's own Node WebSocket signaling service. No media passes through here.
# Railway terminates HTTPS/WSS and forwards internally to process.env.PORT.
FROM node:22-alpine
ENV NODE_ENV=production
ENV HOST=0.0.0.0
ENV XYOOL_ID_REGISTRY=/data/registry.json
WORKDIR /app

COPY package.json ./
RUN npm install --omit=dev --ignore-scripts --no-audit --no-fund
# Copy the module tree as a unit to keep ESM imports available.
COPY ./ ./
RUN node -e "import('./server-id.mjs').then(()=>console.log('Signaling modules import successfully'))"

# A persistent service volume MUST be mounted on /data.
# Railway-provided volumes are mounted as root; keep this small isolated
# container dedicated to signaling. Harden further before larger rollouts.
EXPOSE 8788
CMD ["node","server-id.mjs"]
