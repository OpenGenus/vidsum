# Commit Message Template

Please follow this template to make pull requests on this repository. We will use this format for all commits messages. The messages allow commits to stay small and easy to browse.

## The Layout

```
 <Type> : <Subject>

 <Body>

 <Footer>
```

#### Allowed Values for `Type`

- **feat** (new feature)
- **fix** (bug fix)
- **docs** (changes to documentation)
- **style** (formatting, missing semi colons, etc; no code change)
- **refactor** (refactoring production code)
- **test** (adding missing tests, refactoring tests; no production code change)

#### Subject

- All commits must be in [imperative](https://chris.beams.io/posts/git-commit/#imperative) tone. This tells what the commit does than what it did. For example, use **change**, not _changed_ or _changes_.
- The commit message should be less than or equal to 200 characters.
- The commit message must not end with a period, space, or tab.

#### Body 

- Briefly explain what the commit does with no more than 50 words.

#### Footer

- Please reference issues and pull-requests that relate to your commit. For example: "Issue #XXXX"

_Inspired by [Angular][angularc], [Karma][karmac] and [Sparkbox's][sparkb] commit style._



[angularc]: https://docs.google.com/document/d/1QrDFcIiPjSLDn3EL15IJygNPiHORgU1_OOAqWjiDU5Y/edit#
[karmac]: http://karma-runner.github.io/0.8/dev/git-commit-msg.html
[sparkb]: https://github.com/sparkbox/standard/blob/master/style/git/README.md