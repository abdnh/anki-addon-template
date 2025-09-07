<script lang="ts">
import { bridgeCommand } from "$lib/bridgecommand";
import { onMount } from "svelte";

let reply: string = "";
onMount(() => {
    bridgeCommand("hello", (message) => {
        reply = message as string;
    });
});
</script>

<div class="container">
    <h1>{reply}</h1>
</div>

<style>
.container {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 89vh;
    padding: 2rem;
}

h1 {
    font-size: 2.5rem;
    font-weight: 300;
    color: #333;
    text-align: center;
    margin: 0;
    font-family:
        -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}
</style>
