# Digital Sales Rooms — Deployment

Full reference: [DIGITAL-SALES-ROOMS-DEPLOYMENT-DEPLOYMENT.md](DIGITAL-SALES-ROOMS-DEPLOYMENT-DEPLOYMENT.md)

## Deployment options

| Option | Advantages |
|--------|---------|
| **AWS Amplify** | Git-Push-Deployment, managed |
| **Cloudflare Pages** | Edge-Deployment, GitHub Actions |
| **Ubuntu Server + PM2** | self-hosted, full control |

## SaaS (Beyond)

In SaaS operation the plugin is already installed. All that remains:
1. Deploy the frontend app (one of the options above)
2. Configure the third-party services
3. Configure the plugin
