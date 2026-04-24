# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is an **Obsidian vault** - a knowledge base for note-taking and linking ideas, not a traditional software project. The vault is backed up to git using the Obsidian Git community plugin.

## Vault Structure

- `1_raw/` - Raw/unprocessed source content (e.g., `articles/`)
- `2_wiki/` - Wiki-style notes organized by type: `concepts/`, `indexes/`, `summaries/`
- `3_outputs/` - Published or exported content (e.g., `Q&A/`, `health/`)
- `.obsidian/` - Obsidian application configuration and plugin data
- `.claudian/` - Claudian plugin settings and session data
- `.claude/` - Claude Code agent/command/skill configuration

## Active Plugins

- **Claudian** - AI assistant plugin integrating Claude into Obsidian (configured with Haiku model, `yolo` permission mode)
- **Obsidian Git** - Version control plugin for backing up the vault

## Claude Code Configuration

Claude Code is configured in `.claude/settings.json` with:
- Model: MiniMax-M2 via custom endpoint (`api.minimaxi.com`)
- Environment variables for API authentication are stored in this file

## Working with this Vault

This vault uses Chinese language for many notes. When searching or creating notes:
- The vault follows Obsidian conventions (markdown files, `[[wikilinks]]` for internal linking)
- Notes can have YAML frontmatter for metadata
