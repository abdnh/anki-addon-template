<script lang="ts">
    import {
        client,
        type GetStatsResponse,
        type SayHelloResponse,
    } from "$lib";
    import { bridgeCommand, promiseWithResolver } from "ankiutils";

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

<div class="flex flex-col items-center justify-center prose prose-2xl m-4 mx-auto text-center">
    <p>Bridge reply: {bridgeReply}</p>
    <p>
        Proto reply: {#await protoReplyPromise}<span
                class="loading loading-spinner loading-md"
            ></span>{:then response}
            {response.message}
        {/await}
    </p>
    <div class="mt-2">
        {#await statsPromise}
            <span class="loading loading-spinner w-16"></span>
        {:then response}
            <h2 class="text-2xl font-bold mb-2">Default deck stats:</h2>
            <div class="stats stats-vertical lg:stats-horizontal shadow">
                <div class="stat">
                    <div class="stat-title">Reviews</div>
                    <div class="stat-value">
                        {
                            response.stats?.reviews
                            ?? 0
                        }
                    </div>
                </div>
                <div class="stat">
                    <div class="stat-title">Seconds</div>
                    <div class="stat-value">
                        {
                            (response.stats
                            ?.timeSpent ?? 0n)
                            / 1000n
                        }
                    </div>
                </div>
            </div>
        {/await}
    </div>
</div>

<style lang="scss">
    :global(html) {
        font-size: 48px;
    }
</style>
