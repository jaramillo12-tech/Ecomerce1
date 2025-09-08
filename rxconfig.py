import reflex as rx

config = rx.Config(
    app_name="e_commerce_user_management",
    # Disable the sitemap plugin to remove warnings
    disable_plugins=["reflex.plugins.sitemap.SitemapPlugin"],
    # Optimize for development
    frontend_port=3001,
    backend_port=8001,
    # Disable HMR to prevent route errors
    disable_hmr=False,  # Keep HMR but with better error handling
)