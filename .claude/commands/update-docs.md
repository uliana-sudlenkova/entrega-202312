# Update Docs

Update project documentation to reflect recent changes.

## Instructions

Use the `docs` agent to:

1. Read the recent git changes (`git diff HEAD~1 --name-only`) to identify what changed
2. Read `CLAUDE.md` to understand current documentation state
3. Update CLAUDE.md if any of the following changed:
   - File structure (new or removed pages/functions)
   - Pricing packages or amounts
   - Required environment variables
   - Tech stack or dependencies
   - Build or deploy process

4. Add or update inline comments in changed files only where logic is non-obvious

## Output
Report what was updated:
```
## Documentation Update

### CLAUDE.md changes
- [section]: [what was updated]

### Inline comments
- [file:line]: [comment added/updated]

### No changes needed
- [section]: [reason it's still accurate]
```
