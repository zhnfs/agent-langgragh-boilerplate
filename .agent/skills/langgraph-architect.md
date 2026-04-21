---
description: Expert in designing, building, and debugging stateful LangGraph workflows.
license: MIT
metadata:
  framework: LangGraph (Python)
  version: "1.0.0"
---

# LangGraph Architect Skill

Use this skill to design multi-agent systems, cyclic graphs, or long-running stateful workflows.

## Core Concepts
When designing a graph, always define:
- **State**: Use a `TypedDict` to represent the shared memory between nodes.
- **Nodes**: Python functions that receive the current state and return updates.
- **Edges**: Connections that define the control flow (conditional or direct).

## Design Rules
1. **Prefer Composition**: Break complex logic into smaller subgraphs or discrete nodes.
2. **State Immutability**: Ensure nodes return a *new* state dictionary rather than mutating the input directly.
3. **Use `Annotated`**: When multiple nodes write to the same state key (like `messages`), use `Annotated[list, add]` to ensure they append rather than overwrite.
