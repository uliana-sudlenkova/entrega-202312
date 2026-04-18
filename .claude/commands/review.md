# Review

Run a full code and security review on recently changed files.

## Instructions

1. Use `git diff HEAD~1` or `git status` to identify which files were changed
2. Run the `reviewer` agent on all changed HTML, CSS, and JS files
3. Run the `security` agent on all changed files — prioritize `netlify/functions/` and any inline scripts

## Report back
Combine both reports into a single output:

```
## Review Summary

### Code Quality (reviewer agent)
[paste reviewer report]

### Security (security agent)
[paste security report]

### Overall verdict
[APPROVE / REQUEST CHANGES]
[List of action items if changes requested]
```

If no files were changed recently, ask the user which files to review.
