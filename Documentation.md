Pulse – Module Extraction AI Agent
1. Introduction

This project is designed to automatically extract modules and submodules from product help or documentation websites.
The system analyzes the structure of documentation pages and converts them into a structured JSON format that represents how the product features are organized.

The focus of this project is robust structure inference, not simple scraping.

2. System Architecture Overview

The system follows a pipeline-based architecture, where each component has a clear responsibility.

Input URLs
   ↓
Crawler
   ↓
Content Parser
   ↓
Module & Submodule Extractor
   ↓
Structured JSON Output


Each stage operates independently to keep the system modular and easy to maintain.

3. Component Description
3.1 Crawler

Purpose:
The crawler is responsible for fetching documentation pages starting from the given URL(s).

Key Responsibilities:

Recursively crawls internal links only

Avoids external domains

Handles broken or inaccessible links gracefully

Uses a browser-like user agent to prevent blocked requests

Reasoning:
Documentation sites often block non-browser requests. Adding a user-agent improves reliability.

3.2 Content Parser

Purpose:
The parser extracts meaningful documentation content from raw HTML.

What it removes:

Navigation bars

Footers

Headers

Scripts and styles

What it extracts:

Headings (h1, h2, h3)

Paragraphs (p)

List items (li)

Design Choice:
Only semantic HTML elements are used to preserve document structure.

3.3 Module & Submodule Extraction

Purpose:
This component converts parsed content into a hierarchical structure.

Extraction Strategy:

Ensures at least one top-level module always exists

Treats headings as structural boundaries

Groups related text under the nearest heading

Builds descriptions only from extracted content

Why this approach:
Documentation sites do not follow a single standard. A flexible heuristic-based approach handles real-world inconsistencies.

4. Data Flow

User provides one or more documentation URLs

Crawler fetches relevant pages

Parser cleans and extracts meaningful content

Extractor builds module and submodule hierarchy

Output is returned as structured JSON

5. Design Decisions

Avoided hard-coded assumptions about heading levels

Chose robustness over perfect semantic accuracy

Kept crawling, parsing, and extraction as separate layers

Used Docker to ensure consistent execution across environments

6. Assumptions

Documentation is publicly accessible

HTML structure contains meaningful headings and text

Product features can be inferred from documentation layout

External links are not required for understanding structure
