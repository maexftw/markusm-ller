---
name: review-html
description: Conduct a comprehensive design review of static HTML files using the design-review agent
---

You need to invoke the design-review agent to conduct a comprehensive design review of static HTML files.

First, start a local web server to serve the HTML file, then use the design-review agent to systematically review the UI following the phases outlined in /.claude/agents/design-review-agent.md.

The agent will:
1. Prepare by analyzing the HTML file and setting up Playwright
2. Test interaction and user flows
3. Verify responsiveness across viewports (Desktop 1440px, Tablet 768px, Mobile 375px)
4. Assess visual polish and consistency
5. Check accessibility compliance (WCAG 2.1 AA)
6. Test robustness and edge cases
7. Review code health
8. Check content and console for issues

Steps:
1. Start a simple HTTP server to serve the HTML file (e.g., using Python or npx http-server)
2. Use the Task tool to invoke the design-review agent with the following prompt:

"Review the HTML file at {file_path}. Start a local web server on port 8000 to serve this file, then conduct a comprehensive design review following all phases in your methodology. Provide a structured report with findings categorized as Blockers, High-Priority, Medium-Priority, and Nitpicks."

The final output should be a markdown report following the structure defined in the agent configuration.
