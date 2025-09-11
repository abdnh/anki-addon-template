import { createClient } from "@connectrpc/connect";
import { createConnectTransport } from "@connectrpc/connect-web";

import { BackendService, type GetStatsResponse } from "./generated/backend_pb";

const transport = createConnectTransport({
    baseUrl: "/api",
    useBinaryFormat: true,
    fetch: (input, init) => {
        console.log(init?.body, init?.headers);
        return fetch(input, { ...init });
    },
});

const client = createClient(BackendService, transport);

async function getStats(deckId: number): Promise<GetStatsResponse> {
    return client.getStats({ deckId: BigInt(deckId) });
}

export { getStats, type GetStatsResponse };
