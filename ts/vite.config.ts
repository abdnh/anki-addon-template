import { sveltekit } from "@sveltejs/kit/vite";
import { defineConfig } from "vite";

function configureProxy(proxy: any, _options: any) {
    proxy.on("error", (err: any) => {
        console.log("proxy error", err);
    });
    proxy.on("proxyReq", (_proxyReq: any, req: any) => {
        console.log("Sending Request to the Target:", req.method, req.url);
    });
    proxy.on("proxyRes", (proxyRes: any, req: any) => {
        console.log("Received Response from the Target:", proxyRes.statusCode, req.url);
    });
}

export default defineConfig({
    plugins: [sveltekit()],
    test: {
        expect: { requireAssertions: true },
        projects: [
            {
                extends: "./vite.config.ts",
                test: {
                    name: "server",
                    environment: "node",
                    include: ["src/**/*.{test,spec}.{js,ts}"],
                    exclude: ["src/**/*.svelte.{test,spec}.{js,ts}"],
                },
            },
        ],
    },
    server: {
        port: 5174,
        proxy: {
            "/api": {
                target: "http://localhost:40001",
                changeOrigin: true,
                autoRewrite: true,
                configure: configureProxy,
            },
        },
    },
    css: {
        preprocessorOptions: {
            scss: {
                silenceDeprecations: ["color-functions", "global-builtin", "import"],
            },
        },
    },
});
