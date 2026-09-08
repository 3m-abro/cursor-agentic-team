# ChatGPT adapter

Follow the shared runtime and select `team-orchestrator` when this plugin is
installed on a supported surface. Installation and available tools depend on the
host and account; this repository does not grant access or install itself.

A generated Markdown export is a reference document, not an installed plugin.
Ask ChatGPT to use the attached instructions and name a workflow. Source headings
in the export stand in for its internal file links. External dependency bodies
are not included: use available named skills/resources or report the missing step.

Ordinary chat may have no local filesystem, shell, persistent memory or subagents.
Execute roles sequentially and return outputs in chat when needed. Do not claim
local scripts ran or decisions were saved. For an actual plugin-capable local
runtime, use the packaged scripts and named dependency resolver if shell access
exists. Connect any required MCP tools separately through supported host setup.
Cursor `Task`, Multitask Mode and `/commands` are not ChatGPT APIs.
