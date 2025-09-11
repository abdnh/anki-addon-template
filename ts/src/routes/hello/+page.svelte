<script lang="ts">
    import {
        client,
        type GetStatsResponse,
        promiseWithResolver,
        type SayHelloResponse,
    } from "$lib";
    import { bridgeCommand } from "$lib/bridgecommand";

    import { onMount } from "svelte";

    let bridgeReply: string = "";
    let [statsPromise, resolveStats] = promiseWithResolver<
        GetStatsResponse
    >();
    let [protoReplyPromise, resolveProtoReply] = promiseWithResolver<
        SayHelloResponse
    >();

    onMount(() => {
        bridgeCommand("hello", (message) => {
            bridgeReply = message as string;
        });
        client.getStats({ deckId: 1n }).then(resolveStats);
        client.sayHello({ name: "World" }).then(resolveProtoReply);
    });
</script>

<div class="container">
    <div>Bridge reply: {bridgeReply}</div>
    <div>
        Proto reply: {#await protoReplyPromise}(Loading...){:then response}
            {response.message}
        {/await}
    </div>
    <div class="stats-section">
        {#await statsPromise}
            <div class="loading">
                <p>Loading stats...</p>
            </div>
        {:then response}
            <div class="stats-container">
                <h2>Default deck stats:</h2>
                <div class="stats-grid">
                    <div class="stat-item">
                        <span class="stat-value">{
                            response.stats?.reviews ?? 0
                        }</span>
                        <span class="stat-label">Reviews</span>
                    </div>
                    <div class="stat-item">
                        <span class="stat-value">{
                            (response.stats?.timeSpent ?? 0n)
                            / 1000n
                        }</span>
                        <span class="stat-label">Seconds</span>
                    </div>
                </div>
            </div>
        {/await}
    </div>
</div>

<style>
    .container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        min-height: 89vh;
        padding: 2rem;
        gap: 2rem;
    }

    .stats-section {
        width: 100%;
        max-width: 600px;
    }

    .loading {
        text-align: center;
        padding: 2rem;
        color: #666;
        font-style: italic;
    }

    .stats-container {
        background: #f8f9fa;
        border-radius: 12px;
        padding: 2rem;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }

    .stats-container h2 {
        font-size: 1.5rem;
        font-weight: 500;
        color: #333;
        margin: 0 0 1.5rem 0;
        text-align: center;
        font-family:
            -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }

    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: 1.5rem;
    }

    .stat-item {
        background: white;
        border-radius: 8px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .stat-item:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }

    .stat-value {
        display: block;
        font-size: 2rem;
        font-weight: 600;
        color: #2563eb;
        margin-bottom: 0.5rem;
    }

    .stat-label {
        display: block;
        font-size: 0.875rem;
        font-weight: 500;
        color: #6b7280;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
</style>
