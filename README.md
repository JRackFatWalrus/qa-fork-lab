# qa-fixture-python

A PWR-authored fixture repository used to smoke-test PWR QA. It contains a tiny Python
package with one tested function (`add`) and one untested function (`apply_discount`).

- CI uses a read-only default token and no secrets.
- Pull requests opened here by PWR are drafts and are never merged automatically.

MIT licence.

## Lab use

This repository is PWR's public "customer" stand-in for the fork-publishing lab test: PWR forks it into `pwr-qa-lab` and opens a draft pull request back here. It contains a dummy `PWR_CANARY` Actions secret whose length is printed by CI to show fork pull requests run without secrets. It holds no real secrets. Never merge PWR's pull requests here.
