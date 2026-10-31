# Deployment

- Live URL: https://f78e4c7a.apex-cat-lab.pages.dev
- Provider: Cloudflare Pages project `apex-cat-lab`
- Release: `f78e4c7a-9532-4aef-901d-2ca00a71dfb2` (stage `success`)
- Method: direct Pages upload with a bundled `_worker.js` serving the app files.
- The Supabase JavaScript client is served locally from `/vendor/`; the site does not require a third-party CDN for it.
- Account sign-up/sign-in and practice event sync are implemented. Configure the Supabase Auth Site URL and redirect allow-list with `https://f78e4c7a.apex-cat-lab.pages.dev/` before email confirmation flow is used.
- The existing project uses Direct Upload. Cloudflare does not let an existing Direct Upload project switch to its native Git integration. To keep this project and Pages name, a GitHub Actions direct-upload workflow is prepared in `.github/workflows/deploy-pages.yml` and builds a clean static bundle with `scripts/build-pages.mjs`.
- Automatic CI deployment is **not active yet**. Add GitHub Actions secrets `CLOUDFLARE_ACCOUNT_ID` and `CLOUDFLARE_API_TOKEN` to the private repository. Cloudflare's current Pages CI guide specifies an account-scoped API token with Cloudflare Pages Edit. Do not put the token in the repository or workflow file.

The current local Pages bundle builds and serves the approved, labelled 25-question Research Pilot alongside the three existing samples. The deployed production release listed above predates that pilot, so the production site continues to serve the earlier release until authenticated deployment access is available. The existing project and URL are preserved.

The live site currently contains three original sample questions. It is an initial practice studio, not a fully researched CAT question bank. See [BUILD_STATUS.md](BUILD_STATUS.md) for outstanding work and evidence limits.

