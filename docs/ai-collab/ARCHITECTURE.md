# Architecture

Current architecture: [portable shared layers](../ARCHITECTURE.md).

Cursor discovery adapters and the OpenAI routing entry point read shared routing
and role instructions. Both manifests reference the same skills directory.
Named dependencies resolve through configuration and host-specific lookup defaults.
External tools remain session capabilities; files alone do not install them.
