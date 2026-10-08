# PickleJS documentation restoration

Canonical architecture and deployment record, October 7, 2026.

## Source and scope

The original repository is [hoverinc/picklejs](https://github.com/hoverinc/picklejs), archived upstream at `a73995ad8154a3396e3931eea3f139dda843b5b7`. This repository preserves its Git history and Apache 2.0 license. The documentation is restored independently at `https://picklejs.toli.me`; the Cypress/Cucumber library, npm package and upstream maintenance status are unchanged. GitHub refused the fork API, so the public `tolicodes/picklejs` repository is a history-preserving source copy.

## Rendering and build contract

`docs/` and `website/pages/` render through Docusaurus 1.14.7 (resolved in `website/package-lock.json`) into static HTML/CSS/JavaScript/images in `website/build/picklejs/`. There is no application backend or database. The restored hostname is the canonical URL and sitemap origin. Original documentation, artwork, slide embed, HOVER attribution and upstream GitHub links remain; homepage/footer explicitly label the library as archived. A missing blog title is populated from its existing heading, footer documentation links omit a nonexistent language path, and getting-started example URLs point to the restored routes.

The old npm lock was incomplete; the regenerated lock supports `npm ci`. Install with lifecycle scripts disabled and skip image compression, retaining original image bytes and avoiding obsolete platform-specific optimizer executables/Cypress installation. Build on Node 22 with `NODE_OPTIONS=--openssl-legacy-provider` (legacy build tooling only):

```sh
cd website
npm ci --ignore-scripts --legacy-peer-deps --no-audit --no-fund
NODE_OPTIONS=--openssl-legacy-provider npm run build
cd ..
python3 scripts/check-docs.py
```

The Node 22 static build passes; 31 HTML pages, 708 local references, canonical metadata and the exact license copy pass verification. Node 26 also built successfully. Highlight.js 9 reports its existing end-of-life warning. Restoring the documentation does not establish compatibility of the old library with current Cypress or test the external slides, Algolia, analytics or GitHub widgets.

## Hosting and planned connection

Reuse existing Netlify site `9d08dc94-9f99-4e43-9d85-395e29c50c0a` (`focused-yalow-c31386.netlify.app`). Its preserved October 2019 deploy is `5db233ac2f7830d3b44ef807`. `netlify.toml` defines the reproducible website build, Node 22, static output and legacy `/phrases`, `/getting-started`, `/docs/en/*` redirects. The `/license` path serves the original license.

The intended Cloudflare DNS record is a DNS-only CNAME `picklejs.toli.me` → `focused-yalow-c31386.netlify.app`, with Netlify managing trusted HTTPS. The old `picklejs.com` registration is expired and remains separate; restoration does not renew or recover it. Unrelated DNS/mail records remain outside this task.

At this source commit, the candidate is built and checked, but the new domain/deployment is not yet verified. Publish this committed source, verify the Netlify deployment and custom-host TLS/assets/docs, then retain the exact source SHA, deploy identity, DNS and public verification in `deployments/`. Original raw provider responses and matched screenshots stay outside Git at `/Users/toli/Documents/picklejs-redeploy-2026-10-07/`.


## Verified publication — October 7, 2026

Source `9fbc8ad84bfc251a0e1f98482e97fb0ab9872919` is pushed to `tolicodes/picklejs/master`. Production deploy `6ac713db9d83e7a4a076de72` is ready and serves `https://picklejs.toli.me`. Authoritative DNS and 1.1.1.1 resolve the intended DNS-only CNAME; HTTP upgrades to HTTPS with 301. The edge serves a trusted Let's Encrypt `*.toli.me` certificate valid through January 4, 2027. The site-specific certificate API retains an expired old-domain record and its provision endpoint returned 422; actual HTTPS verification succeeds. A future renewal cycle remains unobserved.

All 49 generated files return trusted HTTPS 200. Eighteen non-HTML assets match exact bytes; 31 HTML pages match after normalizing Netlify's existing Pretty URLs link rewriting. Legacy route redirects and license delivery pass. Browser navigation confirms the homepage, original presentation and Getting Started documentation. The [sanitized deployment receipt](deployments/2026-10-07-restoration.json) and [build hashes](deployments/2026-10-07-build-sha256.json) pin the exact source/artifact. Matched original/restored desktop evidence remains in the local receipt folder.

This was a manual static deployment; the existing Netlify Git build link still points at archived upstream. To redeploy future committed documentation changes, run the build/check commands above, then `netlify deploy --prod --site 9d08dc94-9f99-4e43-9d85-395e29c50c0a --dir website/build/picklejs --no-build` from the repository root. This documentation/receipt follow-up does not change the deployed artifact.
