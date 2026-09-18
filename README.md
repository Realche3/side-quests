# side-quests

Everything that isn't a "real" project: algorithm practice (mostly problems
solved on HackerRank), small experiments, and whatever else is fun to build
on the side. My portfolio links out to the merged PRs here so anyone can
follow along or leave a comment on a specific solution.

## Layout

```
dsa/    one file per algorithm/data-structure problem
fun/    small side experiments, one folder per thing
```

## Workflow

Every entry gets its own branch and its own PR — merged PRs keep their
comment threads forever, so a solution from months ago is still a place
someone can leave feedback.

```bash
git checkout -b solve/two-sum        # or build/<thing> for fun/ entries
# write the solution
git add dsa/two-sum.py
git commit -m "solve: two sum"
git push -u origin solve/two-sum
# open a PR on GitHub, then merge it
```

Each `dsa/` file starts with a comment linking to the original problem.
