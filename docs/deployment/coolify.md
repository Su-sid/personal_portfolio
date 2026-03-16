# Coolify deployment

This repository now ships with a GitHub Actions pipeline and a Coolify-specific Docker Compose stack for production.

## What the pipeline does

- On every pull request to `main`, it runs:
  - backend `ruff check`
  - backend `ruff format --check`
  - backend `pytest`
  - frontend `npm run lint` (`nuxt typecheck`)
  - frontend `npm run build`
  - Docker Compose validation for both local and Coolify stacks
- On every push to `main`, after the same checks pass, it:
  - calculates the next git tag
  - starts at `v0.0.0` if there are no existing release tags
  - increments the patch version for each later push to `main`
  - builds and pushes backend and frontend images to GHCR
  - publishes the git tag after both images build successfully
  - updates the `latest` image tag
  - triggers a Coolify redeploy through the deployment webhook

## Files involved

- Workflow: `.github/workflows/ci-cd.yml`
- Coolify stack: `docker-compose.coolify.yml`

## Coolify setup

This follows Coolify's current guidance for GitHub Actions deployments with prebuilt container images and Docker Compose.

1. In Coolify, create an application from your Git repository.
2. Choose `Docker Compose` as the build pack.
3. Set:
   - `Base Directory`: `/`
   - `Docker Compose Location`: `docker-compose.coolify.yml`
4. In Coolify settings, enable API access.
5. Create an API token with deploy permission.
6. From the application `Webhook` page, copy the deployment webhook URL.

## GitHub secrets

Add these repository secrets in GitHub:

- `COOLIFY_TOKEN`: the Coolify API token with deploy permission
- `COOLIFY_WEBHOOK`: the application webhook URL from Coolify

No extra registry secret is needed in GitHub Actions because the workflow pushes to GHCR with the built-in `GITHUB_TOKEN`.

## Coolify environment variables

Set these in the Coolify application environment:

- `BACKEND_IMAGE=ghcr.io/<github-owner>/personal-portfolio-backend:latest`
- `FRONTEND_IMAGE=ghcr.io/<github-owner>/personal-portfolio-frontend:latest`
- `DATABASE_URL=postgresql://<user>:<password>@db:5432/<database>`
- `SECRET_KEY=<strong-random-secret>`
- `POSTGRES_DB=<database>`
- `POSTGRES_USER=<database-user>`
- `POSTGRES_PASSWORD=<database-password>`
- `ALLOWED_HOSTS=<your-domain>,localhost,127.0.0.1`
- `CSRF_TRUSTED_ORIGINS=https://<your-domain>`

Set any additional mail, social, or site metadata variables there as needed. The compose file includes sensible defaults for non-critical values.

## GHCR access on the server

If the repository or package is private, the Coolify server must be able to pull from GHCR.

Use either:

- a Docker registry entry in Coolify for `ghcr.io`
- or `docker login ghcr.io -u <github-user> --password-stdin` on the server

## Branch protection

To block production deploys from unverified code, configure GitHub branch protection on `main` and require these status checks:

- `Backend Checks`
- `Frontend Checks`
- `Compose Validation`

That ensures pull requests cannot merge until the same checks the deployment pipeline depends on are green.

## Notes

- The production deploy uses the immutable git tag for release history and also updates `latest` so Coolify can keep pulling one stable image reference.
- The frontend check is intentionally `nuxt typecheck` plus a full production build, since there is no dedicated frontend linter configured yet.

## References

- Coolify GitHub auto-deploy: https://coolify.io/docs/applications/ci-cd/github/auto-deploy
- Coolify GitHub Actions: https://coolify.io/docs/applications/ci-cd/github/actions
- Coolify Docker Compose build pack: https://coolify.io/docs/applications/build-packs/docker-compose
- Coolify Nuxt: https://coolify.io/docs/applications/nuxt
- Coolify Django: https://coolify.io/docs/applications/django
