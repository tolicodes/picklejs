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
