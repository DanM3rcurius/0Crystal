# Agent Registry Protocol (Outline)

## Overview

A protocol for decentralized discovery and interaction with agent-enabled Ordinal wallets.

## Components

### 1. Agent Metadata
- JSON schema embedded in an inscription or hosted endpoint
- Contains identity, capabilities, endpoint, and tags

### 2. Agent Gallery
- A curated collection of agents (Ord gallery or JSON list)
- Can be forked and remixed

### 3. Indexer Agent
- Crawls galleries and inscriptions
- Builds a searchable agent graph
- Optionally powers recommenders

### 4. Recommender Agent
- Suggests agents to collectors based on taste vectors
- Lives in-wallet or as a hosted API

### 5. Interaction Protocols
- PSBT for negotiation
- Webhooks or REST endpoints for dynamic logic

## Data Anchoring
- Nostr pubkeys for social trust
- Inscriptions for immutability
- IPFS as fallback

## Security Model
- Optional signing of agent metadata
- Community curation & gallery-based filtering
