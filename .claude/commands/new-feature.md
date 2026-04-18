# New Feature

Implement a new feature following the full development pipeline:

## Pipeline: Implement → Review → Security → QA → Docs

**Step 1 — Implement** (developer agent)
Use the `developer` agent to implement the feature described by the user.
- Read all relevant existing files before making changes
- Follow project conventions (Bootstrap 5, jQuery, existing CSS variables)
- Make the minimum change needed

**Step 2 — Review** (reviewer agent)
Use the `reviewer` agent to review all files changed in Step 1.
- Check quality, consistency, and correctness
- Report issues by severity (Critical / Warning / Suggestion)
- If Critical issues found: return to developer agent to fix before proceeding

**Step 3 — Security check** (security agent)
Use the `security` agent to audit the changed files.
- Focus on: XSS, secret exposure, Stripe security, injection
- If Critical or High findings: return to developer agent to fix before proceeding

**Step 4 — QA check** (qa agent)
Use the `qa` agent to verify no bugs were introduced.
- Check the payment flow, navigation links, JS selectors
- If Blocker bugs found: return to developer agent to fix

**Step 5 — Update docs** (docs agent)
Use the `docs` agent to update CLAUDE.md if:
- A new page was added
- A new Netlify Function was added
- Prices or packages changed
- New environment variables are required

## Output
At the end, provide a summary:
```
## Feature complete: [feature name]

### Changes made
- [file]: [description]

### Review: APPROVED / CHANGES MADE
### Security: PASS / ISSUES FIXED
### QA: PASS / BUGS FIXED
### Docs: UPDATED / NO CHANGES NEEDED
```
