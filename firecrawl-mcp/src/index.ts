#!/usr/bin/env node
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from '@modelcontextprotocol/sdk/types.js';
import FirecrawlApp from '@mendable/firecrawl-js';
import * as dotenv from 'dotenv';

// Load environment variables
dotenv.config();

const API_KEY = process.env.FIRECRAWL_API_KEY;

if (!API_KEY) {
  console.error('Error: FIRECRAWL_API_KEY environment variable is required');
  process.exit(1);
}

// Initialize Firecrawl
const firecrawl = new FirecrawlApp({ apiKey: API_KEY });

// Create MCP server
const server = new Server(
  {
    name: 'firecrawl-mcp-server',
    version: '1.0.0',
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// List available tools
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: 'scrape_url',
        description: 'Scrape a single URL and return its content in markdown format. Perfect for extracting content from a single page.',
        inputSchema: {
          type: 'object',
          properties: {
            url: {
              type: 'string',
              description: 'The URL to scrape',
            },
            formats: {
              type: 'array',
              items: {
                type: 'string',
                enum: ['markdown', 'html', 'rawHtml', 'links', 'screenshot'],
              },
              description: 'Formats to return (default: ["markdown", "html"])',
              default: ['markdown', 'html'],
            },
            onlyMainContent: {
              type: 'boolean',
              description: 'Only return the main content of the page (default: true)',
              default: true,
            },
            includeTags: {
              type: 'array',
              items: { type: 'string' },
              description: 'Only include tags, classes and ids from the page',
            },
            excludeTags: {
              type: 'array',
              items: { type: 'string' },
              description: 'Tags, classes and ids to exclude from the page',
            },
            waitFor: {
              type: 'number',
              description: 'Wait for a specific amount of time in milliseconds before scraping',
            },
          },
          required: ['url'],
        },
      },
      {
        name: 'crawl_website',
        description: 'Crawl multiple pages of a website starting from a URL. Returns content from all discovered pages.',
        inputSchema: {
          type: 'object',
          properties: {
            url: {
              type: 'string',
              description: 'The starting URL to crawl',
            },
            maxDepth: {
              type: 'number',
              description: 'Maximum depth to crawl (default: 2)',
              default: 2,
            },
            limit: {
              type: 'number',
              description: 'Maximum number of pages to crawl (default: 10)',
              default: 10,
            },
            includePaths: {
              type: 'array',
              items: { type: 'string' },
              description: 'Only include URLs matching these patterns',
            },
            excludePaths: {
              type: 'array',
              items: { type: 'string' },
              description: 'Exclude URLs matching these patterns',
            },
          },
          required: ['url'],
        },
      },
      {
        name: 'map_website',
        description: 'Map all URLs found on a website starting from a URL. Returns a list of all discovered URLs without scraping content.',
        inputSchema: {
          type: 'object',
          properties: {
            url: {
              type: 'string',
              description: 'The starting URL to map',
            },
            search: {
              type: 'string',
              description: 'Search term to filter URLs',
            },
            ignoreSitemap: {
              type: 'boolean',
              description: 'Ignore the website sitemap (default: false)',
              default: false,
            },
            includeSubdomains: {
              type: 'boolean',
              description: 'Include subdomains (default: false)',
              default: false,
            },
            limit: {
              type: 'number',
              description: 'Maximum number of URLs to return (default: 5000)',
              default: 5000,
            },
          },
          required: ['url'],
        },
      },
    ],
  };
});

// Handle tool calls
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  try {
    const { name, arguments: args } = request.params;

    switch (name) {
      case 'scrape_url': {
        const { url, formats, onlyMainContent, includeTags, excludeTags, waitFor } = args as {
          url: string;
          formats?: ('markdown' | 'html' | 'rawHtml' | 'links' | 'screenshot')[];
          onlyMainContent?: boolean;
          includeTags?: string[];
          excludeTags?: string[];
          waitFor?: number;
        };

        const result = await firecrawl.scrapeUrl(url, {
          formats: (formats as any) || ['markdown', 'html'],
          onlyMainContent: onlyMainContent !== false,
          includeTags,
          excludeTags,
          waitFor,
        });

        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify(result, null, 2),
            },
          ],
        };
      }

      case 'crawl_website': {
        const { url, maxDepth, limit, includePaths, excludePaths } = args as {
          url: string;
          maxDepth?: number;
          limit?: number;
          includePaths?: string[];
          excludePaths?: string[];
        };

        const result = await firecrawl.crawlUrl(url, {
          maxDepth: maxDepth || 2,
          limit: limit || 10,
          includePaths,
          excludePaths,
        });

        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify(result, null, 2),
            },
          ],
        };
      }

      case 'map_website': {
        const { url, search, ignoreSitemap, includeSubdomains, limit } = args as {
          url: string;
          search?: string;
          ignoreSitemap?: boolean;
          includeSubdomains?: boolean;
          limit?: number;
        };

        const result = await firecrawl.mapUrl(url, {
          search,
          ignoreSitemap: ignoreSitemap || false,
          includeSubdomains: includeSubdomains || false,
          limit: limit || 5000,
        });

        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify(result, null, 2),
            },
          ],
        };
      }

      default:
        throw new Error(`Unknown tool: ${name}`);
    }
  } catch (error) {
    const errorMessage = error instanceof Error ? error.message : String(error);
    return {
      content: [
        {
          type: 'text',
          text: `Error: ${errorMessage}`,
        },
      ],
      isError: true,
    };
  }
});

// Start server
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error('Firecrawl MCP Server running on stdio');
}

main().catch((error) => {
  console.error('Fatal error in main():', error);
  process.exit(1);
});
