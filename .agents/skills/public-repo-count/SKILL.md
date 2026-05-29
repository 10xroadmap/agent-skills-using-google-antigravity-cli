---
name: public-repo-count
description: Find the number of public repositories created by user
---

To find the number of public repositories created by user, first execute following shell script with username:

```bash
curl https://api.github.com/users/<username>
```

Parse output in JSON format and print the value of field `public_repos'
