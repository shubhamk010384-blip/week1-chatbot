# Week 3 Submission

## Features

- Persistent sessions
- Research Desk agent
- AGENTS.md procedural memory
- Web search tool
- Web fetch tool
- Paper search tool
- File read/write tools
- Notes directory
- Interactive REPL

## Design Decisions

I extended the Week 2 research agent into a Research Desk agent that can persist conversations across sessions. Sessions are stored as JSON files and automatically loaded when the agent restarts.

The project separates web tools, paper tools, and file tools into independent modules, making the system easier to maintain and extend.

AGENTS.md acts as procedural memory and guides the behaviour of the agent.

## Learnings

- Session persistence
- Agent architecture
- Tool design
- Research workflows
